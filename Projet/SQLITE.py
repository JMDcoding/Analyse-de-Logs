import sqlite3

def creer_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY, 
        nom TEXT, 
        age INTEGER, 
        ville TEXT
    )""")
    conn.commit()
    conn.close()

def inserer_donnees():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO utilisateurs (nom, age, ville) VALUES (?, ?, ?)",
                       [("Alice", 25, "Paris"), ("Bob", 30, "Lyon")])
    conn.commit()
    conn.close()

def lire_donnees():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utilisateurs")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# Exemple d'utilisation
creer_table()
inserer_donnees()
lire_donnees()
