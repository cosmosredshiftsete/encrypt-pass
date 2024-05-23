import tkinter as tk
from tkinter import ttk
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('logins.db')
c = conn.cursor()

# Criar tabela para armazenar os logins se não existir
c.execute('''CREATE TABLE IF NOT EXISTS logins
             (email TEXT, senha TEXT, site TEXT)''')

# Função para adicionar um novo login ao banco de dados
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

        c.execute("INSERT INTO logins VALUES (?, ?, ?)", (email, password, site))
        conn.commit()
        add_login_window.destroy()
        update_login_view()

    #
    btn_save = tk.Button(add_login_window, text="Save", command=save_login)
    btn_save.pack()

# Função para excluir um login selecionado na Treeview e no banco de dados
def delete_login():
    selected_item = tree.selection()
    if selected_item:
        item_id = selected_item[0]
        idx = int(tree.item(item_id, "text")) - 1
        login_data = logins[idx]
        c.execute("DELETE FROM logins WHERE email = ? AND senha = ? AND site = ?", (login_data["email"], login_data["senha"], login_data["site"]))
        conn.commit()
        update_login_view()

# Função para carregar logins do banco de dados e atualizar a visualização
def load_logins_from_db():
    c.execute("SELECT * FROM logins")
    rows = c.fetchall()
    for row in rows:
        logins.append({"email": row[0], "senha": row[1], "site": row[2]})
    update_login_view()

# Função para atualizar a visualização dos logins na Treeview
def update_login_view():
    for record in tree.get_children():
        tree.delete(record)

    #
    for idx, login in enumerate(logins, start=1):
        email = login["email"]
        senha = login["senha"]
        site = login["site"]
        tree.insert("", "end", text=str(idx), values=(email, senha, site))

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

# Lista para armazenar os logins temporariamente
logins = []

# Carregar logins do banco de dados e atualizar a visualização
load_logins_from_db()

encrypt_pass.mainloop()

# Fechar a conexão com o banco de dados quando o programa terminar
conn.close()