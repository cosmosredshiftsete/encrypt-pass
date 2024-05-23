import tkinter as tk
from tkinter import ttk

#
def add_login():
    pass

#
def delete_login():
    pass

#
encrypt_pass = tk.Tk()
encrypt_pass.title("Encrypt Pass")

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