🏋️ Sistema de Treinos

Aplicação web para criação e organização de treinos de academia. Cada usuário cria sua conta, cadastra seus dados físicos, monta treinos por dia da semana e categoria muscular, e acompanha exercícios com séries, repetições e tempo de descanso.

🔗 Acesse online: https://projeto-treino-flask.onrender.com


Funcionalidades


Cadastro e login com senha criptografada
Perfil com dados físicos e cálculo automático de IMC
Treinos organizados por dia da semana e grupo muscular
Biblioteca com 55 exercícios pré-cadastrados
Adição, edição e exclusão de treinos e exercícios



Tecnologias

Python · Flask · Flask-SQLAlchemy · PostgreSQL (Neon) · Jinja2 · Render


Como rodar localmente

bashgit clone https://github.com/lauangabriell/projeto-treino-flask.git
cd projeto-treino-flask
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

Acesse em http://localhost:5000. Sem a variável DATABASE_URL configurada, a aplicação usa SQLite local automaticamente.


Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/lauangabriell">
        <img src="https://github.com/lauangabriell.png" width="80" style="border-radius: 50%;" alt="Lauan Gabriel"/><br>
        <b>Lauan Gabriel Pereira Lima</b>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Lanabastos">
        <img src="https://github.com/Lanabastos.png" width="80" style="border-radius: 50%;" alt="Lanna Grazielle"/><br>
        <b>Lanna Grazielle Martins Bastos</b>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/RudysGalaxy">
        <img src="https://github.com/RudysGalaxy.png" width="80" style="border-radius: 50%;" alt="Francisco Ruda"/><br>
        <b>Francisco Ruda Gomes</b>
      </a>
    </td>
  </tr>
</table>

Projeto acadêmico.
