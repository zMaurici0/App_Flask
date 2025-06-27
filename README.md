# Projeto Flask - Cadastro de Livros e Listagem de Filmes

Sistema web desenvolvido com Python e Flask com o objetivo de proporcionar uma experiência prática de aprendizado sobre os fundamentos do desenvolvimento web com foco em roteamento, templates com Jinja2, integração com banco de dados utilizando SQLAlchemy e consumo de APIs externas.

O sistema permite ao usuário realizar o cadastro de livros com nome, descrição e valor, armazenando os dados em um banco SQLite. Além disso, oferece uma interface para consultar filmes por categoria (populares, animações e lançamentos de 2010), utilizando a API pública do TMDB (The Movie Database).

Este projeto foi desenvolvido com fins educacionais, como uma forma de praticar conceitos essenciais do ecossistema Flask, incluindo criação de rotas, manipulação de formulários, persistência de dados e integração com serviços externos via requisições HTTP.

# Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask SQLAlchemy
- SQLite
- HTML (com Jinja2)
- API TMDB (para dados de filmes)

# Funcionalidades

📝 Lista de Conteúdos

- Permite ao usuário registrar conteúdos estudados ou abordados.
- Os conteúdos são exibidos em uma lista dinâmica na página inicial.

📊 Notas da Turma

- Interface para registrar notas de alunos.
- Os dados são inseridos via formulário e organizados na página.

✅ Cadastro de Livros
Formulário simples para inserir:

- Nome do livro
- Descrição
- Valor

🎥 Consulta de Filmes
Consulta à API do TMDB para exibir filmes:

- Populares
- Animações
- Filmes lançados em 2010

# Como executar localmente

Pré-requisitos: 

Antes de tudo, você precisa ter instalado no seu computador:

- Python 3.10+
- pip (gerenciador de pacotes do Python — normalmente já vem com o Python)
- Um editor de código, como VS Code

Para verificar se você já tem Python e pip instalados, use:
```
python --version
pip --version
```

1- Clone o repositório:
```
https://github.com/zMaurici0/App_Flask.git
```
2- Crie e ative um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
venv\Scripts\activate  (No Windows)
```
3- Instale as dependências:
```
pip install -r requirements.txt
```
4- Execute a aplicação:
```
flask --app projeto --debug run
```


