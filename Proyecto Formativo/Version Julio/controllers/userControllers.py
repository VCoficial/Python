from models.usersModel import *
from flask import jsonify

# ver usuarios ***************************************************************
def verusuariocontrol (usuario = ""):
    data = verusuario(usuario)
    result = []
    for row in data:
        content = {
                'id':row[0],
                'usuario':row[1],
                'paswword':row[2],  
            }
        result.append(content)
    return jsonify(result)

# Ver Carrusel ***************************************************************
def verCarruselcontrol (id = ""):
    data = verCarruselmodel(id)
    result = []
    for row in data:
        content = {
                'id':row[0],
                'img':row[1],
                'descripcion':row[2],
                'urlink':row[3],
                'fecha_inicio':row[4],
                'fecha_fin':row[5],
                'estado':row[6]
            }
        result.append(content)
    return jsonify(result)

# crear usuarios **************************************************************
def crearUsuariosControllers(datos):

    result = [ str(crearUsuariosModel(datos) ) ]
    
    return jsonify(result)

# modificar usuarios ****************************************************************
def modificarUsuariosControllers(datos):
    result = [ str(modificarUsuarioModel(datos) ) ]
    
    return jsonify(result)

# borrar usuarios ******************************************************************
def borrarUsuariosControllers(datos):
    result = [ str(borrarUsuarioModel(datos) ) ]
    
    return jsonify(result)