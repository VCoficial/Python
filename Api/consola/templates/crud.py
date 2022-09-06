from controllers.crudControllers import agregarUsuarioController, eliminarUsuariosController, verUsuarioController

#Ver Usuario**********************
def verUsuarios():
    datos = verUsuarioController()

    for i in datos:
        print(i)

#Crear Usuario****************************
def crearUsuario():
    usuario=input("Ingrese Usuario: ")
    contraseña=input("Ingrese Contraseña: ")

    return agregarUsuarioController([usuario, contraseña])

#Eliminar Usuario***************************
def eliminarUsuario():
    iduser=input("Seleccione Id Usuario a eliminar: ")
    return eliminarUsuariosController(iduser)

#Modificar Usuario **************************
def modificarUsuario(usuario):
    iduser=input("Seleccione Id Usuario a Modificar: ")

    for i in usuario:
        print (i["id"], iduser)
        # if str(i[])
