from flask import Flask

# Usando o '.' para indicar que controllers estão dentro do mesmo pacote (app)
from .controllers import auth_bp, main_bp

# Corrigido para 'views' conforme a pasta no seu VS Code
app = Flask(__name__, template_folder='views')

# Chave secreta obrigatória para assinar criptograficamente os cookies
app.secret_key = 'substitua_por_uma_chave_longa_e_aleatoria_em_producao'

# Registro dos Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

# O app.run não fica mais aqui!