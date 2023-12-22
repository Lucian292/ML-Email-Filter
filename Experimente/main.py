import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_emails_from_folder(folder_path):
    emails = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                email_text = file.read()
                emails.append(email_text)
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

    # Creăm vectori de caracteristici folosind CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_emails)

    # Împărțim datele în set de antrenare și set de testare
    X_train, X_test, y_train, y_test = train_test_split(X, all_labels, test_size=0.2, random_state=42)

    # Antrenăm un clasificator Naive Bayes
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)

    # Clasificăm datele de testare
    predictions = classifier.predict(X_test)

    # Calculăm precizia clasificatorului
    accuracy = accuracy_score(y_test, predictions)
    print(f'Accuracy: {accuracy}')

    # Încarcăm datele de testare
    test_emails = load_emails_from_folder(test_folder)

    # Vectorizăm datele de testare
    X_test_emails = vectorizer.transform(test_emails)

    # Clasificăm emailurile de testare
    test_predictions = classifier.predict(X_test_emails)

    # Scriem rezultatele în fișiere de output
    with open('spam_results.txt', 'w', encoding='utf-8') as spam_output, \
            open('non_spam_results.txt', 'w', encoding='utf-8') as non_spam_output, \
            open('features_used.txt', 'w', encoding='utf-8') as features_output:

        # Scriem cuvintele folosite pentru caracteristici
        features_output.write('\n'.join(vectorizer.get_feature_names_out()))

        # Scriem rezultatele de clasificare
        for filename, prediction in zip(os.listdir(test_folder), test_predictions):
            if prediction == 1:
                spam_output.write(f'{filename}\n')
            else:
                non_spam_output.write(f'{filename}\n')

# Specificăm căile către folderele cu datele de antrenare și testare
spam_folder_path = '../Sorted Emails/spam'
non_spam_folder_path = '../Sorted Emails/non-spam'
test_folder_path = '../emails/test data/part10'

# Antrenăm și clasificăm emailurile
train_and_classify(spam_folder_path, non_spam_folder_path, test_folder_path)
