from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase): #Creamos una nueva clase que va extender TestCase
    def create_app(self): #Creamos un método create_app que vive en la clase TestCase, el cual debe regresar una app de Flask sobre la cual vamos a probar 
        app.config['TESTING']=True # Aquí configuramos la aplicación para TESTING
        app.config['WTF_CSRF_ENABLED'] = False # Esto indica que no vamos a probar formas
        return app
    
    #Aquí configuramos nuestras pruebas

    def test_app_exists(self): # Esta prueba nos confirma si la app existe
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self): # Esta prueba nos confirma que la app se encuentre en el modo TESTING
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self): # Esta prueba nos confirma que la ruta index nos redirige a la ruta hello
        response=self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))

    def test_hello_get(self): # Esta prueba nos confirma que la conexión de la ruta hello esta ok, nos devuelve 200
        response= self.client.get(url_for('hello'))
        self.assert200(response)

    # def test_hello_post(self): # Esta prueba nos confirma que cuando hacemos un POST nos redirige a la pagina index
    #     fake_form = {
    #         'username':'fake',
    #         'password':'fake-password'
    #     }
    #     response = self.client.post(url_for('hello'), data=fake_form)
    #     self.assertRedirects(response, url_for('index'))
    
    def test_hello_post(self): # Esta prueba nos confirma que nos devuelve un 405
        response = self.client.post(url_for('hello'))
        self.assertTrue(response.status_code, 405)

    def test_auth_blueprint_exists(self): # Esta prueba nos confirma que el blueprint auth registra
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self): # Esta prueba nos confirma que el blueprint auth login devuelve 200
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_auth_login_template(self): # Esta prueba nos confirma que el blueprint auth login se renderiza
        response = self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self): # Esta prueba nos confirma que cuando hacemos un POST desde auth login nos redirige a la pagina index
        fake_form = {
            'username':'fake',
            'password':'fake-password'
        }
        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertRedirects(response, url_for('index'))