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


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(405)
def internal_error(error):
    return render_template('405.html'), 405


@app.errorhandler(403)
def internal_error(error):
    return render_template('403.html'), 403


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.errorhandler(504)
def internal_error(error):
    return render_template('504.html'), 504


@app.errorhandler(406)
def internal_error(error):
    return render_template('406.html'), 406
