import tkinter as tk

def create_project():
    # Ici, vous pouvez ajouter le code pour récupérer les valeurs des widgets et enregistrer les informations du projet dans la base de données
    pass

def retour(root):
    root.destroy()
    import respo  # Assurez-vous que respo.py est dans le même répertoire ou dans le chemin accessible
    respo.main()

def redirect_to_create_project(root):
    root.destroy()
    create_project_window = tk.Tk()
    create_project_window.title("Create Project")
    create_project_window.geometry("400x500")

    frame = tk.Frame(create_project_window, bg="#34495E")
    frame.pack(fill=tk.BOTH, expand=True)

    title_label = tk.Label(frame, text="Create Project", font=("Helvetica", 24), bg="#34495E", fg="white")
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    start_date_label = tk.Label(frame, text="Start Date:", bg="#34495E", fg="white")
    start_date_label.grid(row=1, column=0, padx=(10, 0), pady=(0, 5))
    start_date_entry = tk.Entry(frame)
    start_date_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 5))

    project_name_label = tk.Label(frame, text="Project Name:", bg="#34495E", fg="white")
    project_name_label.grid(row=2, column=0, padx=(10, 0), pady=(0, 5))
    project_name_entry = tk.Entry(frame)
    project_name_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 5))

    end_date_label = tk.Label(frame, text="End Date:", bg="#34495E", fg="white")
    end_date_label.grid(row=3, column=0, padx=(10, 0), pady=(0, 5))
    end_date_entry = tk.Entry(frame)
    end_date_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 5))

    users_involved_label = tk.Label(frame, text="Users Involved:", bg="#34495E", fg="white")
    users_involved_label.grid(row=4, column=0, padx=(10, 0), pady=(0, 5))
    users_involved_entry = tk.Entry(frame)
    users_involved_entry.grid(row=4, column=1, padx=(0, 10), pady=(0, 5))

    num_tasks_label = tk.Label(frame, text="Number of Tasks:", bg="#34495E", fg="white")
    num_tasks_label.grid(row=5, column=0, padx=(10, 0), pady=(0, 5))
    num_tasks_entry = tk.Entry(frame)
    num_tasks_entry.grid(row=5, column=1, padx=(0, 10), pady=(0, 5))

    task_names_label = tk.Label(frame, text="Task Names:", bg="#34495E", fg="white")
    task_names_label.grid(row=6, column=0, padx=(10, 0), pady=(0, 5))
    task_names_entry = tk.Text(frame, height=5, width=30)
    task_names_entry.grid(row=6, column=1, padx=(0, 10), pady=(0, 5))

    create_button = tk.Button(frame, text="Create Project", command=create_project, bg="#16A085", fg="white", relief="flat")
    create_button.grid(row=7, column=0, columnspan=2, pady=(10, 10), padx=(10, 10), sticky="nesw")

    retour_button = tk.Button(frame, text="Retour", command=lambda: retour(create_project_window), bg="#E74C3C", fg="white", relief="flat")
    retour_button.grid(row=8, column=0, columnspan=2, pady=(10, 20), padx=(10, 10))

    create_project_window.mainloop()
