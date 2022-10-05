from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_cors import CORS, cross_origin

from controllers.carruselController import *
from controllers.loginController import valLoginController
from controllers.usuarioController import registrarUsuarioController

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

app.secret_key = "clave"

# rutas
# ver carrusel API *********************************************
@app.route('/api/carrusel')
@cross_origin()
def obtenerCarrusel():
    return verCarruselController()

# pagina por Principal 
@app.route("/")
@cross_origin()
def index():
    return render_template("Login.html", dato = "")

# validar login 
@app.route("/valLogin", methods = ["POST"])
@cross_origin()
def valLogin():
    datos = [
        request.form['user'], 
        request.form['password'] ]    
    respuesta = valLoginController(datos)    
    if len (respuesta) != 0:
        session["du"] = respuesta[0]
        return redirect ( url_for ("inicio") )
    else:
        
        flash("loginIncorrecto")
        return redirect ( url_for("index") )

# Ruta para el registro de usuarios **********************************************
@app.route("/registrarUsuario", methods = ["POST"])
@cross_origin()
def registrarUsuario():
    datos = [
        request.form['nombre'], 
        request.form['apellido'], 
        request.form['tipoDocumento'], 
        request.form['numeroDocumento'],
        request.form['id_rol'], 
        request.form['contrasena'], 
        "1", 
        request.form['correo'], 
        request.form['telefono'], 
        request.form['ficha'], 
        request.form['fechaNacimiento']    
    ]
    
    if registrarUsuarioController(datos):
        flash ("Registro Usuario Exitoso")
    else:
        flash("Error")
        
    return redirect ( url_for("index") )
     

# ruta para la pagina principal de inicio sesion
@app.route("/inicio")
@cross_origin()
def inicio():
    if not "du" in session: return redirect ( url_for("index") )    
    else: return render_template("usuarios.html")


@app.route("/cerrarSesion")
@cross_origin()
def cerrarSesion():
    session.clear()    
    return redirect ( url_for("index") )


# Control de errores ****************************************
@app.errorhandler(404)
def error404(e):
    return "pagina no idexada"

if __name__ == '__main__':
    app.run(port = 3000, debug = True)