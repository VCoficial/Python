from models.usuarioModel import *
from flask import jsonify
from models.usuarioModel import registrarUsuarioModel
from controllers.funciones import validarDatosVacios

#-------------------------------------------------------------------------------

def verUsuarioscontrol (id = ""):
    data = verUsuarios(id)
    result = []
    for row in data:
        content = {
         
                'nombre':row[1],
                'Telefono':row[2] 
              
            }
        result.append(content)
    return jsonify(result)


def registrarUsuarioController(datos):
    
    respuesta = registrarUsuarioModel(datos)  
    # validamos si los campos se encuentran diligenciados   
       
    return respuesta



def modificarUsuarioControl(datos):
    result = [str(modificarUsuariosModel(datos))]
    return jsonify(result)

def borrarUsuarioControl(id):
    result = [str(borrarUsuariosModel(id))]
    return jsonify(result)

#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------

