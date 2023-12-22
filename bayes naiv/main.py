import os
from naive_bayes import NaiveBayesClassifier


def load_emails_from_folder(folder_path):
    emails = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.txt'):
                filepath = os.path.join(root, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    email_text = file.read()
                    emails.append(email_text.split())  # Convertim textul într-o listă de cuvinte
    return emails


def train_and_classify(spam_folder, non_spam_folder, test_folder):
    # Încarcăm datele de antrenare
    spam_emails = load_emails_from_folder(spam_folder)
    non_spam_emails = load_emails_from_folder(non_spam_folder)
    print("spam_emails and non_spam_emails loaded")

    # Etichetăm datele cu 1 pentru spam și 0 pentru non-spam
    spam_labels = [1] * len(spam_emails)
    non_spam_labels = [0] * len(non_spam_emails)
    print("spam_labels and non_spam_labels loaded")

    # Îmbinăm datele de spam și non-spam
    all_emails = spam_emails + non_spam_emails
    all_labels = spam_labels + non_spam_labels
    print("all_emails and all_labels loaded")

    # Antrenăm un clasificator Naive Bayes
    classifier = NaiveBayesClassifier()
    classifier.fit(all_emails, all_labels)
    print("classifier fitted")

    # Încarcăm datele de testare
    test_emails = load_emails_from_folder(test_folder)
    print("test_emails loaded")

    # Clasificăm emailurile de testare
    test_predictions = classifier.predict(test_emails)
    print("test_predictions loaded")

    # Scriem rezultatele în fișiere de output
    with open('spam_results.txt', 'w', encoding='utf-8') as spam_output:
        for root, _, files in os.walk(test_folder):
            for filename in files:
                if filename.endswith('.txt'):
                    filepath = os.path.join(root, filename)
                    prediction = test_predictions[0]  # Atenție la acest pas - test_predictions pare să fie o listă
                    if prediction == 1:
                        spam_output.write(f'{filename}\n')

    with open('non_spam_results.txt', 'w', encoding='utf-8') as non_spam_output:
        for root, _, files in os.walk(test_folder):
            for filename in files:
                if filename.endswith('.txt'):
                    filepath = os.path.join(root, filename)
                    prediction = test_predictions[0]  # Atenție la acest pas - test_predictions pare să fie o listă
                    if prediction == 0:
                        non_spam_output.write(f'{filename}\n')


# Specificăm căile către folderele cu datele de antrenare și testare
spam_folder_path = '../Sorted Emails/spam'
non_spam_folder_path = '../Sorted Emails/non-spam'
test_folder_path = '../test data'

# Antrenăm și clasificăm emailurile
train_and_classify(spam_folder_path, non_spam_folder_path, test_folder_path)
