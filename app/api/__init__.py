from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import users, errors, tokens

login = LoginManager(app)
login.login_view = 'login'