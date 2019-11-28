from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, ObjetivosForm, BajaUser, EditUser, CambiarUser, BorrarObjetivo
from app.models import User, Objetivos


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user = User.query.get(current_user.id)
    obj = user.objetivos.all()
    print(current_user.objetivos)
    return render_template("index.html", title='Home Page', objetivos=obj)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuario o contraseña invalidas')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, puesto=form.puesto.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Bravo!!, Ya estas Registrado!!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/bajausuario', methods=['GET', 'POST'])
@login_required
def bajausuario():
    form = BajaUser()
    if form.validate_on_submit():
        lista = request.form.getlist("users")
        for i in lista:
            user = User.query.get(i)
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for('index'))
    users = User.get_all()
    return render_template("bajausuario.html", title='Home Page', form=form, users=users)

@app.route('/editarusuario', methods=['GET', 'POST'])
@login_required
def editarusuario():
    form = EditUser()
    if form.validate_on_submit():
        number_id = request.form.getlist("users")
        #for a in number_id:
        usuario = User.query.filter_by(id=number_id[0]).first()
        usuario.username=form.username.data
        usuario.email=form.email.data
        usuario.puesto=form.puesto.data
        usuario.set_password(form.password.data)
        db.session.commit()
        flash('Bravo!!, editaste un usuario')
    users = User.get_all()
    return render_template("editarusuario.html", title='Home Page', form=form, users=users)

@app.route("/objetivos", methods=['GET', 'POST'])
def objetivos():
    form = ObjetivosForm()
    if form.validate_on_submit():
        number_id = request.form.getlist("users")
        #for a in number_id:
        usuario = User.query.filter_by(id=number_id[0]).first()
        objetivos = Objetivos(nombre=form.nombre.data, que=form.que.data, porque=form.porque.data, author=usuario)
        db.session.add(objetivos)
        db.session.commit()
        flash('Se cargo un Objetivo')
        return redirect(url_for('index'))
    obje = Objetivos.get_all()
    users = User.get_all()
    return render_template("Objetivos.html", title='Objetivos', form=form, objetivos=obje, users=users)

@app.route("/eliminarobjetivos", methods=['GET', 'POST'])
def eliminarobjetivos():
    form = BorrarObjetivo()
    if form.validate_on_submit():
        number_id = request.form.getlist("users")
        for i in number_id:
            user = User.query.get(i)
            obj = user.objetivos.all()
            for p in obj:
                db.session.delete(p)
                db.session.commit()
        flash('Se cargo un Objetivo')
        return redirect(url_for('index'))
    users = User.get_all()
    return render_template("Objetivos.html", title='Objetivos', form=form, users=users)
