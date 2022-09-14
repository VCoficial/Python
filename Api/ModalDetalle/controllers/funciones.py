
def validarDatosVacios(datos):
    vacio = False    
    for i in datos:        
        if len(i) == 0:
            vacio = True
    return vacio

