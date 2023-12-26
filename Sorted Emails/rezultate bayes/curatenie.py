def eliminate_duplicate_words(file_path):
    # Deschide fișierul în modul de citire
    with open(file_path, 'r') as file:
        # Citeste conținutul fișierului
        content = file.read()

        # Împarte conținutul în cuvinte
        words = content.split()

        # Elimină cuvintele duplicate
        unique_words = list(set(words))

    # Deschide fișierul în modul de scriere
    with open(file_path, 'w') as file:
        # Scrie cuvintele unice înapoi în fișier
        file.write('\n'.join(unique_words))

# Specifică calea către fișierul text
file_path = 'non_spam_final.txt'

# Apelul funcției pentru eliminarea cuvintelor duplicate
eliminate_duplicate_words(file_path)
