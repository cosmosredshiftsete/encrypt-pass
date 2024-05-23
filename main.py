import tkinter as tk

def fazer_login():
    # Aqui você pode verificar se o login e a senha estão corretos
    # Se estiverem corretos, você pode chamar a função para abrir a próxima tela
    pass

# Criando a janela principal
root = tk.Tk()
root.title("Login")
root.geometry("400x200")
root.iconbitmap("img/criptografia-de-dados.png")  # Definindo as dimensões da janela

# Criando os widgets
label_login = tk.Label(root, text="Login:")
label_login.place(x=50, y=50)  # Posicionando o widget na janela
entry_login = tk.Entry(root)
entry_login.place(x=100, y=50)  # Posicionando o widget na janela

label_senha = tk.Label(root, text="Senha:")
label_senha.place(x=50, y=100)  # Posicionando o widget na janela
entry_senha = tk.Entry(root, show="*")
entry_senha.place(x=100, y=100)  # Posicionando o widget na janela

button_login = tk.Button(root, text="Login", command=fazer_login)
button_login.place(x=150, y=150)  # Posicionando o widget na janela

root.mainloop()