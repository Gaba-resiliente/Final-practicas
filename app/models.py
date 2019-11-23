from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    contraseña = db.Column(db.String(128), nullable=False)
    lider = db.Column(db.Boolean, default=False)
    puesto = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.nombre_apellido)    