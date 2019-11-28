from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Aceptar')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repetir Password', validators=[DataRequired(), EqualTo('password')])
    puesto = StringField('Puesto', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Nombre ya utilizado, ingresar otro nombre.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('email ya usado, ingresar otro.')
class ObjetivosForm(FlaskForm):
    nombre= StringField('Nombre', validators=[
        DataRequired(), Length(min=1, max=140)])
    que = StringField('¿Que se quiere hacer?', validators=[
        DataRequired(), Length(min=1, max=140)])
    porque = StringField('¿Por Que?', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Asignar Objetivos')
   
class BajaUser(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Aceptar')

class EditUser(FlaskForm):
    username = StringField('Username')
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repetir Password', validators=[DataRequired(), EqualTo('password')])
    puesto = StringField('Puesto', validators=[DataRequired()])
    submit = SubmitField('Aceptar')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usar otro nombre')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Usar otro email.')
class CambiarUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repetir Password', validators=[DataRequired(), EqualTo('password')])
    puesto = StringField('Puesto', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usar otro nombre.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Usa otro email.')

class BorrarObjetivo(FlaskForm):
    nombre= StringField('Nombre')
    que = StringField('¿Que se quiere hacer?')
    porque = StringField('¿Por Que?')
    submit = SubmitField('Aceptar')