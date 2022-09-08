from funciones.funciones2 import validarListaCaracteres
from modelos.inicioSesionModelo import inicioSesionModelo


def validarInicio(datos):

    if datos[0] =="" or datos[1]=="":
        print("no dejar campos vacios")
        validar=False
    elif not validarListaCaracteres(datos[0],"123456789") or not validarListaCaracteres(datos[1],"123456789"):
        print("No utilice numeros en usuario y contraseña")
        validar= False
    else: 
        validar = True

        if validar:
            print("consulta bade de datos")
            if len(inicioSesionModelo(datos)) !=0:
                return True
            else:   
                return False
        else:
            return False
