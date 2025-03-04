import tkinter as tk
from tkinter import messagebox
import login_interface

class HomeInterface:
    def __init__(self, name):  
        self.root = tk.Tk()
        self.root.title("Home")
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        # Frame principal
        self.frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        self.label_title = tk.Label(self.frame, text="Home", font=('Arial', 18, "bold"), bg="white")
        self.label_title.pack(pady=10)

        # Mensagem de boas-vindas
        self.label_name = tk.Label(self.frame, text=f"Bem-vindo, {name}!", font=('Arial', 14), bg="white")
        self.label_name.pack(pady=10)

        # Botão de voltar ao login
        self.btn_back = tk.Button(self.frame, text="Voltar para Login", font=("Arial", 12, "bold"),
                                  bg="#158aff", fg="white", width=20, height=2, relief="raised",
                                  command=self.open_login_interface)
        self.btn_back.pack(pady=15)

        self.root.mainloop()

    def open_login_interface(self):
        self.root.destroy()
        login_interface.LoginInterface()
