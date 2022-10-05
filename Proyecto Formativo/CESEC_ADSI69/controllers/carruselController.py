from models.carruselModel import *
from flask import jsonify

# ver usuarios **********************************************
def verCarruselController(id = ""):
    
    datos = verCarruselModel(id)
    
    result = []
    
    # estructura formato json
    for row in datos:
        contenido = {
            'id' : row[0],
            'img': row[1], 
            'descripcion': row[2], 
            'url': row[3], 
            'fecha_inicio': row[4], 
            'fecha_fin': row[5], 
            'estado': row[6]  
        }
        result.append(contenido)
    
    return jsonify(result)
