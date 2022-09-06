from flask import Flask
from flask import request
from flask import render_template

from controllers.loginControler import validarDatos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/pagina2')
def pagina2():
    user = request.args.get("user", "No envio usuario")
    password = request.args.get("password", "No envio contraseña")

    lista =[user, password]
    mensaje = ""

    if validarDatos(lista):
        mensaje = "datos correctos"
    else:
        mensaje = "datos vacios"
    return mensaje

if __name__ == '__main__': 
    app.run(debug=True, port=8000)  