from werkzeug.security import generate_password_hash, check_password_hash

# Simulando um banco de dados em memória
USERS = {
    # Usuário: 'professor', Senha: 'senha_segura'
    "professor": generate_password_hash("senha_segura")
}

def authenticate_user(username, password):
    """Verifica se o usuário existe e se a senha está correta."""
    user_hash = USERS.get(username)
    if user_hash and check_password_hash(user_hash, password):
        return True
    return False