from flask import Blueprint

# Registra el blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth') 

# url_prefix='/auth' significa que todas las rutas definidas en el blueprint auth tendrán el prefijo /auth. 
# Así, la ruta de inicio de sesión definida en views.py se convierte en /auth/login

from . import views


"""¿Qué son los Blueprints?
Un blueprint es un objeto que define una colección de rutas, vistas 
Permiten agrupar funcionalidades específicas de la aplicación, como autenticación, 
administración, API, etc., en un solo lugar, lo que facilita su desarrollo y mantenimiento."""

# auth es el nombre del blueprint, que se usará para registrar rutas en la aplicación
# __name__ se refiere al módulo actual.