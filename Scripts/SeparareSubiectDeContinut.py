import os
import re

def extract_subject_and_content(email_text):
    # Căutare după linia care începe cu "Subject:"
    subject_match = re.search(r'^Subject: (.+)$', email_text, flags=re.MULTILINE | re.IGNORECASE)

    if subject_match:
        subject = subject_match.group(1).strip()
    else:
        subject = ""

    # Separare între subiect și conținut
    content_start = email_text.find("\n\n")
    if content_start != -1:
        content = email_text[content_start + 2:]
    else:
        content = ""

    return subject, content

def process_emails(source_folder, subject_folder, content_folder):
    # Parcurgere recursivă a folderului sursă
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)

                # Citirea conținutului emailului
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    email_text = file.read()

                # Extrage subiectul și conținutul
                subject, content = extract_subject_and_content(email_text)

                # Salvare în folderele corespunzătoare
                subject_path = os.path.join(subject_folder, file_name)
                content_path = os.path.join(content_folder, file_name)

                with open(subject_path, 'w', encoding='utf-8') as subject_file:
                    subject_file.write(subject)

                with open(content_path, 'w', encoding='utf-8') as content_file:
                    content_file.write(content)

if __name__ == "__main__":
    # Specificațiile folderelor
    non_spam_source_folder = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\Entire\non-spam'
    spam_source_folder = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\Entire\spam'

    non_spam_subject_folder = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\Non-SpamEmails\Subject'
    non_spam_content_folder = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\Non-SpamEmails\Content'

    spam_subject_folder = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\SpamEmails\Subject'
    spam_content_folder = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\SpamEmails\Content'

    # Crearea folderelor de destinatie daca nu exista
    os.makedirs(non_spam_subject_folder, exist_ok=True)
    os.makedirs(non_spam_content_folder, exist_ok=True)
    os.makedirs(spam_subject_folder, exist_ok=True)
    os.makedirs(spam_content_folder, exist_ok=True)

    # Procesarea emailurilor non-spam
    process_emails(non_spam_source_folder, non_spam_subject_folder, non_spam_content_folder)

    # Procesarea emailurilor spam
    process_emails(spam_source_folder, spam_subject_folder, spam_content_folder)
