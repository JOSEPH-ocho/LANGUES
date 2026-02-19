import tkinter as tk
from tkinter import scrolledtext
from googletrans import Translator

# Configuration du traducteur
translator = Translator()

def traduire():
    texte = entree.get()
    if texte:
        try:
            # Traduction de Français vers Anglais
            resultat = translator.translate(texte, src='fr', dest='en')
            traduction = resultat.text
            
            # Affichage du résultat principal
            label_resultat.config(text=f"Traduction : {traduction}")
            
            # Ajout à l'historique (on l'ajoute au début de la liste)
            zone_historique.configure(state='normal') # On permet l'écriture
            zone_historique.insert(tk.INSERT, f"Fr: {texte} -> En: {traduction}\n")
            zone_historique.configure(state='disabled') # On verrouille pour ne pas effacer par erreur
            
            # Effacer la zone de saisie pour le mot suivant
            entree.delete(0, tk.END)
        except Exception as e:
            label_resultat.config(text="Erreur de connexion", fg="red")

# --- Interface Graphique ---
fenetre = tk.Tk()
fenetre.title("Mon Traducteur Pro")
fenetre.geometry("450x500")
fenetre.configure(bg="#2c3e50") # Couleur de fond Bleu Nuit

# Style du titre
tk.Label(fenetre, text="TRADUCTEUR FRANÇAIS -> ANGLAIS", 
         font=("Arial", 12, "bold"), fg="white", bg="#2c3e50").pack(pady=15)

# Zone de saisie
entree = tk.Entry(fenetre, font=("Arial", 12), width=30)
entree.pack(pady=10)

# Bouton Traduire avec de nouvelles couleurs
bouton_trad = tk.Button(fenetre, text="TRADUIRE MAINTENANT", command=traduire, 
                       bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                       padx=10, pady=5, cursor="hand2")
bouton_trad.pack(pady=10)

# Résultat principal
label_resultat = tk.Label(fenetre, text="", font=("Arial", 12, "italic"), 
                         fg="#f1c40f", bg="#2c3e50") # Texte en jaune clair
label_resultat.pack(pady=15)

# --- Section Historique ---
tk.Label(fenetre, text="Historique des traductions :", 
         font=("Arial", 10), fg="white", bg="#2c3e50").pack(pady=5)

zone_historique = scrolledtext.ScrolledText(fenetre, width=45, height=10, 
                                          font=("Arial", 9), state='disabled',
                                          bg="#ecf0f1") # Fond gris très clair
zone_historique.pack(pady=10)

fenetre.mainloop()# LANGUES
ce projet consiste a crée un traducteur de (une application capable de traduire les mots Français en anglais)
