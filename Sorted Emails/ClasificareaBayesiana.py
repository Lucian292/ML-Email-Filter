import os

def citeste_informatii(fisier):
    informatii = {}
    with open(fisier, "r", encoding="utf-8") as f:
        for linie in f:
            cuvant, aparitii, probabilitate = linie.strip().split(", ")
            informatii[cuvant] = float(probabilitate)
    return informatii

def calculeaza_probabilitate_aparitie(cuvant, informatii):
    if cuvant in informatii:
        return informatii[cuvant]
    else:
        return 0.0001  # valoare returnata pentru regula Laplace

def clasifica_email(continut, informatii_spam, informatii_non_spam):
    probabilitate_spam = 0.1660261337
    probabilitate_non_spam = 0.8339738663

    cuvinte = continut.split()
    for cuvant in cuvinte:
        probabilitate_spam *= calculeaza_probabilitate_aparitie(cuvant, informatii_spam)
        probabilitate_non_spam *= calculeaza_probabilitate_aparitie(cuvant, informatii_non_spam)

    return probabilitate_spam > probabilitate_non_spam

def main():
    path_folder = "../test data/lemm_stop"
    rezultate_spam = "rezultate_spam.txt"
    rezultate_non_spam = "rezultate_non_spam.txt"

    informatii_spam = citeste_informatii(rezultate_spam)
    informatii_non_spam = citeste_informatii(rezultate_non_spam)

    spam_files = []
    non_spam_files = []

    for folder_radacina, _, fisiere in os.walk(path_folder):
        for fisier in fisiere:
            if fisier.endswith(".txt"):
                cale_fisier = os.path.join(folder_radacina, fisier)
                with open(cale_fisier, "r", encoding="utf-8") as f:
                    continut = f.read()
                    if clasifica_email(continut, informatii_spam, informatii_non_spam):
                        spam_files.append(fisier)
                    else:
                        non_spam_files.append(fisier)

    with open("spam_files.txt", "w", encoding="utf-8") as f_spam:
        f_spam.write("\n".join(spam_files))

    with open("non_spam_files.txt", "w", encoding="utf-8") as f_non_spam:
        f_non_spam.write("\n".join(non_spam_files))

if __name__ == "__main__":
    main()
