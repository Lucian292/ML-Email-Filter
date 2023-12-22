import os
from naive_bayes import NaiveBayesClassifier


def load_emails_from_folder(folder_path):
    emails = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                email_text = file.read()
                emails.append(email_text.split())  # Convertim textul într-o listă de cuvinte
    return emails


def train_and_classify(spam_folder, non_spam_folder, test_folder):
    # Încarcăm datele de antrenare
    spam_emails = load_emails_from_folder(spam_folder)
    non_spam_emails = load_emails_from_folder(non_spam_folder)

    # Etichetăm datele cu 1 pentru spam și 0 pentru non-spam
    spam_labels = [1] * len(spam_emails)
    non_spam_labels = [0] * len(non_spam_emails)

    # Îmbinăm datele de spam și non-spam
    all_emails = spam_emails + non_spam_emails
    all_labels = spam_labels + non_spam_labels

    # Antrenăm un clasificator Naive Bayes
    classifier = NaiveBayesClassifier()
    classifier.fit(all_emails, all_labels)

    # Încarcăm datele de testare
    test_emails = load_emails_from_folder(test_folder)

    # Clasificăm emailurile de testare
    test_predictions = classifier.predict(test_emails)

    # Scriem rezultatele în fișiere de output
    with open('../spam_results.txt', 'w', encoding='utf-8') as spam_output:
        for filename, prediction in zip(os.listdir(test_folder), test_predictions):
            if prediction == 1:
                spam_output.write(f'{filename}\n')

    with open('../non_spam_results.txt', 'w', encoding='utf-8') as non_spam_output:
        for filename, prediction in zip(os.listdir(test_folder), test_predictions):
            if prediction == 0:
                non_spam_output.write(f'{filename}\n')


# Specificăm căile către folderele cu datele de antrenare și testare
spam_folder_path = 'C:/Users/user/Desktop/lingspam_public/spam'
non_spam_folder_path = 'C:/Users/user/Desktop/lingspam_public/non-spam'
test_folder_path = 'C:/Users/user/Desktop/lingspam_public/part10'

# Antrenăm și clasificăm emailurile
train_and_classify(spam_folder_path, non_spam_folder_path, test_folder_path)
