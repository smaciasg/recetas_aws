# Ejecuta la aplicación
from flask_app import app
from flask_app.controllers import controlador_formulario 
from flask_app.controllers import controlador_recetas

#Corremos la aplicación: 
if __name__=="__main__":
    app.run(debug=True)