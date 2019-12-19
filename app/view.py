from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/menu')
def menu():
    return render_template('/menu.html')

@app.route('/doorder')
def doorder():
    return render_template('/doorder.html')

@app.route('/order')
def order():
    return render_template('/order.html')





