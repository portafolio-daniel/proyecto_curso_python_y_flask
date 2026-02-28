from flask_login import UserMixin
from app.firestore_service import get_user

# Es una clase simple que encapsula la información básica del usuario
class UserData: 
    def __init__(self, username, password):
        self.username = username
        self.password = password

#Esta clase hereda de UserMixin, lo que significa que ahora tiene las funcionalidades de autenticación que necesita Flask-Login (como is_authenticated, get_id, etc.)
class UserModel(UserMixin):
    def __init__(self, user_data):
        #Recibe la clase UserData
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod #Indica que este método no depende de la instancia de la clase. Es decir, puedes llamarlo sin instanciar UserModel.
    def query(user_id): #Este método busca a un usuario en la base de datos Firestore por su user_id
        user_doc = get_user(user_id)
        user_data = UserData(
            username=user_doc.id,
            password=user_doc.to_dict()['password']
        )
        return UserModel(user_data) #retorna una instancia de UserModel que representa al usuario buscado.
