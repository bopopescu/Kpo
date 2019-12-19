import flask_sqlalchemy
from flask import Flask, render_template
from config import Configuration
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
app = Flask(__name__, static_folder='static')
bootstrap = Bootstrap(app)
app.config.from_object(Configuration)
app.config.from_object('config')
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)




