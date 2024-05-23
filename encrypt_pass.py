import tkinter as tk
from tkinter import ttk
from add_login_screen import *

#
def add_login():
    add_login_window = tk.Toplevel()
    add_login_window.title("Add Login")
    add_login_window.iconbitmap("img/criptografia-de-dados.ico")
    add_login_window.geometry("300x200")

    #
    label_email = tk.Label(add_login_window, text="Email:")
    label_email.pack()
    entry_email = tk.Entry(add_login_window)
    entry_email.pack()

    #
    label_password = tk.Label(add_login_window, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(add_login_window, show="*")
    entry_password.pack()

    #
    label_site = tk.Label(add_login_window, text="Site:")
    label_site.pack()
    entry_site = tk.Entry(add_login_window)
    entry_site.pack()

    #
    def save_login():
        email = entry_email.get()
        password = entry_password.get()
        site = entry_site.get()

        print("Email: ", email)
        print("Password: ", password)
        print("Site: ", site)

        add_login_window.destroy()
    
    #
    btn_save = tk.Button(add_login_window, text="Save", command=save_login)
    btn_save.pack()

#
def delete_login():
    pass

#
encrypt_pass = tk.Tk()
encrypt_pass.title("Encrypt Pass")
encrypt_pass.iconbitmap("img/criptografia-de-dados.ico")

#
tree = ttk.Treeview(encrypt_pass)
tree["columns"] = ("email", "senha", "site")
tree.heading("#0", text="ID")
tree.heading("email", text="Email")
tree.heading("senha", text="Senha")
tree.heading("site", text="Site")
tree.pack()

#
btn_add = tk.Button(encrypt_pass, text="Add Login", command=add_login)
btn_add.pack(side=tk.LEFT)

#
btn_delete = tk.Button(encrypt_pass, text="Delete Login", command=delete_login)
btn_delete.pack(side=tk.LEFT)

encrypt_pass.mainloop()