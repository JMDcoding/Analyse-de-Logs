import xml.etree.ElementTree as ET

def ecrire_xml(fichier, donnees):
    root = ET.Element("Personnes")
    for personne in donnees:
        personne_element = ET.SubElement(root, "Personne")
        ET.SubElement(personne_element, "Nom").text = personne["nom"]
        ET.SubElement(personne_element, "Âge").text = str(personne["age"])
        ET.SubElement(personne_element, "Ville").text = personne["ville"]
    tree = ET.ElementTree(root)
    tree.write(fichier)

def lire_xml(fichier):
    tree = ET.parse(fichier)
    root = tree.getroot()
    for personne in root.findall("Personne"):
        nom = personne.find("Nom").text
        age = personne.find("Âge").text
        ville = personne.find("Ville").text
        print(f"Nom: {nom}, Âge: {age}, Ville: {ville}")

# Exemple d'utilisation
donnees = [{"nom": "Alice", "age": 25, "ville": "Paris"},
           {"nom": "Bob", "age": 30, "ville": "Lyon"}]
ecrire_xml("donnees.xml", donnees)
lire_xml("donnees.xml")
