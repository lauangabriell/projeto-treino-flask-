# app.py
import os
from flask import Flask, render_template, request, jsonify
from models import db, Usuario, Treino, Exercicio

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

# 1. ROTA PARA SALVAR UM TREINO E SEUS EXERCÍCIOS PARA O USUÁRIO
@app.route('/api/treino/salvar', methods=['POST'])
def salvar_treino():
    dados = request.get_json()
    
    # Busca o Usuário 1 ou cria um padrão para o teste funcionar de primeira
    usuario = Usuario.query.get(1)
    if not usuario:
        usuario = Usuario(
            nome="Lauan Gabriel", 
            email="lauan@treino.com", 
            senha="123",
            idade=20,
            sexo="Masculino",
            altura=175.0,
            peso=70.0,
            objetivo="Ganho de Massa",
            nivel_experiencia="Intermediário"
        )
        db.session.add(usuario)
        db.session.commit()

    # Cria o novo Treino
    novo_treino = Treino(
        nivel_dificuldade=dados.get('nivel'),
        objetivo_alvo=dados.get('objetivo').capitalize(),
        duracao_estimada=int(dados.get('duracao', 30))
    )
    
    # Adiciona cada exercício enviado no treino
    for ex_nome in dados.get('exercicios', []):
        # Cria o exercício associando o grupo muscular
        exercicio = Exercicio(
            nome=ex_nome,
            grupo_muscular=dados.get('objetivo'),
            equipamento_necessario="Nenhum / Peso Corporal"
        )
        novo_treino.exercicios.append(exercicio)
    
    # Associa o treino criado ao usuário
    usuario.treinos.append(novo_treino)
    
    db.session.add(novo_treino)
    db.session.commit()
    
    return jsonify({"status": "sucesso", "message": f"Treino de {novo_treino.objetivo_alvo} salvo para {usuario.nome}!"})

# 2. ROTA PARA BUSCAR OS TREINOS SALVOS DO USUÁRIO NO NEON
@app.route('/api/treinos/salvos', methods=['GET'])
def listar_treinos():
    usuario = Usuario.query.get(1)
    if not usuario:
        return jsonify([])
        
    historico = []
    for t in usuario.treinos:
        historico.append({
            "id_treino": t.id_treino,
            "nivel": t.nivel_dificuldade,
            "objetivo": t.objetivo_alvo,
            "duracao": t.duracao_estimada,
            "exercicios": [e.nome for e in t.exercicios]
        })
    return jsonify(historico)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
