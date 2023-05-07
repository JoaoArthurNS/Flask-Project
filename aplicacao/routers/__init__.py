from aplicacao import app, database, bcrypt
from flask import redirect, render_template, url_for, flash
from aplicacao.forms import FormLogin, FormCadastrarUsuario, FormCasdastrarProduto
from aplicacao.models import usuario, produto
from flask_login import login_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        user = usuario.query.filter_by(usuario=form.usuario.data).first()
        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            login_user(user)
            flash(f'Login feito com sucesso para o user: {form.usuario.data}', 'alert-success')
            return redirect(url_for('index'))
        else:
            flash(f'Usuário ou senha inválidos', 'alert-danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Sessão Encerrada', 'alert-danger')
    return redirect(url_for('login'))


@app.route('/cadastro-usuario', methods=['GET', 'POST'])
def cadastro_usuario():

    form = FormCadastrarUsuario()
    if form.validate_on_submit():
        print(form.usuario.data)
        with app.app_context():
            senha_crypt = bcrypt.generate_password_hash(form.senha.data)
            try:
                user = usuario(usuario=form.usuario.data, email=form.email.data, senha=senha_crypt)
                database.session.add(user)
                database.session.commit()
                flash(f'Usuário cadastrado com sucesso', 'alert-success')
                return redirect(url_for('login'))
            except:
                flash(f'Não foi possível cadastrar usuário', 'alert-danger')
    return render_template('cadastro_usuario.html', form=form)

@app.route('/tela-principal')
@login_required
def index():
    return render_template('index.html')

@app.route('/cadastro_produtos', methods=['GET', 'POST'])
@login_required
def cadastro_produtos():
    form = FormCasdastrarProduto()
    if form.validate_on_submit():
        print(form.modelo.data)
        try:
            prod = produto(modelo=form.modelo.data, marca=form.marca.data, preco=form.preco.data, estoque=form.estoque.data)
            database.session.add(prod)
            database.session.commit()
            flash(f'Produto cadastrado com sucesso', 'alert-success')
            return redirect(url_for('cadastro_produtos'))
        except:
            flash(f'Não foi possível cadastrar produto', 'alert-danger')
    return render_template('cadastro_produtos.html', form=form)


@app.route('/lista_produtos')
def lista_produtos():
    produtos = produto.query.all()
    return render_template('lista_produtos.html', produtos=produtos)

@app.route("/lista_produtos/<id>")
def produto_id(id):
    produtos = produto.query.all()
    produtoId = produto.query.get(id)
    return render_template('lista_produtos.html', produtos=produtos, produtoId=produtoId)


@app.route("/remover_produto/<id>", methods=['GET', 'POST'])
def remover_produto(id):
    prod_delete = produto.query.get(id)
    database.session.delete(prod_delete)
    database.session.commit()
    return redirect(url_for('lista_produtos'))

