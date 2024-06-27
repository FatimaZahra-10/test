import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
import sys
import creer_projet  # Assurez-vous que ce module existe
import employe  # Assurez-vous que ce module existe
import respo  # Assurez-vous que ce module existe

# Connexion à la base de données SQLite (elle sera créée si elle n'existe pas)
conn = sqlite3.connect('gestion_projet.db')
c = conn.cursor()

# Création de la table users si elle n'existe pas déjà
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    role TEXT,
    username TEXT UNIQUE,
    password TEXT
)
''')

# Insertion des données initiales dans la table
c.executemany('''
INSERT OR IGNORE INTO users (role, username, password) VALUES (?, ?, ?)
''', [
    ('admin', 'admin@gmail.com', 'admin'),
    ('respo', 'respo@gmail.com', 'respo'),
    ('employe', 'employe@gmail.com', 'employe'),
    ('admin', 'fati@gmail.com', 'fati')
])

# Validation des changements dans la base de données
conn.commit()

# Fonction pour déterminer le rôle de l'utilisateur
def get_role(username):
    c.execute('SELECT role FROM users WHERE username=?', (username,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        return None

# Fonction pour ouvrir l'interface admin
def open_admin_interface():
    subprocess.Popen([sys.executable, "admin.py"])

# Fonction pour ouvrir l'interface respo
def open_respo_interface():
    respo.main()

# Fonction pour ouvrir l'interface employe
def open_employe_interface():
    employe.main()

# Fonction de redirection vers l'interface appropriée en fonction du rôle
def redirect_interface(username):
    role = get_role(username)
    if role == "admin":
        open_admin_interface()
    elif role == "respo":
        open_respo_interface()
    elif role == "employe":
        open_employe_interface()
    else:
        messagebox.showerror("Error", "Unknown role")

# Fonction de connexion
def login():
    username = username_entry.get()
    password = password_entry.get()
    c.execute('SELECT password FROM users WHERE username=?', (username,))
    result = c.fetchone()

    if result and result[0] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        # Redirection vers l'interface appropriée
        redirect_interface(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Project Management App")
root.geometry("800x600")  # Agrandir la taille de la fenêtre
root.configure(bg="#2C3E50")

frame = tk.Frame(root, bg="#34495E")
frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(frame, text="Login", font=("Helvetica", 32), bg="#34495E", fg="white")
title_label.grid(row=0, column=0, columnspan=2, pady=(40, 20))

username_label = tk.Label(frame, text="Username:", font=("Helvetica", 16), bg="#34495E", fg="white")
username_label.grid(row=1, column=0, padx=(20, 10), pady=(10, 10))
username_entry = tk.Entry(frame, font=("Helvetica", 16))
username_entry.grid(row=1, column=1, padx=(10, 20), pady=(10, 10))

password_label = tk.Label(frame, text="Password:", font=("Helvetica", 16), bg="#34495E", fg="white")
password_label.grid(row=2, column=0, padx=(20, 10), pady=(10, 10))
password_entry = tk.Entry(frame, show='*', font=("Helvetica", 16))
password_entry.grid(row=2, column=1, padx=(10, 20), pady=(10, 10))

login_button = tk.Button(frame, text="Login", command=login, font=("Helvetica", 16), bg="#16A085", fg="white", relief="flat")
login_button.grid(row=3, column=0, columnspan=2, pady=(20, 20), padx=(20, 20), sticky="nesw")

# Fermer la connexion à la base de données lors de la fermeture de l'application
def on_closing():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
