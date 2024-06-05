import platform
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# SETTINGS
CORRECT_LOGIN = "admin" # u can change the login if u want!
CORRECT_PASSWORD = "Nala00110111#" # u can change the passwd if u want!
CORRECT_ENCRYPTION_PASSWORD = "8181160" # u can change the enc. passwd if u want!

# DATABASE
connection = sqlite3.connect("logins.db")
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS logins (email TEXT, senha TEXT, site TEXT)"""
)


def set_screen_icon(screen: tk.Tk | tk.Toplevel):
    """Configura o ícone correto de acordo com o sistema operacional."""
    os = platform.system()
    if os == "Windows":
        return screen.iconbitmap("img/criptografia-de-dados.ico")
    elif os == "Linux":
        return screen.iconbitmap("@img/criptografia-de-dados.xbm")
    else:
        return None


def perform_login():
    username = entry_username.get()
    password = entry_auth_password.get()
    encryption_password = entry_encryption_password.get()

    if (
        username == CORRECT_LOGIN
        and password == CORRECT_PASSWORD
        and encryption_password == CORRECT_ENCRYPTION_PASSWORD
    ):
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()  # if login have a been successful, close the login
        main_screen()  # open the main window
    else:
        messagebox.showerror("Error", "Incorrect username or password!")


def main_screen():
    encrypt_pass = tk.Tk()
    encrypt_pass.title("Encrypt Pass")
    set_screen_icon(encrypt_pass)

    global tree, logins

    passwords_frame = tk.Frame(encrypt_pass)
    passwords_frame.pack()

    tree = ttk.Treeview(passwords_frame)
    tree["columns"] = ("email", "senha", "site")
    tree.heading("#0", text="ID")
    tree.heading("email", text="Email")
    tree.heading("senha", text="Senha")
    tree.heading("site", text="Site")
    tree.pack()

    btn_add = tk.Button(passwords_frame, text="Add Login", command=add_login)
    btn_add.pack(side=tk.LEFT)

    btn_delete = tk.Button(passwords_frame, text="Delete Login", command=delete_login)
    btn_delete.pack(side=tk.LEFT)

    logins = []

    load_logins_from_db()
    encrypt_pass.mainloop()

    connection.close()


def add_login():
    add_login_window = tk.Toplevel()
    add_login_window.title("Add Login")
    set_screen_icon(add_login_window)
    add_login_window.geometry("300x200")

    label_email = tk.Label(add_login_window, text="Email:")
    label_email.pack()
    entry_email = tk.Entry(add_login_window)
    entry_email.pack()

    label_password = tk.Label(add_login_window, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(add_login_window, show="*")
    entry_password.pack()

    label_site = tk.Label(add_login_window, text="Site:")
    label_site.pack()
    entry_site = tk.Entry(add_login_window)
    entry_site.pack()

    def save_login():
        email = entry_email.get()
        password = entry_password.get()
        site = entry_site.get()

        cursor.execute("INSERT INTO logins VALUES (?, ?, ?)", (email, password, site))
        connection.commit()
        add_login_window.destroy()
        update_login_view()

    btn_save = tk.Button(add_login_window, text="Save", command=save_login)
    btn_save.pack()


def delete_login():
    selected_item = tree.selection()
    if selected_item:
        item_id = selected_item[0]
        idx = int(tree.item(item_id, "text")) - 1
        login_data = logins[idx]
        cursor.execute(
            "DELETE FROM logins WHERE email = ? AND senha = ? AND site = ?",
            (login_data["email"], login_data["senha"], login_data["site"]),
        )
        connection.commit()
        update_login_view()


def load_logins_from_db():
    cursor.execute("SELECT * FROM logins")
    rows = cursor.fetchall()
    for row in rows:
        logins.append({"email": row[0], "senha": row[1], "site": row[2]})
    update_login_view()


def update_login_view():
    for record in tree.get_children():
        tree.delete(record)

    for idx, login in enumerate(logins, start=1):
        email = login["email"]
        senha = login["senha"]
        site = login["site"]
        tree.insert("", "end", text=str(idx), values=(email, senha, site))


if __name__ == "__main__":
    # WINDOW
    root = tk.Tk()
    root.title("Login Screen")
    root.geometry("400x190")
    set_screen_icon(root)

    label_username = tk.Label(root, text="Username: ")
    label_username.place(x=50, y=50)
    label_username.pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    label_auth_password = tk.Label(root, text="Pass:")
    label_auth_password.place(x=50, y=100)
    label_auth_password.pack()
    entry_auth_password = tk.Entry(root, show="*")
    entry_auth_password.pack()

    label_encryption_password = tk.Label(root, text="Encryption Pass")
    label_encryption_password.place(x=50, y=150)
    label_encryption_password.pack()
    entry_encryption_password = tk.Entry(root, show="*")
    entry_encryption_password.pack()

    button_login = tk.Button(root, text="Login", command=perform_login)
    button_login.place(x=150, y=200)
    button_login.pack(pady=10)

    root.mainloop()