from flask import Blueprint, render_template, session
from ..utils import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/welcome')
@login_required # <-- Middleware bloqueando acesso anônimo
def welcome():
    return render_template('main/dashboard.html', username=session.get('user_id'))