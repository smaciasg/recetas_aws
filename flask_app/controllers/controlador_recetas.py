from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.modelo_registro import Registro
from flask_app.models.modelo_recetas import Receta


@app.route('/creador_recetas')
def ver_data_user():
    if "user_id" not in session:
        return redirect('/')
    data = {"id":session['user_id'] }
    user = Registro.consulta_por_id(data)
    return render_template('creador_recetas.html',user=user)

@app.route('/enviar_receta', methods=['POST'])
def enviar_receta():
    if "user_id" not in session:
        return redirect('/')

    #Validación información antes de enviarla a guardado
    if not Receta.validador_estructura_receta(request.form):
        print("ESTOS ESTOT MANDANDO", request.form)
        return redirect('/creador_recetas')
    
    Receta.enviar_receta_db(request.form)
    return redirect('/visualizador_recetas')

@app.route('/visualizador_recetas')
def visualizador_recetas():
    if "user_id" not in session:
        return redirect('/')
    data = {"id":session['user_id'] }
    user = Registro.consulta_por_id(data)
    recetas = Receta.consultar_todas_las_recetas()
    return render_template('visual_recetas.html',recetas=recetas,user=user)

@app.route('/editar_receta/<int:id>')
def editar_receta(id):
    if "user_id" not in session:
        return redirect('/')

    data = {"id":id}
    receta = Receta.consultar_receta_id(data)

    if receta.creador_id != session['user_id']:
        session.clear()
        return redirect('/')

    return render_template('editar_receta.html', receta=receta)

@app.route('/actualizar_receta', methods=['POST'])
def actualizar_receta():
    if "user_id" not in session:
        return redirect('/')

    #Validación información antes de enviarla a guardado
    if not Receta.validador_estructura_receta(request.form):
        print("ESTOS ESTOT MANDANDO", request.form)
        session['receta_id'] = request.form['id']
        return redirect(f"/editar_receta/{session['receta_id'] }")

    Receta.actualizar_receta_por_id(request.form)
    return redirect('/visualizador_recetas')

@app.route("/ver_receta/<int:id>")
def ver_receta(id):
    if "user_id" not in session:
        return redirect('/')

    data = {"id":id}
    receta = Receta.consultar_receta_id(data)
    data_user = {'id':session['user_id']}
    user = Registro.consulta_por_id(data_user)
    return render_template('ver_receta.html', receta=receta, user=user)

@app.route('/eliminar_receta/<int:id>')
def eliminar_receta(id):
    if "user_id" not in session:
        return redirect('/')
    
    data = {'id':id}
    receta = Receta.consultar_receta_id(data)

    if receta.creador_id != session['user_id']:
        session.clear()
        return redirect('/')

    Receta.eliminar_receta(data)
    return redirect('/visualizador_recetas')