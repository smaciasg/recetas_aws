from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import modelo_recetas
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Registro:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def guardar_nuevo_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL('login_red').query_db(query,data)
        return result

    #----------------------------------------
    # FUNCIÓN DE VALIDACIÓN

    @staticmethod
    def validaciones_registro_user(formulario):
        es_valido = True

        if (formulario["first_name"].isalpha() == False) or (len(formulario["first_name"]) < 2) :
            flash("El nombre debe tener al menos dos caracteres y no debe contener dígitos ni caracteres especiales", 'registro')
            es_valido = False

        if (formulario["last_name"].isalpha() == False) or (len(formulario["last_name"]) < 2):
            flash("El apellido debe tener al menos dos caracteres y no debe contener dígitos ni caracteres epeciales", 'registro')
            es_valido = False

        if not EMAIL_REGEX.match(formulario["email"]):
            flash("Email con formato no válido", 'registro')
            es_valido = False

        # Comprobar si el correo existe en la bd
        query = "SELECT * FROM users WHERE email = %(email)s"
        resul = connectToMySQL('login_red').query_db(query,formulario)
        if len(resul) > 0:
            flash('El email ya se encuentra registraso', 'registro')
            es_valido = False

        # Comprobar que el password tiene al menos 6 caracteres-
        if len(formulario["password"]) < 8:
            flash("La longitud mínima del password debe ser 6 dígitos", 'registro')
            es_valido = False

        if ((formulario["password"].isalpha() == True) or (formulario["password"].isnumeric() == True)):
            flash("La contraseña debe ser alfanumérica", 'registro')
            es_valido= False

        if ((formulario["password"].islower() == True) or (formulario["password"].isupper() == True)):
            flash("La contraseña debe tener al menos un caracter en mayúscula y uno en minúscula", 'registro')
            es_valido= False

        if formulario["password"] != formulario["password_confirmacion"]:
            flash("Las contraseñas no coinciden por favor verifique", 'registro')
            es_valido = False

        return es_valido

    #////////////////////////////////
    @classmethod
    def consulta_por_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        resul = connectToMySQL('login_red').query_db(query,data)
        if len(resul) < 1 :
            return False
        else:
            return cls(resul[0])
    
    @classmethod
    def consulta_por_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        resul = connectToMySQL('login_red').query_db(query,data)
        return cls(resul[0])