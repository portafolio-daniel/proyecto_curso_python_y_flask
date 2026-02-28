from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from markupsafe import escape
from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users, get_todos
from flask_login import login_required, current_user

# Create the application instance
app = create_app()

todos=['Comprar café', 'Enviar solicitud', 'Entregar video al productor']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests') #Los tests será todo lo que encuentre en la carpeta tests
    unittest.TextTestRunner().run(tests)           #Corremos los test que descubrimos anteriormente

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip=request.remote_addr                   # Capturo la ip del usuario
    session['user_ip'] = user_ip                  # Guardo la variable en session
    response = make_response(redirect('/hello'))  # Redirecciono a la página hello.html
    #response.set_cookie('user_ip', user_ip)
    return response

# Create a URL route in our application for "/"
@app.route('/hello', methods=['GET'])
@login_required #Con esta linea ya no hay manera de entrar a la ruta hello sin un login (from flask_login import login_required)
def hello():
    user_ip = session.get('user_ip')   # Si hay un user_ip en session, lo rescato.
    username = current_user.id # Si hay un username en session, lo rescato.
    login_form = LoginForm()           # Ejecuto la clase LoginForm
    #user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':get_todos(user_id=username),
        'login_form':login_form,
        'username':username, 
    }

    return render_template('hello.html', **context) 

if __name__=="__main__":
    app.run(debug=True)

