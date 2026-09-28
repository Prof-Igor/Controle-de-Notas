from app.db import get_connection
from app.models.user_model import create_user

def inicializar_banco():
    # 1. Conecta e cria a tabela
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()
    print("Banco de dados e tabelas validados com sucesso!")

    # 2. Insere o utilizador de exemplo
    print("A configurar utilizador de exemplo...")
    sucesso = create_user("prof.igor", "SenhaSegura123")
    
    if sucesso:
        print("-> Utilizador 'prof.igor' criado com sucesso! Pode fazer o login.")
    else:
        print("-> O utilizador 'prof.igor' já existe no banco de dados.")

if __name__ == '__main__':
    inicializar_banco()