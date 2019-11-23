from flask import Flask
<<<<<<< HEAD
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config from object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import routes, models
=======
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate = Migrate(app,db)
from app import routes
>>>>>>> d385cad6a48699c62376d7136a0094bf3e5e88e4
