
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

config = {
    " desarrollo " : " bookshelf.config.DevelopmentConfig " ,
    " testing " : " bookshelf.config.TestingConfig " ,
    " default " : " bookshelf.config.DevelopmentConfig "
}


def  configure_app (app):
    config_name = os.getenv ( ' FLASK_CONFIGURATION ' , ' default ' )
    app.config.from_object (config [config_name]) # configuración predeterminada basada en objetos
    app.config.from_pyfile ( ' config.cfg ' , silent = True ) # configuración de carpetas de instancia


