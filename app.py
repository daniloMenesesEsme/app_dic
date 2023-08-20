# Primeiro exmplo de como podemos usar para chamar a grid de Usuário e Senha:
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("DIC")

label_username = tk.Label(root, text="Usuário:")
label_password = tk.Label(root, text="Senha:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
button_login = tk.Button(root, text="Login")
label_username.grid(row=0, column=0)
label_password.grid(row=1, column=0)
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
button_login.grid(row=2, columnspan=2)
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "usuario" and password == "senha":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

button_login.config(command=login)
root.mainloop()

# Segundo exeplo para grid Login e Pass que podemos usar:

import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "usuario" and password == "senha":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

root = tk.Tk()
root.title("Tela de Login")

# Configuração de tamanho da janela
largura = 300
altura = 200
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

x = (largura_tela - largura) / 2
y = (altura_tela - altura) / 2
root.geometry(f"{largura}x{altura}+{int(x)}+{int(y)}")

label_username = tk.Label(root, text="Usuário:")
label_password = tk.Label(root, text="Senha:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
button_login = tk.Button(root, text="Login")

label_username.grid(row=0, column=0, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_login.grid(row=2, columnspan=2, padx=10, pady=20)

button_login.config(command=login)

root.mainloop()

