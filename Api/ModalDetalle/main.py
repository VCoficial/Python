from flask import Flask, render_template, request, url_for, redirect, flash
from flask_cors import CORS, cross_origin

from controllers.controlador import verUsuarioscontrol
from controllers.controladorPc import verequiposcontrol
from controllers.controlador import registrarUsuarioController
from controllers.controlador import modificarUsuarioControl
from controllers.controlador import borrarUsuariosModel


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

# pagina por Principal 
@app.route("/")
@cross_origin()
def index():
    return render_template("Index.html")

#---------------------------------------------------------------------
#para ver datos de usuario   
@app.route('/api/usuarios')
@cross_origin()
def getAllUsers():
    return verUsuarioscontrol()

@app.route('/api/usuarios/<id>')
@cross_origin()
def getoneuser(id):
    return verUsuarioscontrol(id)

@app.route("/api/registrarUsuario", methods = ["POST"])
@cross_origin()

def registrarUsuario():
    if 'id' in request.json:
        result = updateUser()
    else:
        result = createUser()
    return result
    
    
def createUser():  
    datos = [
        request.json['nombre'], 
        request.json['Telefono'] 
          ]
    
    """print (datos)
    return "jj"""
    
        
    return registrarUsuarioController(datos)

def updateUser():
    datos = [
        request.json['id'],
        request.json['nombre'],
        request.json['Telefono']
    ]
    return modificarUsuarioControl(datos)    
    


@app.route('/api/usuarios/<id>', methods = ['DELETE'])
@cross_origin()
def removeUsers(id):
    return borrarUsuariosModel(id)

#------------------------------------------------------------------------
#ver equipos
#para ver datos de usuario   
@app.route('/api/pc')
@cross_origin()
def getAllPc():
    return verequiposcontrol()
    
@app.route('/api/pc/<id>')
@cross_origin()
def getonePc(id):
    return verequiposcontrol(id)
    





#-----------------------------------------------------------------
if __name__ == '__main__':
    app.run(port = 5000, debug = True)
 