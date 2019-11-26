from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User (UserMixin,db.Model):
      id = db.Column(db.Integer, primary_key=True)
      username= db.Column(db.String(80), nullable=False)
      email = db.Column(db.String(256), unique=True, nullable=False)
      password = db.Column(db.String(128), nullable=False)
      lider = db.Column(db.Boolean, default=False)
      puesto = db.Column(db.String(80), nullable=False)
      objetivos = db.relationship('Objetivos', backref='User', lazy='dynamic')

      def __repr__(self):
          return '<User {}>'.format(self.nombre_apellido)   
      
      def set_password(self, password):
        self.password_hash = generate_password_hash(password)

      def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
        return User.query.get(int(id))

class Objetivos (db.Model):
      id = db.Column(db.Integer, primary_key=True)
      nombre = db.Column(db.String(80), nullable=False)
      que = db.Column(db.String(200), nullable=False)
      porque = db.Column(db.String(200), nullable=False)
      fecha_inicio = db.Column(db.DateTime, index=True, default=datetime.utcnow)
      usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))  
  
      def __repr__(self):
          return '<Objetivos {}>' % (self.nombre)    

class Acciones (db.Model):
      id = db.Column(db.Integer, primary_key=True)
      como = db.Column(db.String(200), nullable=False)
      fecha_fin = db.Column(db.DateTime)
      objetivos_id = db.Column(db.Integer, db.ForeignKey('objetivos.id'))

      def __repr__(self):
         return '<Acciones {}>' % (self.como)

