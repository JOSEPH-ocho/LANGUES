import sqlite3



# 1. Connexion à la base de données (crée le fichier s'il n'existe pas)
connexion = sqlite3.connect('langues.db')
curseur = connexion.cursor()

# 2. Création de la table avec deux colonnes : anglais et francais
curseur.execute('''
    CREATE TABLE IF NOT EXISTS vocabulaire (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        anglais TEXT NOT NULL,
        francais TEXT NOT NULL
    )
''')

# 3. La liste des 50 mots (2 colonnes)
mots_a_ajouter = [
    ('Hello', 'Bonjour'), ('Goodbye', 'Au revoir'), ('Please', 'S\'il vous plaît'),
    ('Thank you', 'Merci'), ('Yes', 'Oui'), ('No', 'Non'), ('Friend', 'Ami'),
    ('Family', 'Famille'), ('Home', 'Maison'), ('School', 'École'),
    ('Work', 'Travail'), ('Water', 'Eau'), ('Food', 'Nourriture'),
    ('Bread', 'Pain'), ('Time', 'Temps'), ('Day', 'Jour'), ('Night', 'Nuit'),
    ('Today', 'Aujourd\'hui'), ('Tomorrow', 'Demain'), ('Yesterday', 'Hier'),
    ('Man', 'Homme'), ('Woman', 'Femme'), ('Child', 'Enfant'), ('City', 'Ville'),
    ('Country', 'Pays'), ('Book', 'Livre'), ('Pen', 'Stylo'), ('Table', 'Table'),
    ('Chair', 'Chaise'), ('Window', 'Fenêtre'), ('Door', 'Porte'),
    ('Money', 'Argent'), ('Sun', 'Soleil'), ('Moon', 'Lune'), ('Sky', 'Ciel'),
    ('Tree', 'Arbre'), ('Flower', 'Fleur'), ('Car', 'Voiture'), ('Road', 'Route'),
    ('Small', 'Petit'), ('Big', 'Grand'), ('Good', 'Bon'), ('Bad', 'Mauvais'),
    ('Happy', 'Heureux'), ('Sad', 'Triste'), ('New', 'Nouveau'), ('Old', 'Vieux'),
    ('Life', 'Vie'), ('Love', 'Amour'), ('Help', 'Aide')
]

# 4. Insertion des 50 mots d'un coup
curseur.executemany('INSERT INTO vocabulaire (anglais, francais) VALUES (?, ?)', mots_a_ajouter)

# 5. Validation et fermeture
connexion.commit()
connexion.close()

print("Félicitations ! Les 50 mots ont été ajoutés à 'langues.db'.")