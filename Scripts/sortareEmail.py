import os
import shutil

def sort_emails(source_folder, destination_folder_spam, destination_folder_non_spam):
    # Parcurgere recursivă a folderelor
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)

                # Verificare dacă numele fisierului contine 'spm'
                if 'spm' in file_name:
                    destination_path = os.path.join(destination_folder_spam, file_name)
                else:
                    destination_path = os.path.join(destination_folder_non_spam, file_name)

                # Copierea fisierului la destinatie
                shutil.copy(file_path, destination_path)

if __name__ == "__main__":
    # Specificațiile folderelor
    source_folder = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\lemm_stop'
    destination_folder_spam = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\Entire\spam'
    destination_folder_non_spam = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\Entire\non-spam'

    # Crearea folderelor de destinatie daca nu exista
    os.makedirs(destination_folder_spam, exist_ok=True)
    os.makedirs(destination_folder_non_spam, exist_ok=True)

    # Apelarea functiei pentru sortarea emailurilor
    sort_emails(source_folder, destination_folder_spam, destination_folder_non_spam)
