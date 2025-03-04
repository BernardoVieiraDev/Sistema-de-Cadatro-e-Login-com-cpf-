import sqlite3
from tkinter import messagebox


class Banco:
    def __init__(self, db_name="user_registry"):
        self.db_name = db_name
        self.create_table()

    def execute_command(self, command, parameters=()):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(command, parameters)
                conn.commit()
                return cursor.fetchall()
        except sqlite3.DatabaseError as e:
            messagebox.showerror("Erro no Banco de Dados", f"Ocorreu um erro ao acessar banco de dados: {e}")
            return []
        except Exception as e:
            messagebox.showerror("Um erro inesperado aconteceu", f"Detalhes do erro: {e}")
            return []
        
    def create_table(self):
        self.execute_command('''CREATE TABLE IF NOT EXISTS users (
                         id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         name TEXT NOT NULL, 
                         password TEXT NOT NULL, 
                         cpf TEXT NOT NULL
                         )''')
    
    def check_existence_cpf(self, cpf):
        query = self.execute_command("SELECT COUNT(*) FROM users WHERE cpf = ?", ( cpf,))
        count = query[0][0] if query else 0
        return count > 0
    
    def check_login(self, name, password):
        query = self.execute_command("SELECT COUNT(*) FROM users WHERE name = ? AND password = ?", ( name, password,))
        count = query[0][0] if query else 0
        return count > 0


    def add_user(self, cpf, name, password):
        self.execute_command("INSERT INTO users (cpf, name, password) VALUES (?,?,?)",
                             (cpf, name, password))




 