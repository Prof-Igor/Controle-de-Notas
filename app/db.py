import sqlite3
import os

# Pega o caminho absoluto da pasta raiz (Controle-de-Notas-main)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'banco_notas.db')

def get_connection():
    """Retorna uma nova conexão ativa com o banco SQLite."""
    return sqlite3.connect(DB_PATH)