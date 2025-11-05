import csv

def ecrire_csv(fichier, donnees):
    with open(fichier, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Nom", "Âge", "Ville"])
        writer.writerows(donnees)

def lire_csv(fichier):
    with open(fichier, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# Exemple d'utilisation
donnees = [["Alice", 25, "Paris"], ["Bob", 30, "Lyon"]]
ecrire_csv("donnees.csv", donnees)
lire_csv("donnees.csv")