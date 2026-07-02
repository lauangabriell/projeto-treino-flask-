# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tabela de Associação: Relação "Realiza" (Usuário <-> Treino)
usuario_treino = db.Table('usuario_treino',
    db.Column('id_usuario', db.Integer, db.ForeignKey('usuario.id_usuario'), primary_key=True),
    db.Column('id_treino', db.Integer, db.ForeignKey('treino.id_treino'), primary_key=True)
)

# Tabela de Associação: Relação "Contém" (Treino <-> Exercício)
treino_exercicio = db.Table('treino_exercicio',
    db.Column('id_treino', db.Integer, db.ForeignKey('treino.id_treino'), primary_key=True),
    db.Column('id_exercicio', db.Integer, db.ForeignKey('exercicio.id_exercicio'), primary_key=True)
)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(20))
    altura = db.Column(db.Float)
    peso = db.Column(db.Float)
    objetivo = db.Column(db.String(100))
    nivel_experiencia = db.Column(db.String(50))
    
    # Relacionamento muitos para muitos com Treino
    treinos = db.relationship('Treino', secondary=usuario_treino, backref=db.backref('usuarios', lazy=True))

class Treino(db.Model):
    __tablename__ = 'treino'
    id_treino = db.Column(db.Integer, primary_key=True)
    nivel_dificuldade = db.Column(db.String(50))
    objetivo_alvo = db.Column(db.String(100))
    duracao_estimada = db.Column(db.Integer)
    
    # Relacionamento muitos para muitos com Exercicio
    exercicios = db.relationship('Exercicio', secondary=treino_exercicio, backref=db.backref('treinos', lazy=True))

class Exercicio(db.Model):
    __tablename__ = 'exercicio'
    id_exercicio = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    grupo_muscular = db.Column(db.String(50))
    equipamento_necessario = db.Column(db.String(100))
