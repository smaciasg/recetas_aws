from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.modelo_registro import Registro
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registro_use_db():
    #Voy a crear las funciones de validación 
    if not Registro.validaciones_registro_user(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    dic_data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    id = Registro.guardar_nuevo_user(dic_data)
    session['user_id'] = id
    return  redirect('/visualizador_recetas')

@app.route('/login', methods=['POST'])
def ingresar():
    data = {'email': request.form["email"]}
    print(data)
    user = Registro.consulta_por_email(data)
    if not user:
        flash("Email no se encuentra registrado",'login')
        return redirect('/')
    # valifación clave
    if not bcrypt.check_password_hash(user.password,request.form["password"]):
        flash("Contraseña inválida por favor verifique", 'login')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/visualizador_recetas')

@app.route('/logout')
def cerrar_sesion():
    session.clear()
    return redirect('/')