import sqlite3

class Backend:
    @staticmethod
    def initDB():
        conexao = sqlite3.connect("nomes.db")
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)
        conexao.commit()
        conexao.close()

    @staticmethod
    def salvar_nome(nome):
        conexao = sqlite3.connect("nomes.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO pessoas (nome) VALUES (?)", (nome,))
        conexao.commit()
        conexao.close()
        
# Importa o módulo sqlite3 para manipular banco de dados SQLite
import sqlite3

# Função para conectar e criar banco de dados caso não exista
def conectar():
    # Cria conexão com o banco chamado 'clientes.db'
    conn = sqlite3.connect("clientes.db")
    # Retorna o objeto de conexão
    return conn
