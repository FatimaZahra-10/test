import tkinter as tk
import creer_projet  # Assurez-vous que creer_projet.py est dans le même répertoire ou dans le chemin accessible
import gestion_tache  # Importer gestion_tache.py
import test_auth  # Importer le fichier d'authentification pour la déconnexion

def gestion_projets():
    respo_window.withdraw()
    creer_projet.redirect_to_create_project(respo_window)

def suivi_avancement():
    # Code pour le suivi d'avancement
    pass

def gestion_taches():
    respo_window.withdraw()
    gestion_tache.main(respo_window)

def deconnexion():
    respo_window.withdraw()
    test_auth.main()

def main():
    global respo_window
    respo_window = tk.Tk()
    respo_window.title("Respo Interface")
    respo_window.geometry("400x400")
    respo_window.configure(bg="#2C3E50")

    label = tk.Label(respo_window, text="Welcome to the Respo Interface", font=("Helvetica", 16), bg="#2C3E50", fg="white")
    label.pack(pady=20)

    button_style = {
        'bg': "#16A085",
        'fg': "white",
        'relief': "flat",
        'width': 25,
        'height': 2,
        'font': ("Helvetica", 12)
    }

    projets_button = tk.Button(respo_window, text="Gestion des Projets", command=gestion_projets, **button_style)
    projets_button.pack(pady=10)

    suivi_button = tk.Button(respo_window, text="Suivi d'Avancement", command=suivi_avancement, **button_style)
    suivi_button.pack(pady=10)

    taches_button = tk.Button(respo_window, text="Gestion des Tâches", command=gestion_taches, **button_style)
    taches_button.pack(pady=10)

    deconnexion_button = tk.Button(respo_window, text="Déconnexion", command=deconnexion, **button_style)
    deconnexion_button.pack(pady=20)

    respo_window.mainloop()

if __name__ == "__main__":
    main()
