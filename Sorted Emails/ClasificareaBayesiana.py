import os


def citeste_informatii(fisier):
    informatii = {}
    with open(fisier, "r", encoding="utf-8") as f:
        for linie in f:
            cuvant, aparitii, probabilitate = linie.strip().split(", ")
            informatii[cuvant] = float(probabilitate)
    return informatii


def calculeaza_probabilitate_aparitie(cuvant, informatii, laplace_value):
    if cuvant in informatii:
        return informatii[cuvant]
    else:
        return laplace_value


def clasifica_email(continut, informatii_spam, informatii_non_spam, laplace_value):
    probabilitate_spam = 0.1660261337
    probabilitate_non_spam = 0.8339738663

    cuvinte = continut.split()
    for cuvant in cuvinte:
        probabilitate_spam *= calculeaza_probabilitate_aparitie(cuvant, informatii_spam, laplace_value)
        probabilitate_non_spam *= calculeaza_probabilitate_aparitie(cuvant, informatii_non_spam, laplace_value)

    return probabilitate_spam > probabilitate_non_spam


def main():
    path_folder_content = "D:/Universitate/ML/tema practica/ML-Email-Filter/test data/separat subiect continut/content"
    path_folder_subject = "D:/Universitate/ML/tema practica/ML-Email-Filter/test data/separat subiect continut/subjects"

    rezultate_spam_content = "D:/Universitate/ML/tema practica/ML-Email-Filter/Sorted Emails/probabilitati/rezultate_content_spam.txt"
    rezultate_non_spam_content = "D:/Universitate/ML/tema practica/ML-Email-Filter/Sorted Emails/probabilitati/rezultate_content_non_spam.txt"

    rezultate_spam_subject = "D:/Universitate/ML/tema practica/ML-Email-Filter/Sorted Emails/probabilitati/rezultate_subject_spam.txt"
    rezultate_non_spam_subject = "D:/Universitate/ML/tema practica/ML-Email-Filter/Sorted Emails/probabilitati/rezultate_subject_non_spam.txt"

    informatii_spam_content = citeste_informatii(rezultate_spam_content)
    informatii_non_spam_content = citeste_informatii(rezultate_non_spam_content)

    informatii_spam_subject = citeste_informatii(rezultate_spam_subject)
    informatii_non_spam_subject = citeste_informatii(rezultate_non_spam_subject)

    spam_files_content = []
    non_spam_files_content = []

    spam_files_subject = []
    non_spam_files_subject = []

    laplace_value_content = 0.0001
    laplace_value_subject = 0.0004

    # Iterează pentru content
    for folder_radacina, _, fisiere in os.walk(path_folder_content):
        for fisier in fisiere:
            if fisier.endswith(".txt"):
                cale_fisier = os.path.join(folder_radacina, fisier)
                with open(cale_fisier, "r", encoding="utf-8") as f:
                    continut = f.read()
                    if clasifica_email(continut, informatii_spam_content, informatii_non_spam_content,
                                       laplace_value_content):
                        spam_files_content.append(fisier)
                    else:
                        non_spam_files_content.append(fisier)

    # Iterează pentru subject
    for folder_radacina, _, fisiere in os.walk(path_folder_subject):
        for fisier in fisiere:
            if fisier.endswith(".txt"):
                cale_fisier = os.path.join(folder_radacina, fisier)
                with open(cale_fisier, "r", encoding="utf-8") as f:
                    continut = f.read()
                    if clasifica_email(continut, informatii_spam_subject, informatii_non_spam_subject,
                                       laplace_value_subject):
                        spam_files_subject.append(fisier)
                    else:
                        non_spam_files_subject.append(fisier)

    # Salvează rezultatele în fișiere
    with open("D:/Universitate/ML/tema practica/ML-Email-Filter/Sorted Emails/rezultate bayes/spam_files_content.txt",
              "w", encoding="utf-8") as f_spam:
        f_spam.write("\n".join(spam_files_content))

    with open(
            "D:/Universitate/ML/tema practica/ML-Email-Filter/Sorted Emails/rezultate bayes/non_spam_files_content.txt",
            "w", encoding="utf-8") as f_non_spam:
        f_non_spam.write("\n".join(non_spam_files_content))

    with open("D:/Universitate/ML/tema practica/ML-Email-Filter/Sorted Emails/rezultate bayes/spam_files_subject.txt",
              "w", encoding="utf-8") as f_spam:
        f_spam.write("\n".join(spam_files_subject))

    with open(
            "D:/Universitate/ML/tema practica/ML-Email-Filter/Sorted Emails/rezultate bayes/non_spam_files_subject.txt",
            "w", encoding="utf-8") as f_non_spam:
        f_non_spam.write("\n".join(non_spam_files_subject))


if __name__ == "__main__":
    main()
