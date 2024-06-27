import tkinter as tk
from tkinter import messagebox
import creer_projet  # Assurez-vous que creer_projet.py est dans le même répertoire ou dans le chemin accessible

def gestion_projet():
    # Fermer la fenêtre admin avant d'ouvrir l'interface de création de projet
    admin_window.destroy()
    creer_projet.main()  # Appelle la fonction principale de creer_projet

def gestion_utilisateurs():
    # Code pour la gestion des utilisateurs
    messagebox.showinfo("Gestion des Utilisateurs", "Gestion des utilisateurs est en cours de développement.")

def main():
    global admin_window
    admin_window = tk.Tk()
    admin_window.title("Admin Interface")
    admin_window.geometry("500x400")
    admin_window.configure(bg="#2C3E50")

    label = tk.Label(admin_window, text="Welcome to the Admin Interface", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="white")
    label.pack(pady=30)

    button_style = {
        'bg': "#16A085",
        'fg': "white",
        'relief': "flat",
        'width': 25,
        'height': 3,
        'font': ("Helvetica", 14)
    }

    projet_button = tk.Button(admin_window, text="Gestion de Projet", command=gestion_projet, **button_style)
    projet_button.pack(pady=15)

    utilisateurs_button = tk.Button(admin_window, text="Gestion des Utilisateurs", command=gestion_utilisateurs, **button_style)
    utilisateurs_button.pack(pady=15)

    admin_window.mainloop()

if __name__ == "__main__":
    main()
