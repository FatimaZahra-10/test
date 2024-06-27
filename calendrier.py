import tkinter as tk
from tkcalendar import Calendar
from datetime import date
import gestion_tache  # Importer le fichier gestion_tache.py

class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendrier")
        self.master.geometry("600x400")
        self.master.configure(bg="#2C3E50")

        self.calendar = Calendar(self.master, selectmode="day", year=date.today().year, month=date.today().month, day=date.today().day)
        self.calendar.pack(pady=10)

        self.add_task_button = tk.Button(self.master, text="Ajouter Tâche", command=self.add_task, bg="#16A085", fg="white", relief="flat")
        self.add_task_button.pack(pady=10)

        self.tasks = {}

    def add_task(self):
        selected_date = self.calendar.selection_get()  # Utilisez selection_get() pour obtenir la date sélectionnée
        # Ouvrir l'interface gestion_tache.py
        gestion_tache.main()

def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
