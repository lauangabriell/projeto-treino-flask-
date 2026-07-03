# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False) # Guardaremos a senha criptografada
    
    # Relação: 1 Usuário possui N Treinos
    treinos = db.relationship('Treino', backref='usuario', lazy=True)

class Treino(db.Model):
    __tablename__ = 'treino'
    id_treino = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False) # Ex: "Treino de Perna"
    dia_semana = db.Column(db.String(50)) # Ex: "Quinta-feira"
    categoria = db.Column(db.String(50)) # Ex: "Costas", "Peito", "Panturrilha"
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    
    # Relação: 1 Treino possui N Exercícios associados (ItemTreino)
    itens = db.relationship('ItemTreino', backref='treino', lazy=True, cascade="all, delete-orphan")

class Exercicio(db.Model):
    __tablename__ = 'exercicio'
    id_exercicio = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    grupo_muscular = db.Column(db.String(50))

class ItemTreino(db.Model):
    __tablename__ = 'item_treino'
    id_item = db.Column(db.Integer, primary_key=True)
    id_treino = db.Column(db.Integer, db.ForeignKey('treino.id_treino'), nullable=False)
    id_exercicio = db.Column(db.Integer, db.ForeignKey('exercicio.id_exercicio'), nullable=False)
    
    # Variáveis de evolução da Lana (Ex: 20x6 com 30s)
    series = db.Column(db.Integer, default=3)
    repeticoes = db.Column(db.Integer, default=12)
    descanso_segundos = db.Column(db.Integer, default=30)
    
    # Facilita o acesso aos dados do exercício no HTML
    exercicio = db.relationship('Exercicio')
