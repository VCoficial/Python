""" from distutils.log import debug
from struct import pack
from flask import Flask

from controller.controller import controladorUsuarios

app = Flask(__name__)

#rutas
@app.route('/')
def index():
    return "hola mundo"

@app.route('/pagina2/<name>/')
@app.route('/pagina2/')
def pagina2(name = ""):
    controladorUsuarios(name)
    return "parametro enviado: "

if __name__ == '__main__':
    app.run(debug=True,port=8000) """

from flask import Flask           # importamos  Flask
from flask import render_template # importamos renderizador de templates
from flask import request         # importamos  request
from controller.controller import controladorUsuarios
# El contenido que un cliente web manda al servidor siempre va almacenado en la Request

app = Flask(__name__)             # creamos un objeto 
# app = Flask(__name__, template_folder = 'nombre carpeta') en caso de utilizar otra carpeta de templates

# rutas 
@app.route('/')                   # wrap o decorador
def index():
    return "pagina inicial"

@app.route('/pagina2/')           # wrap o decorador
@app.route('/pagina2/<name>')   
def pagina2(name = ""):
    datos = controladorUsuarios(name)
    return  render_template("formulario.html", dato = datos)



if __name__ == '__main__':        # lanzador del servidor
    app.run(debug=True, port=8000)        
