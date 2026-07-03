# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Usuario, Treino, Exercicio, ItemTreino

app = Flask(__name__)
# Chave secreta obrigatória para gerenciar logins e sessões
app.secret_key = "chave_secreta_super_segura_flask" 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

DIAS_SEMANA = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
CATEGORIAS_TREINO = ["Peito", "Costas", "Pernas", "Panturrilha", "Posterior de Coxa", "Antebraço", "Bíceps", "Tríceps", "Ombro", "Abdômen", "Cardio"]

# ================================
# ROTAS DE AUTENTICAÇÃO
# ================================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email).first()
        
        # Verifica criptografia
        if usuario and check_password_hash(usuario.senha, senha):
            session['usuario_id'] = usuario.id_usuario
            session['usuario_nome'] = usuario.nome
            return redirect(url_for('dashboard'))
        else:
            flash("E-mail ou senha incorretos.")
            
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        if Usuario.query.filter_by(email=email).first():
            flash("E-mail já existe!")
            return redirect(url_for('register'))
            
        senha_cripto = generate_password_hash(senha)
        novo_user = Usuario(nome=nome, email=email, senha=senha_cripto)
        db.session.add(novo_user)
        db.session.commit()
        
        # Como é um projeto de teste, vamos dar um Treino de Presente automático para quem cria a conta
        novo_treino = Treino(nome="Treino de Adaptação (Perna)", dia_semana="Quinta-feira", categoria="Pernas", id_usuario=novo_user.id_usuario)
        db.session.add(novo_treino)
        db.session.commit()
        
        # Associa o agachamento a esse treino
        agachamento = Exercicio.query.filter_by(nome="Agachamento Livre").first()
        if agachamento:
            item = ItemTreino(id_treino=novo_treino.id_treino, id_exercicio=agachamento.id_exercicio, series=6, repeticoes=20, descanso_segundos=30)
            db.session.add(item)
            db.session.commit()

        flash("Conta criada! Faça o login.")
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ================================
# ROTAS DO SISTEMA (TREINOS)
# ================================
@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session: return redirect(url_for('login'))
    
    # Busca SÓ os treinos deste usuário logado
    treinos = Treino.query.filter_by(id_usuario=session['usuario_id']).all()

    # Agrupa os treinos por dia da semana, na ordem certa, pra ficar organizado
    treinos_por_dia = {dia: [] for dia in DIAS_SEMANA}
    outros = []  # treinos sem dia definido ou com valor fora da lista
    for t in treinos:
        if t.dia_semana in treinos_por_dia:
            treinos_por_dia[t.dia_semana].append(t)
        else:
            outros.append(t)

    return render_template(
        'dashboard.html',
        treinos_por_dia=treinos_por_dia,
        dias_semana=DIAS_SEMANA,
        outros=outros,
        nome=session['usuario_nome'],
        categorias=CATEGORIAS_TREINO
    )

# Cria um treino novo (dia + categoria) para o usuário logado
@app.route('/treino/novo', methods=['POST'])
def novo_treino():
    if 'usuario_id' not in session: return redirect(url_for('login'))

    dia_semana = request.form.get('dia_semana', '').strip()
    categoria = request.form.get('categoria', '').strip()
    nome = request.form.get('nome', '').strip() or categoria

    if nome and categoria:
        treino = Treino(nome=nome, dia_semana=dia_semana, categoria=categoria, id_usuario=session['usuario_id'])
        db.session.add(treino)
        db.session.commit()
        flash("Treino criado com sucesso!")
    else:
        flash("Escolha o dia e a categoria do treino.")

    return redirect(url_for('dashboard'))

@app.route('/treino/<int:id_treino>', methods=['GET', 'POST'])
def ver_treino(id_treino):
    if 'usuario_id' not in session: return redirect(url_for('login'))
    
    treino = Treino.query.get_or_404(id_treino)
    
    # Proteção: Se eu tentar ver o treino de outro aluno pela URL, sou bloqueado
    if treino.id_usuario != session['usuario_id']:
        return redirect(url_for('dashboard'))
        
    # Se ela preencheu o formulário de evoluir treino (aumentar série, etc)
    if request.method == 'POST':
        id_item = request.form.get('id_item')
        item = ItemTreino.query.get(id_item)
        if item:
            item.series = request.form.get('series')
            item.repeticoes = request.form.get('repeticoes')
            item.descanso_segundos = request.form.get('descanso')
            db.session.commit()
            flash("Evolução registrada com sucesso!")
            return redirect(url_for('ver_treino', id_treino=id_treino))
            
    return render_template(
        'treino.html',
        treino=treino,
        exercicios_da_categoria=Exercicio.query.filter_by(grupo_muscular=treino.categoria).order_by(Exercicio.nome).all(),
        exercicios=Exercicio.query.order_by(Exercicio.nome).all()
    )

# Adiciona um novo exercício dentro de um treino (cria o Exercicio se ainda não existir)
@app.route('/treino/<int:id_treino>/exercicio/adicionar', methods=['POST'])
def adicionar_exercicio(id_treino):
    if 'usuario_id' not in session: return redirect(url_for('login'))

    treino = Treino.query.get_or_404(id_treino)
    if treino.id_usuario != session['usuario_id']:
        return redirect(url_for('dashboard'))

    nome_exercicio = request.form.get('nome_exercicio', '').strip()
    grupo_muscular = request.form.get('grupo_muscular', '').strip() or treino.categoria
    series = request.form.get('series') or 3
    repeticoes = request.form.get('repeticoes') or 12
    descanso = request.form.get('descanso') or 30

    if nome_exercicio:
        # Reaproveita o exercício se já existir na biblioteca (mesmo nome), senão cria um novo
        exercicio = Exercicio.query.filter_by(nome=nome_exercicio).first()
        if not exercicio:
            exercicio = Exercicio(nome=nome_exercicio, grupo_muscular=grupo_muscular)
            db.session.add(exercicio)
            db.session.commit()

        item = ItemTreino(
            id_treino=treino.id_treino,
            id_exercicio=exercicio.id_exercicio,
            series=series,
            repeticoes=repeticoes,
            descanso_segundos=descanso
        )
        db.session.add(item)
        db.session.commit()
        flash("Exercício adicionado ao treino!")
    else:
        flash("Escolha ou digite o nome do exercício.")

    return redirect(url_for('ver_treino', id_treino=id_treino))

# Remove um exercício de dentro de um treino
@app.route('/treino/<int:id_treino>/exercicio/<int:id_item>/remover', methods=['POST'])
def remover_exercicio(id_treino, id_item):
    if 'usuario_id' not in session: return redirect(url_for('login'))

    treino = Treino.query.get_or_404(id_treino)
    if treino.id_usuario != session['usuario_id']:
        return redirect(url_for('dashboard'))

    item = ItemTreino.query.get_or_404(id_item)
    db.session.delete(item)
    db.session.commit()
    flash("Exercício removido do treino.")

    return redirect(url_for('ver_treino', id_treino=id_treino))

# ================================
# INICIALIZAÇÃO
# ================================
def iniciar_banco():
    # Cria uma biblioteca fixa de exercícios se estiver vazia
    if Exercicio.query.count() == 0:
        exs = [
            Exercicio(nome="Agachamento Livre", grupo_muscular="Pernas"),
            Exercicio(nome="Leg Press 45", grupo_muscular="Pernas"),
            Exercicio(nome="Supino Reto", grupo_muscular="Peito"),
            Exercicio(nome="Puxada Costas", grupo_muscular="Costas")
        ]
        db.session.bulk_save_objects(exs)
        db.session.commit()

with app.app_context():
    db.create_all()
    iniciar_banco()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
