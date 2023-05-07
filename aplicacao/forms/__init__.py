from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, length, email, equal_to, NumberRange


class FormLogin(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(), length(4, 12)])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 18)])
    submit_entrar = SubmitField('Entrar')


class FormCadastrarUsuario(FlaskForm):
    usuario = StringField('Nome de Usuário', validators=[DataRequired(), length(5, 12)])
    email = StringField('Email', validators=[DataRequired(), email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 18)])
    confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), equal_to('senha')])
    submit_cadastrar = SubmitField('Cadastrar')


class FormCasdastrarProduto(FlaskForm):
    modelo = StringField('Modelo', validators=[DataRequired(), length(2, 25)])
    marca = StringField('Marca', validators=[DataRequired(), length(2, 15)])
    preco = DecimalField('Preço', validators=[DataRequired()])
    estoque = IntegerField('Estoque', validators=[DataRequired()])
    submit_cadastrar_produto = SubmitField('Cadastrar')