import os
import shutil

def sort_emails(folder_path):
    new_folders_path = ''
    spam_folder = os.path.join(new_folders_path, 'spam')
    non_spam_folder = os.path.join(new_folders_path, 'non-spam')

    # Creează folderele 'spam' și 'non-spam' dacă nu există deja
    if not os.path.exists(spam_folder):
        os.makedirs(spam_folder)
    if not os.path.exists(non_spam_folder):
        os.makedirs(non_spam_folder)

    # Parcurge fiecare fisier din folderul radacina
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Verifică dacă numele fisierului incepe cu 'spm' pentru a identifica spam-ul
            if file.startswith('spm'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(spam_folder, file)
                shutil.copy(source_path, destination_path)
                print(f"Spam file '{file}' moved to '{spam_folder}'")
            else:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(non_spam_folder, file)
                shutil.copy(source_path, destination_path)
                print(f"Non-spam file '{file}' moved to '{non_spam_folder}'")

if __name__ == "__main__":
    # Înlocuiește calea de mai jos cu calea către folderul tău radacină
    root_folder_path = r'../emails'
    sort_emails(root_folder_path)
