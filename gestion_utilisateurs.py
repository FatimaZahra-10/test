import tkinter as tk
from tkinter import messagebox
import sqlite3
import admin  # Assurez-vous que admin.py est dans le même répertoire ou dans le chemin accessible

def add_user():
    username = username_entry.get()
    password = password_entry.get()
    role = role_var.get()

    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    connection.commit()
    messagebox.showinfo("Success", "User added successfully!")
    refresh_user_list()

def edit_user():
    username = username_entry.get()
    password = password_entry.get()
    role = role_var.get()

    cursor.execute("UPDATE users SET password=?, role=? WHERE username=?", (password, role, username))
    connection.commit()
    messagebox.showinfo("Success", "User information updated successfully!")
    refresh_user_list()

def delete_user():
    username = username_entry.get()

    cursor.execute("DELETE FROM users WHERE username=?", (username,))
    connection.commit()
    messagebox.showinfo("Success", "User deleted successfully!")
    refresh_user_list()

def refresh_user_list():
    user_info_text.delete('1.0', tk.END)  # Clear the current text
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        user_info_text.insert(tk.END, "Username: {}\nPassword: {}\nRole: {}\n\n".format(user[1], user[2], user[3]))

def retour():
    root.destroy()
    admin.main()

def main():
    global root, username_entry, password_entry, role_var, user_info_text, connection, cursor

    root = tk.Tk()
    root.title("User Management")
    root.geometry("400x400")
    root.configure(bg="#2C3E50")

    frame = tk.Frame(root, bg="#34495E")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title_label = tk.Label(frame, text="User Management", font=("Helvetica", 24), bg="#34495E", fg="white")
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    username_label = tk.Label(frame, text="Username:", bg="#34495E", fg="white")
    username_label.grid(row=1, column=0, padx=(10, 0), pady=(0, 5))
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 5))

    password_label = tk.Label(frame, text="Password:", bg="#34495E", fg="white")
    password_label.grid(row=2, column=0, padx=(10, 0), pady=(0, 5))
    password_entry = tk.Entry(frame)
    password_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 5))

    role_label = tk.Label(frame, text="Role:", bg="#34495E", fg="white")
    role_label.grid(row=3, column=0, padx=(10, 0), pady=(0, 5))
    role_var = tk.StringVar(root)
    role_var.set("admin")  
    role_options = ["admin", "responsable", "employe"]
    role_menu = tk.OptionMenu(frame, role_var, *role_options)
    role_menu.grid(row=3, column=1, padx=(0, 10), pady=(0, 5))

    add_button = tk.Button(frame, text="Add User", command=add_user, bg="#16A085", fg="white", relief="flat")
    add_button.grid(row=4, column=0, pady=(10, 10), padx=(10, 10), sticky="nesw")

    edit_button = tk.Button(frame, text="Edit User", command=edit_user, bg="#3498DB", fg="white", relief="flat")
    edit_button.grid(row=4, column=1, pady=(10, 10), padx=(10, 10), sticky="nesw")

    delete_button = tk.Button(frame, text="Delete User", command=delete_user, bg="#E74C3C", fg="white", relief="flat")
    delete_button.grid(row=5, column=0, columnspan=2, pady=(10, 20), padx=(10, 10), sticky="nesw")

    user_info_text = tk.Text(frame, height=10, width=40)
    user_info_text.grid(row=6, column=0, columnspan=2, pady=(0, 10))

    retour_button = tk.Button(frame, text="Retour", command=retour, bg="#E74C3C", fg="white", relief="flat")
    retour_button.grid(row=7, column=0, columnspan=2, pady=(10, 20), padx=(10, 10), sticky="nesw")

    connection = sqlite3.connect("base_donnee.db")
    cursor = connection.cursor()

    refresh_user_list()
    root.mainloop()

if __name__ == "__main__":
    main()
