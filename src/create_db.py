import sqlite3

def criar_banco_dados():
    conn = sqlite3.connect('dados_ambientais.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS dados_ambientais
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                       poluicao_ar REAL,
                       qualidade_agua REAL,
                       ruido_urbano REAL)''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_banco_dados()
    print("Banco de dados criado com sucesso!")
