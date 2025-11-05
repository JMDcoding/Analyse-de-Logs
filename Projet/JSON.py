import json

def ecrire_json(fichier, donnees):
    with open(fichier, 'w') as f:
        json.dump(donnees, f, indent=4)

def lire_json(fichier):
    with open(fichier, 'r') as f:
        return json.load(f)

# Exemple d'utilisation
donnees = {"nom": "Alice", "age": 25, "ville": "Paris"}
ecrire_json("donnees.json", donnees)
print(lire_json("donnees.json"))