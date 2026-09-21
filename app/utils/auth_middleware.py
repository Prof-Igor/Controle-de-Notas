from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Verifica se existe uma sessão válida ativa
        if 'user_id' not in session:
            flash("Por favor, faça o login para acessar esta página.")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function