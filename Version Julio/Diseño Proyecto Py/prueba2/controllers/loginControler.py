from models.loginModel import guardarDatos

def validarDatos(lista):
    mensaje = True
    for i in lista:
        if len(i) == 0:
            mensaje = False
    return mensaje

def guardarDatos(lista):
    if validarDatos(lista):
        pass
    else:
        return False
