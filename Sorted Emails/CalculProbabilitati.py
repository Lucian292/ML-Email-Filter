import os
from collections import Counter


def calculeaza_probabilitate(aparitii, total_cuvinte):
    return round(aparitii / total_cuvinte, 10)


def probabilitate_subject_non_spam():
    # Specifica calea către folderul cu fișierele txt
    cale_folder = "bySubject/non-spam"

    total_cuvinte = 0
    cuvinte_distincte = set()
    aparitii_cuvinte = Counter()

    # Iterează prin toate folderele și fișierele txt
    for folder_radacina, subfoldere, fisiere in os.walk(cale_folder):
        for fisier in fisiere:
            if fisier.endswith(".txt"):
                cale_fisier = os.path.join(folder_radacina, fisier)
                with open(cale_fisier, "r", encoding="utf-8") as f:
                    continut = f.read()
                    cuvinte = continut.split()
                    total_cuvinte += len(cuvinte)
                    cuvinte_distincte.update(set(cuvinte))
                    aparitii_cuvinte.update(cuvinte)

        # Calculează probabilitățile și scrie în fișierul de output
    with open("probabilitati/rezultate_subject_non_spam.txt", "w", encoding="utf-8") as output:
        for cuvant, aparitii in aparitii_cuvinte.items():
            probabilitate = calculeaza_probabilitate(aparitii, total_cuvinte)
            # Formatare cu precizie de 5 zecimale
            output.write(f"{cuvant}, {aparitii}, {probabilitate:.10f}\n")
            

def probabilitate_content_spam():
    # Specifica calea către folderul cu fișierele txt
    cale_folder = "byContent/spam"

    total_cuvinte = 0
    cuvinte_distincte = set()
    aparitii_cuvinte = Counter()

    # Iterează prin toate folderele și fișierele txt
    for folder_radacina, subfoldere, fisiere in os.walk(cale_folder):
        for fisier in fisiere:
            if fisier.endswith(".txt"):
                cale_fisier = os.path.join(folder_radacina, fisier)
                with open(cale_fisier, "r", encoding="utf-8") as f:
                    continut = f.read()
                    cuvinte = continut.split()
                    total_cuvinte += len(cuvinte)
                    cuvinte_distincte.update(set(cuvinte))
                    aparitii_cuvinte.update(cuvinte)

        # Calculează probabilitățile și scrie în fișierul de output
    with open("probabilitati/rezultate_content_spam.txt", "w", encoding="utf-8") as output:
        for cuvant, aparitii in aparitii_cuvinte.items():
            probabilitate = calculeaza_probabilitate(aparitii, total_cuvinte)
            # Formatare cu precizie de 5 zecimale
            output.write(f"{cuvant}, {aparitii}, {probabilitate:.10f}\n")
            
            
def probabilitate_content_non_spam():
    # Specifica calea către folderul cu fișierele txt
    cale_folder = "byContent/non-spam"

    total_cuvinte = 0
    cuvinte_distincte = set()
    aparitii_cuvinte = Counter()

    # Iterează prin toate folderele și fișierele txt
    for folder_radacina, subfoldere, fisiere in os.walk(cale_folder):
        for fisier in fisiere:
            if fisier.endswith(".txt"):
                cale_fisier = os.path.join(folder_radacina, fisier)
                with open(cale_fisier, "r", encoding="utf-8") as f:
                    continut = f.read()
                    cuvinte = continut.split()
                    total_cuvinte += len(cuvinte)
                    cuvinte_distincte.update(set(cuvinte))
                    aparitii_cuvinte.update(cuvinte)

        # Calculează probabilitățile și scrie în fișierul de output
    with open("probabilitati/rezultate_content_non_spam.txt", "w", encoding="utf-8") as output:
        for cuvant, aparitii in aparitii_cuvinte.items():
            probabilitate = calculeaza_probabilitate(aparitii, total_cuvinte)
            # Formatare cu precizie de 5 zecimale
            output.write(f"{cuvant}, {aparitii}, {probabilitate:.10f}\n")
            
            
def probabilitate_subject_spam():
    # Specifica calea către folderul cu fișierele txt
    cale_folder = "bySubject/spam"

    total_cuvinte = 0
    cuvinte_distincte = set()
    aparitii_cuvinte = Counter()

    # Iterează prin toate folderele și fișierele txt
    for folder_radacina, subfoldere, fisiere in os.walk(cale_folder):
        for fisier in fisiere:
            if fisier.endswith(".txt"):
                cale_fisier = os.path.join(folder_radacina, fisier)
                with open(cale_fisier, "r", encoding="utf-8") as f:
                    continut = f.read()
                    cuvinte = continut.split()
                    total_cuvinte += len(cuvinte)
                    cuvinte_distincte.update(set(cuvinte))
                    aparitii_cuvinte.update(cuvinte)

        # Calculează probabilitățile și scrie în fișierul de output
    with open("probabilitati/rezultate_subject_spam.txt", "w", encoding="utf-8") as output:
        for cuvant, aparitii in aparitii_cuvinte.items():
            probabilitate = calculeaza_probabilitate(aparitii, total_cuvinte)
            # Formatare cu precizie de 5 zecimale
            output.write(f"{cuvant}, {aparitii}, {probabilitate:.10f}\n")

if __name__ == "__main__":
    probabilitate_subject_spam()
    probabilitate_subject_non_spam()
    probabilitate_content_spam()
    probabilitate_content_non_spam()
