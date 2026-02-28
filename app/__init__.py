from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .config import DevelopmentConfig
from .auth import auth
from .models import UserModel

login_manager = LoginManager() #Crea una instancia de LoginManager, que es la clase principal de Flask-Login para manejar el inicio de sesión y la autenticación de usuarios.
login_manager.login_view = 'auth.login'
"""login_view: Esta propiedad de LoginManager 
indica cuál es la vista (ruta o endpoint) que 
se debe mostrar cuando un usuario no autenticado 
intenta acceder a una página protegida.
En este caso, 'auth.login' hace referencia a la 
vista de inicio de sesión dentro de un blueprint llamado auth. 
Esto significa que, si el usuario no ha iniciado sesión e intenta 
acceder a una página que requiere autenticación, Flask-Login 
lo redirigirá a la ruta definida por 'auth.login', que sería 
algo como /auth/login si sigues la convención de blueprints."""


@login_manager.user_loader #Este decorador se usa para registrar una función que Flask-Login utilizará para cargar un usuario desde la base de datos cuando sea necesario.
def load_user(username):
    return UserModel.query(username) #Este método busca en la base de datos Firestore al usuario cuyo username corresponde al ID del usuario almacenado en la cookie de sesión y devuelve una instancia de UserModel.

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(DevelopmentConfig)
    login_manager.init_app(app) #inicio el login_manager antes de los blueprints
    app.register_blueprint(auth)
    return app