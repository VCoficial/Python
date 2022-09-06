from flask import Flask,  render_template, request, redirect, url_for, session # pip install Flask
from flask_mysqldb import MySQL,MySQLdb # pip install Flask-MySQLdb
from os import path #pip install notify-py
from notifypy import Notify
from flask_cors import CORS, cross_origin
from flask import session

from controllers.userControllers import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'senacta'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
cors = CORS (app)
app.config['CORS_HEADERS'] = 'Content-Type'

#--------------------------------------------------
#Login
@app.route('/')
def home():
    return render_template("login.html")    

@app.route('/layout', methods = ["GET", "POST"])
def layout():
    session.clear()
    return render_template("login.html")

@app.route('/login', methods= ["GET", "POST"])
def login():

    notificacion = Notify()

    if request.method == 'POST':
        documento = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuario WHERE documento=%s",(documento,))
        user = cur.fetchone()
        cur.close()

        if len(user)>0:
            if password == user["contraseña"]:
                session['name'] = user['nombre']
                session['email'] = user['documento']
                session['tipo'] = user['id_Rol']

                if session['tipo'] == 1:
                    return render_template("vigilante.html")
                elif session['tipo'] == 2:
                    return render_template("usuario.html")
            else:
                notificacion.title = "Error de Acceso"
                notificacion.message="Correo o contraseña no valida"
                notificacion.send()
                return render_template("templates/login.html")
        else:
            notificacion.title = "Error de Acceso"
            notificacion.message="No existe el usuario"
            notificacion.send()
            return render_template("login.html")
    else:
        return render_template("login.html")

#--------------------------------------------------
#Registro
@app.route('/registro', methods = ["GET", "POST"])
def registro():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario")
    con = cur.fetchall()

    cur.close()

    notificacion = Notify()

    if request.method == 'GET':
        return render_template("registro.html", con = con )
    
    else:
        email = request.form['email']
        password = request.form['password']
        name = request.form['nombre']
        apellido = request.form['apellido']
        tel = request.form['telefono']
        tipo = request.form['tipo']
        correo = request.form['correo']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuario (id_tipo, documento, contraseña, nombre, apellido, correo, telefono) VALUES (%s,%s,%s,%s,%s,%s,%s)", (tipo, email, password, name, apellido, correo, tel))
        mysql.connection.commit()
        notificacion.title = "Registro Exitoso"
        notificacion.message="ya te encuentras registrado en el programa"
        notificacion.send()
        return redirect(url_for('login'))

#-------------------------------------------------------------------
#carrusel
@app.route('/api/carrusel')
@cross_origin()
def getAllUsers():
    return verCarruselcontrol()
    
@app.route('/api/usuarios/<id>')
@cross_origin()
def getUsers(id):
    return verCarruselcontrol(id)

if __name__ == '__main__':
    app.secret_key = 'mysecretkey'
    app.run(debug=True)