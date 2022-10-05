import os

# validar que los datos no esten vacios **************************************************************
def validarDatosVacios(datos):
    vacio = False    
    for i in datos:        
        if len(i) == 0:
            vacio = True
    return vacio

# Generar Codigo QR *************************************************************************************
def crearQR(cadena, nombreimagenG):
    import qrcode
    
    ruta = ""
    imagen = qrcode.make(cadena)    # generamos imagen QR
    nombre_imagen = nombreimagenG + ".png"
    
    # creamos archivo de imagen
    archivo_imagen = open(ruta+nombre_imagen, "wb")
    imagen.save(archivo_imagen)
    archivo_imagen.close()
    
# Cargar Imagen y equipo ***************************************************************************************
def validarExtension(archivo, extensionesPermitidas):
    archivo = archivo.split( "." )
    if archivo[1].lower() in extensionesPermitidas:
        return True
    else: return False

# fotos
def subirFotos(archivo, nombreArchivo, tipo):
    ruta = "static/img/usuarios/" + nombreArchivo + "/"
    os.makedirs()
    
    if tipo == "usuario":
        enlace = "static/img/usuario/photos"
    elif tipo == "equipo": 
        enlace = "static/img/usuario/photos"
    elif tipo == "carrusel":
        enlace = "static/img/carrusel"
        
    extensionesPermitidas  =["jpg"]    

    if archivo and validarExtension(archivo.filename, extensionesPermitidas):    
        ruta = os.path.join(enlace, nombreArchivo)
        archivo.save(ruta)
        return True
    else:
        return False
