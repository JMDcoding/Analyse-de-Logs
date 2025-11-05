import yaml

def ecrire_yaml(fichier, donnees):
    with open(fichier, 'w') as f:
        yaml.dump(donnees, f, default_flow_style=False)

def lire_yaml(fichier):
    with open(fichier, 'r') as f:
        return yaml.safe_load(f)

# Exemple d'utilisation
donnees = {"nom": "Alice", "age": 25, "ville": "Paris"}
ecrire_yaml("donnees.yaml", donnees)
print(lire_yaml("donnees.yaml"))
