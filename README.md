<div align="center">
  <h1>🏋️ Sistema de Treinos</h1>
  <p><strong>Aplicação web para criação e organização de treinos de academia, com acompanhamento de dados físicos e cálculo de IMC.</strong></p>
  <br/>
Mostrar Imagem
Mostrar Imagem
Mostrar Imagem
Mostrar Imagem

  <br/>
Mostrar Imagem

</div>

Sobre o Projeto

O Sistema de Treinos é uma plataforma web desenvolvida para ajudar usuários a organizar sua rotina de academia de forma simples e estruturada.

Cada usuário cria sua conta, informa seus dados físicos (idade, sexo, altura, peso, objetivo e nível de experiência) e monta seus próprios treinos, separados por dia da semana e por grupo muscular. A plataforma calcula automaticamente o IMC do usuário e mantém uma biblioteca de exercícios organizada por categoria, disponível para reaproveitamento entre treinos.


Objetivos

O objetivo principal do projeto é facilitar a organização e o acompanhamento de treinos de academia, oferecendo uma ferramenta simples que centraliza dados físicos, planejamento semanal e histórico de exercícios em um só lugar.

A plataforma busca:


Eliminar a necessidade de planilhas ou anotações em papel;
Organizar os treinos de forma visual, por dia da semana e grupo muscular;
Acompanhar a evolução física do usuário através do cálculo de IMC.



Funcionalidades


Cadastro e login de usuário com senha criptografada;
Perfil com dados físicos (idade, sexo, altura, peso, objetivo, nível de experiência);
Cálculo automático de IMC com classificação (abaixo do peso, normal, sobrepeso, obesidade);
Criação de treinos organizados por dia da semana e categoria muscular;
Biblioteca com 55 exercícios pré-cadastrados (5 por grupo muscular);
Adição de exercícios personalizados, com séries, repetições e tempo de descanso;
Edição e exclusão de treinos e exercícios.



Tecnologias Utilizadas

As seguintes tecnologias foram utilizadas no desenvolvimento do projeto:

TecnologiaFinalidadeMostrar Imagem PythonLinguagem principal do back-endMostrar Imagem FlaskFramework web e definição de rotasMostrar Imagem Flask-SQLAlchemyORM para comunicação com o banco de dadosMostrar Imagem PostgreSQL (Neon)Banco de dados relacionalMostrar Imagem Jinja2Motor de templates HTMLMostrar Imagem RenderHospedagem e deploy da aplicação


Estrutura do Projeto

projeto-treino-flask/
├── app.py                  # Rotas e lógica principal (controller)
├── models.py                # Tabelas do banco de dados (models)
├── requirements.txt          # Dependências Python
├── render.yaml               # Configuração de deploy do Render
├── .python-version           # Versão do Python usada no deploy
└── templates/
    ├── base.html             # Layout base (navbar + estilos)
    ├── login.html
    ├── register.html
    ├── dashboard.html         # Treinos organizados por dia
    ├── treino.html            # Detalhe de um treino
    └── perfil.html            # Dados físicos e IMC


Dependências

Para executar o projeto localmente, você precisará ter instalado:


Python (versão 3.11 ou superior);
pip (gerenciador de pacotes, incluído com o Python);
Navegador atualizado (Chrome, Firefox, Edge);
Uma variável de ambiente DATABASE_URL apontando para um banco PostgreSQL (opcional — sem ela, a aplicação usa SQLite local);
Visual Studio Code (recomendado).



Instalação

Siga os passos abaixo para rodar o projeto localmente:

1. Clone o repositório:

bashgit clone https://github.com/lauangabriell/projeto-treino-flask.git
cd projeto-treino-flask

2. Crie um ambiente virtual:

bashpython -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Instale as dependências:

bashpip install -r requirements.txt

4. Inicie a aplicação:

bashpython app.py

5. Acesse no navegador:

http://localhost:5000


<div align="center">
Nossos Colaboradores

Este projeto foi desenvolvido com dedicação por:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/lauangabriell">
        <img src="https://github.com/lauangabriell.png" width="100px" height="100px" style="border-radius:50%;object-fit:cover;" alt="Lauan Gabriel"/>
        <br/><b>Lauan Gabriel Pereira Lima</b>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Lanabastos">
        <img src="https://github.com/Lanabastos.png" width="100px" height="100px" style="border-radius:50%;object-fit:cover;" alt="Lanna Grazielle"/>
        <br/><b>Lanna Grazielle Martins Bastos</b>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/RudysGalaxy">
        <img src="https://github.com/RudysGalaxy.png" width="100px" height="100px" style="border-radius:50%;object-fit:cover;" alt="Francisco Rudá"/>
        <br/><b>Francisco Ruda Gomes</b>
      </a>
    </td>
  </tr>
</table>
</div>

<h1>🚀 Aplicação online</h1>
<p>
  A aplicação já está online e disponível para uso:
</p>
<p>
  Acesse agora:
  <a href="https://projeto-treino-flask.onrender.com" target="_blank">
    https://projeto-treino-flask.onrender.com
  </a>
</p>

<div align="center">
  <p>Projeto acadêmico.</p>
  <p>
    <a href="#-sistema-de-treinos">Voltar ao topo</a>
  </p>
</div>
