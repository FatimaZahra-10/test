import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Tâches")
        self.root.geometry("400x400")
        self.root.configure(bg="#2C3E50")

        self.tasks = []

        self.frame = tk.Frame(self.root, bg="#34495E")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.frame, text="Gestion des Tâches", font=("Helvetica", 24), bg="#34495E", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        self.name_label = tk.Label(self.frame, text="Nom de la Tâche:", bg="#34495E", fg="white")
        self.name_label.grid(row=1, column=0, padx=(10, 0), pady=(0, 5))
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 5))

        self.description_label = tk.Label(self.frame, text="Description:", bg="#34495E", fg="white")
        self.description_label.grid(row=2, column=0, padx=(10, 0), pady=(0, 5))
        self.description_entry = tk.Entry(self.frame)
        self.description_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 5))

        self.date_label = tk.Label(self.frame, text="Date:", bg="#34495E", fg="white")
        self.date_label.grid(row=3, column=0, padx=(10, 0), pady=(0, 5))
        self.date_entry = tk.Entry(self.frame)
        self.date_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 5))

        self.user_label = tk.Label(self.frame, text="Utilisateur:", bg="#34495E", fg="white")
        self.user_label.grid(row=4, column=0, padx=(10, 0), pady=(0, 5))
        self.user_entry = tk.Entry(self.frame)
        self.user_entry.grid(row=4, column=1, padx=(0, 10), pady=(0, 5))

        self.create_button = tk.Button(self.frame, text="Créer Tâche", command=self.create_task, bg="#16A085", fg="white", relief="flat")
        self.create_button.grid(row=5, column=0, columnspan=2, pady=(10, 10), padx=(10, 10), sticky="nesw")

        self.task_listbox = tk.Listbox(self.frame)
        self.task_listbox.grid(row=6, column=0, columnspan=2, pady=(0, 10), padx=(10, 10), sticky="nesw")

        self.delete_button = tk.Button(self.frame, text="Supprimer Tâche", command=self.delete_task, bg="#E74C3C", fg="white", relief="flat")
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=(10, 20), padx=(10, 10), sticky="nesw")

        self.populate_task_list()

    def populate_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task["name"])

    def create_task(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()
        user = self.user_entry.get()

        if name and description and date and user:
            task = {"name": name, "description": description, "date": date, "user": user}
            self.tasks.append(task)
            self.populate_task_list()
            messagebox.showinfo("Success", "Tâche créée avec succès!")
        else:
            messagebox.showerror("Error", "Veuillez remplir tous les champs.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.populate_task_list()
            messagebox.showinfo("Success", "Tâche supprimée avec succès!")
        else:
            messagebox.showerror("Error", "Veuillez sélectionner une tâche à supprimer.")

def main():
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
