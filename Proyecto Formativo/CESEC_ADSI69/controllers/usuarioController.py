from controllers.funciones import validarDatosVacios
from models.usuarioModel import registrarUsuarioModel

def registrarUsuarioController(datos):
    
    respuesta = False
    
    # validamos si los campos se encuentran diligenciados
    if not validarDatosVacios(datos):        
        respuesta = registrarUsuarioModel(datos)        
    return respuesta