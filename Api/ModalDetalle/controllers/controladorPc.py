from models.equipoModel import *
from flask import jsonify




#--------------------------------------------------------

def verequiposcontrol (id = ""):
    data = verpcModel(id)
    result = []
    for row in data:
        content = {
                'serie':row[1],
                'id_Marca':[2],
                'detalle':[3],
                'id_Usuario':[4],
                'estado':[5],
                'img':[6]          }
        result.append(content)
    return jsonify(result)