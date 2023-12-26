import os
import re

def separate_subject_content(email_text):
    # Utilizează expresii regulate pentru a separa subiectul și conținutul
    match = re.match(r"Subject: (.+?)\n\n(.+)", email_text, re.DOTALL)
    if match:
        subject, content = match.groups()
        return subject, content
    return None, None

def process_emails_folder(folder_path, subjects_path, content_path):
    # Creează folderele pentru subiecte și conținut dacă nu există deja
    os.makedirs(subjects_path, exist_ok=True)
    os.makedirs(content_path, exist_ok=True)

    # Parcurge recursiv folderele și găsește fișierele .txt
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)

                # Deschide fișierul și citește conținutul
                with open(file_path, "r", encoding="utf-8") as f:
                    email_text = f.read()

                # Separă subiectul și conținutul
                subject, content = separate_subject_content(email_text)

                if subject is not None and content is not None:
                    # Salvează subiectul într-un fișier separat
                    subject_file_path = os.path.join(subjects_path, f"{file[:-4]}_subject.txt")
                    with open(subject_file_path, "w", encoding="utf-8") as subject_file:
                        subject_file.write(subject)

                    # Salvează conținutul într-un fișier separat
                    content_file_path = os.path.join(content_path, f"{file[:-4]}_content.txt")
                    with open(content_file_path, "w", encoding="utf-8") as content_file:
                        content_file.write(content)

# Specifică căile pentru foldere
emails_folder_path = r"D:\Universitate\ML\tema practica\ML-Email-Filter\test data\lemm_stop"
subjects_output_path = r"D:\Universitate\ML\tema practica\ML-Email-Filter\test data\separat subiect continut\subjects"
content_output_path = r"D:\Universitate\ML\tema practica\ML-Email-Filter\test data\separat subiect continut\content"

# Procesează folderele și salvează subiectele și conținutul
process_emails_folder(emails_folder_path, subjects_output_path, content_output_path)
