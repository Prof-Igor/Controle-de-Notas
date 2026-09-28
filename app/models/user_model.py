from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_connection

def authenticate_user(username, password):
    """Busca o usuário no SQLite e valida a senha."""
    query = "SELECT password_hash FROM usuarios WHERE username = ?"
    
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        
        if row:
            stored_hash = row[0]
            if check_password_hash(stored_hash, password):
                return True
    finally:
        # Garante que a conexão será fechada de forma segura
        conn.close()
        
    return False

def create_user(username, password):
    """Insere um novo usuário no SQLite com hash de senha."""
    hashed_password = generate_password_hash(password)
    
    check_query = "SELECT id FROM usuarios WHERE username = ?"
    insert_query = "INSERT INTO usuarios (username, password_hash) VALUES (?, ?)"
    
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        cursor.execute(check_query, (username,))
        if cursor.fetchone() is not None:
            return False # Usuário já existe
        
        cursor.execute(insert_query, (username, hashed_password))
        conn.commit()
        return True
    finally:
        conn.close()