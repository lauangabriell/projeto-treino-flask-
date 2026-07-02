# app.py
import os
from flask import Flask, render_template
from models import db

app = Flask(__name__)

# O Render injeta a variável DATABASE_URL automaticamente aqui
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados conectado com o app
db.init_app(app)

@app.route('/')
def index():
    # Abre a interface de Calistenia e Pilates
    return render_template('index.html')

# Garante a criação de tabelas no banco de dados Neon no primeiro acesso
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
