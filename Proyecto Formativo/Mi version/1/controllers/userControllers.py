import re
from unittest import result
from models.usersModel import *
from flask import jsonify

# ver usuarios *********************************************************
def verCarruselControllers(id=""):

    datos = verCarruselModel(id)

    result = []

    # estructura formato json
    for row in datos:
        contenido = {
            'id':row[0],
            'img':row[1],
            'descripcion':row[2],
            'url':row[3],
            'fecha_inicio':row[4],
            'fecha_fin':row[5],
            'estado':row[6]

        }
        result.append(contenido)
    
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