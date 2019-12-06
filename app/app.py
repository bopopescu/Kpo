from flask import Flask,render_template
from config import Configuration
from datetime import datetime
from  flask_bootstrap import Bootstrap

app = Flask(__name__,static_folder='static')
bootstrap = Bootstrap(app)
app.config.from_object(Configuration)



