from datetime import datetime, timedelta
import base64
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import os


class User (UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    lider = db.Column(db.Boolean, default=False)
    puesto = db.Column(db.String(80), nullable=True)
    objetivos = db.relationship('Objetivos', backref='User', lazy='dynamic')
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    
    def __repr__(self):
      return '<User {}>'.format(self.username)   
    def set_password(self, password):
      self.password_hash = generate_password_hash(password)

    def check_password(self, password):
      return check_password_hash(self.password_hash, password)
    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

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

