from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ..models import authenticate_user

# Blueprint para rotas de autenticação
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Se o usuário já estiver logado, redireciona para a tela de bem-vindo
    if 'user_id' in session:
        return redirect(url_for('main.welcome'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if authenticate_user(username, password):
            # Cria a sessão de forma segura
            session.clear() # Limpa sessões antigas para evitar "Session Fixation"
            session['user_id'] = username
            return redirect(url_for('main.welcome'))
        else:
            flash('Usuário ou senha inválidos.')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))