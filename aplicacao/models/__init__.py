from aplicacao import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return usuario.query.get(int(id_usuario))

class usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

class produto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    modelo = database.Column(database.String, nullable=False)
    marca = database.Column(database.String, nullable=False)
    preco = database.Column(database.Double, nullable=False)
    estoque = database.Column(database.Integer, nullable=False)