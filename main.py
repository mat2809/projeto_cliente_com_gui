import tkinter as tk
from Gui import Gui
from Backend import Backend

def main():
    Backend.initDB()
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
   
    # Importa o módulo sqlite3 para manipular banco de dados SQLite
import sqlite3

# Função para conectar e criar banco de dados caso não exista
def conectar():
    # Cria conexão com o banco chamado 'clientes.db'
    conn = sqlite3.connect("clientes.db")
    # Retorna o objeto de conexão
    return conn
