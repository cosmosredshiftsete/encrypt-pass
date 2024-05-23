import tkinter as tk
from encrypt_pass import *

def make_login():
    pass

# 
root = tk.Tk()
root.title("Login")
root.geometry("400x200")
root.iconbitmap("img/criptografia-de-dados.ico")

# 
label_login = tk.Label(root, text="Login: ")
label_login.place(x=50, y=50)  
entry_login = tk.Entry(root)
entry_login.place(x=100, y=50)  

label_pass = tk.Label(root, text="Password: ")
label_pass.place(x=50, y=100)  
entry_pass = tk.Entry(root, show="*")
entry_pass.place(x=100, y=100)  

button_login = tk.Button(root, text="Login", command=make_login)
button_login.place(x=150, y=150)  
root.mainloop()