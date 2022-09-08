from controles.inicioSesionControl import validarInicio
from templates.formulario import inicioSesion
from templates.paginaPrincipal import inicio

if validarInicio(inicioSesion()):
    inicio()
else:
    print("usuario incorrecto!")