from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'
db.init_app(app)

from projeto import routes


#Para rodar o servidor: flask --app (nome do arquivo) run
#Para rodar em modo debug: flask --app (nome do arquivo) run --debug
#no modo debug, toda alteração será atualizada automaticamente sem ter q reiniciar o server