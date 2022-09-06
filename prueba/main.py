from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/pagina2')
def pagina2():
    nombre = request.args.get("user", "No envio usuario")
    password = request.args.get("password", "No envio contraseña")
    return "Usuario: "+nombre+" "+password

if __name__ == '__main__': 
    app.run(debug=True, port=8000)  