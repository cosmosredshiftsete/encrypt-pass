import tkinter as tk
from tkinter import messagebox

#
def perform_login():
    username = entry_username.get()
    password = entry_password.get()
    encryption_password = entry_encryption_password.get()

    #
    if username == CORRECT_LOGIN and password == CORRECT_PASSWORD and encryption_password == CORRECT_ENCRYPTION_PASSWORD:
        messagebox.showinfo("Success", "Login Successful!")
    #
    else:
        messagebox.showerror("Error", "Incorrect username or password!")

#
def open_encrypt_pass_window():
    root.destroy()

#
CORRECT_LOGIN = "admin"
CORRECT_PASSWORD = "Nala00110111#"
CORRECT_ENCRYPTION_PASSWORD = "8181160"

#
root = tk.Tk()
root.title("Login Screen")
root.geometry("400x150")
root.iconbitmap("img/criptografia-de-dados.ico")

#
label_username = tk.Label(root, text="Username: ")
label_username.place(x=50, y=50)
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

#
label_password = tk.Label(root, text="Pass:")
label_password.place(x=50, y=100)
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

#
label_encryption_password = tk.Label(root, text="Encryption Pass")
label_encryption_password.place(x=50, y=150)
label_encryption_password.pack()
entry_encryption_password = tk.Entry(root, show="*")
entry_encryption_password.pack()

#
button_login = tk.Button(root, text="Login", command=perform_login)
button_login.place(x=150, y=200)
button_login.pack()

root.mainloop()