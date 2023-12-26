import os


def citeste_fisiere_clasificate(cale_fisier):
    with open(cale_fisier, "r", encoding="utf-8") as f:
        return [linie.strip() for linie in f]


def elimina_sufix(fisier, sufix):
    if fisier.endswith(sufix):
        return fisier[:-len(sufix)]
    return fisier


def clasifica_final(fisiere_subject_spam, fisiere_subject_non_spam, fisiere_content_spam, fisiere_content_non_spam):
    spam_final = set()
    non_spam_final = set()
    nesigur = set()

    for fisier in fisiere_subject_spam:
        nume_fisier = elimina_sufix(fisier, "_subject.txt")
        if fisier in fisiere_content_spam:
            spam_final.add(nume_fisier)
        else:
            nesigur.add(nume_fisier)

    for fisier in fisiere_subject_non_spam:
        nume_fisier = elimina_sufix(fisier, "_subject.txt")
        if fisier in fisiere_content_non_spam:
            non_spam_final.add(nume_fisier)
        else:
            nesigur.add(nume_fisier)

    for fisier in fisiere_content_spam:
        nume_fisier = elimina_sufix(fisier, "_content.txt")
        if nume_fisier not in spam_final and nume_fisier not in non_spam_final:
            spam_final.add(nume_fisier)

    for fisier in fisiere_content_non_spam:
        nume_fisier = elimina_sufix(fisier, "_content.txt")
        if nume_fisier not in spam_final and nume_fisier not in non_spam_final:
            non_spam_final.add(nume_fisier)

    return spam_final, non_spam_final, nesigur


def scrie_in_fisier(cale_fisier, continut):
    with open(cale_fisier, "w", encoding="utf-8") as f:
        for linie in continut:
            f.write(f"{linie}\n")


def main():
    path_rezultate = "/Sorted Emails/rezultate bayes"

    fisiere_subject_spam = citeste_fisiere_clasificate(os.path.join(path_rezultate, "spam_files_subject.txt"))
    fisiere_subject_non_spam = citeste_fisiere_clasificate(os.path.join(path_rezultate, "non_spam_files_subject.txt"))
    fisiere_content_spam = citeste_fisiere_clasificate(os.path.join(path_rezultate, "spam_files_content.txt"))
    fisiere_content_non_spam = citeste_fisiere_clasificate(os.path.join(path_rezultate, "non_spam_files_content.txt"))

    spam_final, non_spam_final, nesigur = clasifica_final(
        fisiere_subject_spam, fisiere_subject_non_spam, fisiere_content_spam, fisiere_content_non_spam
    )

    # Scrie rezultatele în fișiere separate
    scrie_in_fisier(os.path.join(path_rezultate, "spam_final.txt"), spam_final)
    scrie_in_fisier(os.path.join(path_rezultate, "non_spam_final.txt"), non_spam_final)
    scrie_in_fisier(os.path.join(path_rezultate, "nesigur.txt"), nesigur)


if __name__ == "__main__":
    main()
