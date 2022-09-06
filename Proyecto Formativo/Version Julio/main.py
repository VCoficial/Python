# Iniciar : py main.py
from flask import Flask,  render_template, request, redirect, url_for, session # pip install Flask
from flask_mysqldb import MySQL,MySQLdb # pip install Flask-MySQLdb
from os import path #pip install notify-py
from notifypy import Notify


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'senacta'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

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

                if session['tipo'] == 2:
                    return render_template("vigilante.html")
                elif session['tipo'] == 1:
                    return render_template("usuario.html")
            else:
                notificacion.title = "Error de Acceso"
                notificacion.message="Correo o contraseña no valida"
                notificacion.send()
                return render_template("login.html")
        else:
            notificacion.title = "Error de Acceso"
            notificacion.message="No existe el usuario"
            notificacion.send()
            return render_template("login.html")
    else:
        return render_template("login.html")

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
        rol = request.form['rol']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuario (documento, contraseña, nombre, apellido, telefono, id_Rol) VALUES (%s,%s,%s,%s,%s,%s)", (email, password, name, apellido, tel, rol))
        mysql.connection.commit()
        notificacion.title = "Registro Exitoso"
        notificacion.message="ya te encuentras registrado en el programa"
        notificacion.send()
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.secret_key = "llave"
    app.run(debug=True)