import tkinter as tk
from tkinter import messagebox
import cpfValidation
import banco_usuarios
from utils import carregar_imagem  # Importa a função de carregar as imagens

class RegistrationInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro")
        self.root.geometry("380x500")
        self.root.resizable(False, False)
        self.bd = banco_usuarios.Banco()

        self.show_icon = carregar_imagem("eye.png").subsample(25)  #type: ignore
        self.hide_icon = carregar_imagem("hide.png").subsample(25)  #type: ignore

        # Alternar visibilidade da senha
        def show_hide_password(entry, button):
            if entry['show'] == '':
                button.config(image=self.hide_icon)
                entry.config(show='•')
            else:
                button.config(image=self.show_icon)
                entry.config(show='')

        def open_login_interface():
            self.root.destroy()
            import login_interface
            login_interface.LoginInterface()

        # Frame principal
        self.frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        
        self.label_title = tk.Label(self.frame, text="Cadastro", font=('Arial', 16, "bold"), bg="white")
        self.label_title.pack(pady=10)

        
        self.label_name = tk.Label(self.frame, text="Nome:", font=("Arial", 12), bg="white")
        self.label_name.pack(anchor="w")
        self.entry_name = tk.Entry(self.frame, font=("Arial", 12), width=30, relief="solid", bd=1)
        self.entry_name.pack(pady=5)

        
        self.label_password = tk.Label(self.frame, text="Senha:", font=("Arial", 12), bg="white")
        self.label_password.pack(anchor="w")

        self.password_frame = tk.Frame(self.frame, bg="white")
        self.password_frame.pack()

        self.entry_password = tk.Entry(self.password_frame, font=("Arial", 12), width=27, relief="solid", bd=1, show="•")
        self.entry_password.pack(side="left", pady=5)

        self.btn_show_password = tk.Button(self.password_frame, image=self.hide_icon, bd=0, bg="white",
                                           command=lambda: show_hide_password(self.entry_password, self.btn_show_password))
        self.btn_show_password.pack(side="left", padx=5)

        
        self.label_confirm_password = tk.Label(self.frame, text="Confirmar Senha:", font=("Arial", 12), bg="white")
        self.label_confirm_password.pack(anchor="w")

        self.confirm_password_frame = tk.Frame(self.frame, bg="white")
        self.confirm_password_frame.pack()

        self.entry_confirm_password = tk.Entry(self.confirm_password_frame, font=("Arial", 12), width=27, relief="solid", bd=1, show="•")
        self.entry_confirm_password.pack(side="left", pady=5)

        self.btn_show_password_confirm = tk.Button(self.confirm_password_frame, image=self.hide_icon, bd=0, bg="white",
                                                   command=lambda: show_hide_password(self.entry_confirm_password, self.btn_show_password_confirm))
        self.btn_show_password_confirm.pack(side="left", padx=5)

        # Campo CPF
        self.label_cpf = tk.Label(self.frame, text="CPF:", font=("Arial", 12), bg="white")
        self.label_cpf.pack(anchor="w")
        self.entry_cpf = tk.Entry(self.frame, font=("Arial", 12), width=30, relief="solid", bd=1)
        self.entry_cpf.pack(pady=5)
        self.entry_cpf.bind("<KeyRelease>", lambda event: cpfValidation.apply_cpf_mask(event, self.entry_cpf))

        # Mensagem de CPF inválido
        self.label_invalid_cpf = tk.Label(self.frame, text="", font=("Arial", 10), fg="red", bg="white")
        self.label_invalid_cpf.pack(pady=2)

        # Botão Registrar
        self.btn_register = tk.Button(self.frame, text="Registrar", font=('Arial', 12, "bold"),
                                      bg='#158aff', fg='white', width=25, height=2, relief="raised",
                                      command=self.add_user)
        self.btn_register.pack(pady=10)

        # Botão Voltar para Login (estilo link)
        self.btn_back = tk.Button(self.frame, text="Voltar para login", font=('Arial', 10),
                                  fg='#158aff', bg="white", relief="flat", command=open_login_interface)
        self.btn_back.pack()

        self.root.mainloop()

    def get_input_entry(self):
        return (self.entry_cpf.get(), self.entry_name.get(),
                self.entry_password.get(), self.entry_confirm_password.get())

    def add_user(self):
        cpf, name, password, password_confirmed = self.get_input_entry()

        if not all([cpf, name, password, password_confirmed]):
            messagebox.showwarning("Entrada inválida", "Preencha todos os campos.")
            return
        
        if password != password_confirmed:
            messagebox.showerror("Erro", "As senhas não coincidem. Por favor, verifique e tente novamente.")
            return

        if not cpfValidation.cpf_validation(self.entry_cpf, self.label_invalid_cpf):
            self.label_invalid_cpf.config(text="CPF inválido!", foreground="red")
            return

        self.label_invalid_cpf.config(text="")

        if self.bd.check_existence_cpf(cpf):
            messagebox.showwarning("Usuário já existe", "Já existe um usuário com esse CPF cadastrado.")
            return

        self.bd.add_user(cpf, name, password)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
