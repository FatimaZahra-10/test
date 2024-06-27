import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('gestion_projet.db')
c = conn.cursor()

# Fonction pour ajouter un utilisateur
def add_user():
    role = role_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    if role and username and password:
        try:
            c.execute('INSERT INTO users (role, username, password) VALUES (?, ?, ?)', (role, username, password))
            conn.commit()
            messagebox.showinfo("Success", "User added successfully")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
    else:
        messagebox.showerror("Error", "All fields are required")

# Fonction pour modifier un utilisateur
def modify_user():
    username = username_entry.get()
    new_role = role_entry.get()
    new_password = password_entry.get()
    
    if username and (new_role or new_password):
        if new_role:
            c.execute('UPDATE users SET role = ? WHERE username = ?', (new_role, username))
        if new_password:
            c.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
        conn.commit()
        if c.rowcount:
            messagebox.showinfo("Success", "User updated successfully")
        else:
            messagebox.showerror("Error", "User not found")
    else:
        messagebox.showerror("Error", "Username and at least one new value are required")

# Fonction pour supprimer un utilisateur
def delete_user():
    username = username_entry.get()
    
    if username:
        c.execute('DELETE FROM users WHERE username = ?', (username,))
        conn.commit()
        if c.rowcount:
            messagebox.showinfo("Success", "User deleted successfully")
        else:
            messagebox.showerror("Error", "User not found")
    else:
        messagebox.showerror("Error", "Username is required")

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Admin Panel")
root.geometry("600x400")
root.configure(bg="#2C3E50")

frame = tk.Frame(root, bg="#34495E")
frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(frame, text="Admin Panel", font=("Helvetica", 24), bg="#34495E", fg="white")
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 20))

role_label = tk.Label(frame, text="Role:", font=("Helvetica", 14), bg="#34495E", fg="white")
role_label.grid(row=1, column=0, padx=(20, 10), pady=(10, 10))
role_entry = tk.Entry(frame, font=("Helvetica", 14))
role_entry.grid(row=1, column=1, padx=(10, 20), pady=(10, 10))

username_label = tk.Label(frame, text="Username:", font=("Helvetica", 14), bg="#34495E", fg="white")
username_label.grid(row=2, column=0, padx=(20, 10), pady=(10, 10))
username_entry = tk.Entry(frame, font=("Helvetica", 14))
username_entry.grid(row=2, column=1, padx=(10, 20), pady=(10, 10))

password_label = tk.Label(frame, text="Password:", font=("Helvetica", 14), bg="#34495E", fg="white")
password_label.grid(row=3, column=0, padx=(20, 10), pady=(10, 10))
password_entry = tk.Entry(frame, show='*', font=("Helvetica", 14))
password_entry.grid(row=3, column=1, padx=(10, 20), pady=(10, 10))

add_button = tk.Button(frame, text="Add User", command=add_user, font=("Helvetica", 14), bg="#16A085", fg="white", relief="flat")
add_button.grid(row=4, column=0, pady=(20, 10), padx=(20, 10), sticky="nesw")

modify_button = tk.Button(frame, text="Modify User", command=modify_user, font=("Helvetica", 14), bg="#2980B9", fg="white", relief="flat")
modify_button.grid(row=4, column=1, pady=(20, 10), padx=(20, 10), sticky="nesw")

delete_button = tk.Button(frame, text="Delete User", command=delete_user, font=("Helvetica", 14), bg="#C0392B", fg="white", relief="flat")
delete_button.grid(row=5, column=0, columnspan=2, pady=(10, 20), padx=(20, 20), sticky="nesw")

# Fermer la connexion à la base de données lors de la fermeture de l'application
def on_closing():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
