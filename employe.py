import tkinter as tk
from tkinter import messagebox
import calendrier  # Importez le module calendrier

def consultation_calendriers():
    # Ouvrir l'interface calendrier
    calendrier.main()

def gestion_taches():
    # Code pour la gestion des tâches
    messagebox.showinfo("Gestion des Tâches", "Gestion des tâches est en cours de développement.")

def soumission_rapports():
    # Code pour la soumission de rapports
    messagebox.showinfo("Soumission de Rapports", "Soumission de rapports est en cours de développement.")

def main():
    employe_window = tk.Tk()
    employe_window.title("Employe Interface")
    employe_window.geometry("400x300")
    employe_window.configure(bg="#2C3E50")

    label = tk.Label(employe_window, text="Welcome to the Employe Interface", font=("Helvetica", 16), bg="#2C3E50", fg="white")
    label.pack(pady=20)

    calendriers_button = tk.Button(employe_window, text="Consultation des Calendriers", command=consultation_calendriers, bg="#16A085", fg="white", relief="flat", width=25)
    calendriers_button.pack(pady=10)

    taches_button = tk.Button(employe_window, text="Gestion des Tâches", command=gestion_taches, bg="#16A085", fg="white", relief="flat", width=25)
    taches_button.pack(pady=10)

    rapports_button = tk.Button(employe_window, text="Soumission de Rapports", command=soumission_rapports, bg="#16A085", fg="white", relief="flat", width=25)
    rapports_button.pack(pady=10)

    employe_window.mainloop()

if __name__ == "__main__":
    main()
