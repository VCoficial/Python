def validarDatos(lista):
    mensaje = True
    for i in lista:
        if len(i) == 0:
            mensaje = False
    return mensaje
