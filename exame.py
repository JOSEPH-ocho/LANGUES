# Fonction traduire
def traduire():
    mot = zone_texte.get().lower()
    
    cursor.execute("SELECT anglais FROM dictionnaire WHERE francais=?", (mot,))
    resultat = cursor.fetchone()
    
    if resultat:
        label_resultat.config(text=resultat[0])
    else:
        label_resultat.config(text="Mot non trouvé")