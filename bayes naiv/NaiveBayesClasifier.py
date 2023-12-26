import os
import re
from collections import defaultdict


def tokenize(text):
    # Simplificare: vom folosi spațiul și punctuația pentru tokenizare
    return re.findall(r'\b\w+\b', text)


def load_emails_from_directory(directory):
    emails = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    emails.append((file, content))
    return emails


def train_naive_bayes(train_directory):
    # Pregătește dicționare pentru a număra cuvintele în documente spam și non-spam
    word_count_spam = defaultdict(int)
    word_count_non_spam = defaultdict(int)
    total_spam_emails = 0
    total_non_spam_emails = 0

    train_data = load_emails_from_directory(train_directory)

    for email in train_data:
        file_name, content = email
        tokens = tokenize(content.lower())

        if 'spm' in file_name:
            total_spam_emails += 1
            for token in tokens:
                word_count_spam[token] += 1
        else:
            total_non_spam_emails += 1
            for token in tokens:
                word_count_non_spam[token] += 1

    return word_count_spam, word_count_non_spam, total_spam_emails, total_non_spam_emails


def classify_emails(test_directory, word_count_spam, word_count_non_spam, total_spam_emails, total_non_spam_emails):
    test_data = load_emails_from_directory(test_directory)
    filenames_spam = []
    filenames_non_spam = []

    for email in test_data:
        file_name, content = email
        tokens = tokenize(content.lower())

        # Calculează probabilitatea că un email este spam sau non-spam
        prob_spam = total_spam_emails / (total_spam_emails + total_non_spam_emails)
        prob_non_spam = total_non_spam_emails / (total_spam_emails + total_non_spam_emails)

        for token in tokens:
            # Calculează probabilitatea că un cuvânt să apară într-un email spam sau non-spam
            prob_word_given_spam = (word_count_spam[token] + 1) / (sum(word_count_spam.values()) + len(word_count_spam))
            prob_word_given_non_spam = (word_count_non_spam[token] + 1) / (
                        sum(word_count_non_spam.values()) + len(word_count_non_spam))

            # Ajustează probabilitățile cu logaritmul pentru a evita subfluctuațiile
            prob_spam += prob_word_given_spam
            prob_non_spam += prob_word_given_non_spam

        # Decide dacă email-ul este spam sau non-spam pe baza probabilităților calculate
        if prob_spam > prob_non_spam:
            filenames_spam.append(file_name)
        else:
            filenames_non_spam.append(file_name)

    return filenames_spam, filenames_non_spam


def save_results_to_txt(results, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + '\n')


# Antrenează algoritmul Naive Bayes pe datele de antrenare
word_count_spam, word_count_non_spam, total_spam_emails, total_non_spam_emails = train_naive_bayes(
    r'D:\Universitate\ML\tema practica\ML-Email-Filter\emails\lemm_stop')

# Clasifică datele de test și salvează rezultatele
spam_files, non_spam_files = classify_emails(r'D:\Universitate\ML\tema practica\ML-Email-Filter\test data\lemm_stop',
                                             word_count_spam, word_count_non_spam, total_spam_emails,
                                             total_non_spam_emails)

save_results_to_txt(spam_files, r'D:\Universitate\ML\tema practica\ML-Email-Filter\bayes naiv\classified_as_spam.txt')
save_results_to_txt(non_spam_files,
                    r'D:\Universitate\ML\tema practica\ML-Email-Filter\bayes naiv\classified_as_non_spam.txt')
