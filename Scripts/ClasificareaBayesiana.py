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
    path_folder_content = "D:/Universitate/ML/tema practica/ML-Email-Filter/date pt testare/separat subiect continut/content"
    path_folder_subject = "D:/Universitate/ML/tema practica/ML-Email-Filter/date pt testare/separat subiect continut/subjects"
    path_folder_entire = "D:/Universitate/ML/tema practica/ML-Email-Filter/date pt testare/lemm_stop/part10"

    rezultate_spam_content = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\probabilitati\rezultate_content_spam.txt'
    rezultate_non_spam_content = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\probabilitati\rezultate_content_non_spam.txt'

    rezultate_spam_subject = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\probabilitati\rezultate_subject_spam.txt'
    rezultate_non_spam_subject = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\probabilitati\rezultate_subject_non_spam.txt'

    rezultate_entire_spam = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\probabilitati\rezultate_entire_spam.txt'
    rezultate_entire_non_spam = r'D:\Universitate\ML\tema practica\ML-Email-Filter\date pt antrenare\Sorted Emails\probabilitati\rezultate_entire_non_spam.txt'

    informatii_spam_content = citeste_informatii(rezultate_spam_content)
    informatii_non_spam_content = citeste_informatii(rezultate_non_spam_content)

    informatii_spam_subject = citeste_informatii(rezultate_spam_subject)
    informatii_non_spam_subject = citeste_informatii(rezultate_non_spam_subject)

    informatii_entire_spam = citeste_informatii(rezultate_entire_spam)
    informatii_entire_non_spam = citeste_informatii(rezultate_entire_non_spam)

    spam_files_content = []
    non_spam_files_content = []

    spam_files_subject = []
    non_spam_files_subject = []

    spam_files_entire = []
    non_spam_files_entire = []

    laplace_value_content = 0.0001
    laplace_value_subject = 0.0004
    laplace_value_entire = 0.0001

    # Iterează pentru content
    for cale_fisier in os.listdir(path_folder_content):
        if cale_fisier.endswith(".txt"):
            with open(os.path.join(path_folder_content, cale_fisier), "r", encoding="utf-8") as f:
                continut = f.read()
                if clasifica_email(continut, informatii_spam_content, informatii_non_spam_content,
                                   laplace_value_content):
                    spam_files_content.append(cale_fisier)
                else:
                    non_spam_files_content.append(cale_fisier)

    # Iterează pentru subject
    for cale_fisier in os.listdir(path_folder_subject):
        if cale_fisier.endswith(".txt"):
            with open(os.path.join(path_folder_subject, cale_fisier), "r", encoding="utf-8") as f:
                continut = f.read()
                if clasifica_email(continut, informatii_spam_subject, informatii_non_spam_subject,
                                   laplace_value_subject):
                    spam_files_subject.append(cale_fisier)
                else:
                    non_spam_files_subject.append(cale_fisier)

    # Iterează pentru entire
    for cale_fisier in os.listdir(path_folder_entire):
        if cale_fisier.endswith(".txt"):
            with open(os.path.join(path_folder_entire, cale_fisier), "r", encoding="utf-8") as f:
                continut = f.read()
                if clasifica_email(continut, informatii_entire_spam, informatii_entire_non_spam, laplace_value_entire):
                    spam_files_entire.append(cale_fisier)
                else:
                    non_spam_files_entire.append(cale_fisier)

    # Salvează rezultatele în fișiere
    output_folder = "D:/Universitate/ML/tema practica/ML-Email-Filter/date pt testare/rezultate bayes"

    with open(os.path.join(output_folder, "spam_files_content.txt"), "w", encoding="utf-8") as f_spam:
        f_spam.write("\n".join(spam_files_content))

    with open(os.path.join(output_folder, "non_spam_files_content.txt"), "w", encoding="utf-8") as f_non_spam:
        f_non_spam.write("\n".join(non_spam_files_content))

    with open(os.path.join(output_folder, "spam_files_subject.txt"), "w", encoding="utf-8") as f_spam:
        f_spam.write("\n".join(spam_files_subject))

    with open(os.path.join(output_folder, "non_spam_files_subject.txt"), "w", encoding="utf-8") as f_non_spam:
        f_non_spam.write("\n".join(non_spam_files_subject))

    with open(os.path.join(output_folder, "spam_files_entire.txt"), "w", encoding="utf-8") as f_spam:
        f_spam.write("\n".join(spam_files_entire))

    with open(os.path.join(output_folder, "non_spam_files_entire.txt"), "w", encoding="utf-8") as f_non_spam:
        f_non_spam.write("\n".join(non_spam_files_entire))


if __name__ == "__main__":
    main()
