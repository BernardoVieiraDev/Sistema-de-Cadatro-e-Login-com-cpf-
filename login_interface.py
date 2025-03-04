import tkinter as tk
from tkinter import messagebox
import home_interface
import banco_usuarios
import registration_interface
from utils import carregar_imagem  # Importe a função de carregar as imagens

class LoginInterface:
    def __init__(self): 
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("380x400")
        self.root.resizable(False, False)
        self.bd = banco_usuarios.Banco()

        # Carregar e redimensionar imagens para os botões de mostrar/esconder senha
        self.show_icon = carregar_imagem("eye.png").subsample(25)  #type: ignore
        self.hide_icon = carregar_imagem("hide.png").subsample(25)      #type: ignore

        # Alternar visibilidade da senha
        def show_hide_password():
            if self.entry_password['show'] == '':
                self.btn_show_hide.config(image=self.hide_icon)
                self.entry_password.config(show='•')
            else:
                self.btn_show_hide.config(image=self.show_icon)
                self.entry_password.config(show='')

        def open_register_interface():
            self.root.destroy()
            registration_interface.RegistrationInterface()

        # Frame principal
        self.frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        self.label_title = tk.Label(self.frame, text="Login", font=('Arial', 16, "bold"), bg="white")
        self.label_title.pack(pady=10)

        # Campo Nome
        self.label_name = tk.Label(self.frame, text="Nome:", font=("Arial", 12), bg="white")
        self.label_name.pack(anchor="w")
        self.entry_name = tk.Entry(self.frame, font=("Arial", 12), width=30, relief="solid", bd=1)
        self.entry_name.pack(pady=5)

        # Campo Senha
        self.label_password = tk.Label(self.frame, text="Senha:", font=("Arial", 12), bg="white")
        self.label_password.pack(anchor="w")

        self.password_frame = tk.Frame(self.frame, bg="white")
        self.password_frame.pack()

        self.entry_password = tk.Entry(self.password_frame, font=("Arial", 12), width=30, relief="solid", bd=1, show="•")
        self.entry_password.pack(side="left", pady=5)

        self.btn_show_hide = tk.Button(self.password_frame, image=self.hide_icon, bd=0, bg="white",
                                       command=show_hide_password)
        self.btn_show_hide.pack(side="left", padx=5)

        # Botão de login
        self.btn_login = tk.Button(self.frame, text="Login", font=('Arial', 12, "bold"),
                                   bg='#158aff', fg='white', width=25, height=2, relief="raised",
                                   command=self.login)
        self.btn_login.pack(pady=10)

        # Botão "Cadastre-se" estilo link
        self.btn_register_page_link = tk.Button(self.frame, text="Cadastre-se", font=('Arial', 10),
                                                fg='#158aff', bg="white", relief="flat",
                                                command=open_register_interface)
        self.btn_register_page_link.pack()

        self.root.mainloop()

    def get_input_entry(self):
        return self.entry_name.get(), self.entry_password.get()

    def login(self):
        name, password = self.get_input_entry()
        if not all([name, password]):
            messagebox.showwarning("Entrada inválida", "Preencha todos os campos.")
            return

        if not self.bd.check_login(name, password):
            messagebox.showerror("Erro", "Usuário ou senha incorretos ou não existem.")
            return 
        
        self.root.destroy()
        home_interface.HomeInterface(name)
