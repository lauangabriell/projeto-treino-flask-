# 🏋️ Sistema de Treinos

**Aplicação web para criação e organização de treinos de academia, com acompanhamento de dados físicos e cálculo de IMC.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=flat-square">
</p>

<p align="center">
  <a href="https://projeto-treino-flask-sxjk.onrender.com"><b>🔗 Acessar aplicação</b></a>
</p>

---

## Sobre o Projeto

O **Sistema de Treinos** é uma plataforma web desenvolvida para ajudar usuários a organizar sua rotina de academia de forma simples e estruturada.

Cada usuário cria sua conta, informa seus dados físicos (idade, sexo, altura, peso, objetivo e nível de experiência) e monta seus próprios treinos, separados por dia da semana e por grupo muscular. A plataforma calcula automaticamente o IMC do usuário e mantém uma biblioteca de exercícios organizada por categoria, disponível para reaproveitamento entre treinos.

---

## Objetivos

O objetivo principal do projeto é facilitar a organização e o acompanhamento de treinos de academia, oferecendo uma ferramenta simples que centraliza dados físicos, planejamento semanal e histórico de exercícios em um só lugar.

A plataforma busca:

- Eliminar a necessidade de planilhas ou anotações em papel
- Organizar os treinos de forma visual, por dia da semana e grupo muscular
- Acompanhar a evolução física do usuário através do cálculo de IMC

---

## Funcionalidades

- Cadastro e login de usuário com senha criptografada
- Perfil com dados físicos (idade, sexo, altura, peso, objetivo, nível de experiência)
- Cálculo automático de IMC com classificação (abaixo do peso, normal, sobrepeso, obesidade)
- Criação de treinos organizados por dia da semana e categoria muscular
- Biblioteca com 55 exercícios pré-cadastrados (5 por grupo muscular)
- Adição de exercícios personalizados, com séries, repetições e tempo de descanso
- Edição e exclusão de treinos e exercícios

---

## Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal do back-end |
| Flask | Framework web e definição de rotas |
| Flask-SQLAlchemy | ORM para comunicação com o banco de dados |
| PostgreSQL (Neon) | Banco de dados relacional |
| Jinja2 | Motor de templates HTML |
| Render | Hospedagem e deploy da aplicação |

---

## Estrutura do Projeto

```
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
```

---

## Dependências

- Python (versão 3.11 ou superior)
- pip (gerenciador de pacotes, incluído com o Python)
- Navegador atualizado (Chrome, Firefox, Edge)
- Variável de ambiente `DATABASE_URL` apontando para um banco PostgreSQL *(opcional — sem ela, a aplicação usa SQLite local)*
- Visual Studio Code *(recomendado)*

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/lauangabriell/projeto-treino-flask.git
cd projeto-treino-flask
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie a aplicação

```bash
python app.py
```

### 5. Acesse no navegador

```
http://localhost:5000
```

---

## Nossos Colaboradores

Este projeto foi desenvolvido com dedicação por:

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/lauangabriell">
        <img src="https://github.com/lauangabriell.png" width="100" height="100"><br>
        <b>Lauan Gabriel Pereira Lima</b>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Lanabastos">
        <img src="https://github.com/Lanabastos.png" width="100" height="100"><br>
        <b>Lanna Grazielle Martins Bastos</b>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/RudysGalaxy">
        <img src="https://github.com/RudysGalaxy.png" width="100" height="100"><br>
        <b>Francisco Ruda Gomes</b>
      </a>
    </td>
  </tr>
</table>

---

## Aplicação Online

A aplicação já está online e disponível para uso:

🔗 **[projeto-treino-flask-sxjk.onrender.com](https://projeto-treino-flask-sxjk.onrender.com)**

---

<p align="center">Projeto acadêmico.</p>
<p align="center"><a href="#-sistema-de-treinos">Voltar ao topo</a></p>
