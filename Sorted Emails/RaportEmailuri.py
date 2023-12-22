import os


def numara_fisiere(path):
    try:
        numar_fisiere = len(os.listdir(path))
        return numar_fisiere
    except FileNotFoundError:
        print(f"Path-ul '{path}' nu există.")
        return 0


def calculeaza_rapoarte(path1, path2):
    numar_fisiere_path1 = numara_fisiere(path1)
    numar_fisiere_path2 = numara_fisiere(path2)
    numar_total_fisiere = numar_fisiere_path1 + numar_fisiere_path2

    raport_path1 = numar_fisiere_path1 / numar_total_fisiere if numar_total_fisiere != 0 else 0
    raport_path2 = numar_fisiere_path2 / numar_total_fisiere if numar_total_fisiere != 0 else 0

    return numar_fisiere_path1, numar_fisiere_path2, raport_path1, raport_path2


def main():
    path1 = "spam"
    path2 = "non-spam"

    numar_fisiere_path1, numar_fisiere_path2, raport_path1, raport_path2 = calculeaza_rapoarte(path1, path2)

    print(f"Numarul de fisiere din {path1}: {numar_fisiere_path1}")
    print(f"Numarul de fisiere din {path2}: {numar_fisiere_path2}")
    print(f"Raportul numarului de fisiere din {path1} la numarul total de fisiere: {raport_path1:.6f}")
    print(f"Raportul numarului de fisiere din {path2} la numarul total de fisiere: {raport_path2:.6f}")


if __name__ == "__main__":
    main()
