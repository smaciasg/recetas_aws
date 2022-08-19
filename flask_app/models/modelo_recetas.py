from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import modelo_registro

class Receta:

    def __init__(self,data):
        self.id = data['id']
        self.nombre_receta = data['nombre_receta']
        self.descripcion = data['descripcion']
        self.instrucciones = data['instrucciones']
        self.fecha_creacion = data['fecha_creacion']
        self.menor30 = data['menor30']
        self.created_at = data['created_at']
        self.creador_id = data['creador_id']
        self.nombre_creador = data['nombre_creador']
        self.apellido_creador = data['apellido_creador']

    @classmethod
    def enviar_receta_db(cls,formulario):
        query = "INSERT INTO recetas (nombre_receta, descripcion, instrucciones, fecha_creacion, menor30, creador_id) VALUES (%(nombre_receta)s, %(descripcion)s, %(instrucciones)s, %(fecha_creacion)s, %(menor30)s, %(creador_id)s);"
        result = connectToMySQL('login_red').query_db(query,formulario)
        return result

    @classmethod
    def consultar_todas_las_recetas(cls):
        query = "SELECT recetas.*, users.first_name AS nombre_creador, users.last_name AS apellido_creador FROM recetas JOIN users ON recetas.creador_id = users.id;"
        result = connectToMySQL('login_red').query_db(query)
        lista_resultados = []
        for recete in result:
            lista_resultados.append(cls(recete))
        return lista_resultados

    @classmethod
    def consultar_receta_id(cls,formulario):
        query = "SELECT recetas.*, users.first_name AS nombre_creador, users.last_name AS apellido_creador FROM recetas JOIN users ON recetas.creador_id = users.id WHERE recetas.id = %(id)s;"
        result = connectToMySQL('login_red').query_db(query,formulario)
        return cls(result[0])

    @classmethod
    def actualizar_receta_por_id(cls,formulario):
        query = "UPDATE recetas SET nombre_receta=%(nombre_receta)s, descripcion=%(descripcion)s, instrucciones=%(instrucciones)s, fecha_creacion =%(fecha_creacion)s, menor30= %(menor30)s, creador_id=%(creador_id)s WHERE id=%(id)s" 
        result = connectToMySQL('login_red').query_db(query,formulario)
        return result

    @classmethod
    def eliminar_receta(cls,formulario):
        query = "DELETE FROM recetas WHERE id=%(id)s"
        result = connectToMySQL('login_red').query_db(query,formulario)
        return result

    #////////////////////////////////////////////
    # MÉTODO ESTÁTICO PARA VALIDACIÓN DE INFORMACIÓN
    @staticmethod
    def validador_estructura_receta(formulario):
        es_valido = True

        if len(formulario['nombre_receta']) < 3:
            flash("La receta debe tener un nombre mínimo de 3 caracteres", 'receta')
            es_valido = False

        if len(formulario['descripcion']) < 3:
            flash("La descripción debe tener mínimo 3 caracteres", 'receta')
            es_valido = False

        if len(formulario['instrucciones']) < 3:
            flash("La instrucción debe tener un paso a paso, mínimo 3 caracteres", 'receta')
            es_valido = False

        if formulario['fecha_creacion'] == "":
            flash("La fecha de creación es requerida", 'receta')
            es_valido = False

        return es_valido

