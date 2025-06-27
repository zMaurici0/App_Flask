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

✅ Cadastro de Livros
Formulário simples para inserir:

- Nome do livro
- Descrição
- Valor
- Dados armazenados via SQLAlchemy no banco livros.sqlite3.

🎥 Consulta de Filmes
Consulta à API do TMDB para exibir filmes:

-Populares
-Animações
-Filmes lançados em 2010
