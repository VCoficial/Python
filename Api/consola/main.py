from templates.crud import eliminarUsuario, modificarUsuario, crearUsuario, verUsuarios
from controllers.crudControllers import agregarUsuarioController, eliminarUsuariosController, verUsuarioController

usuarios=verUsuarios();

op = input("""Menu :

1.Eliminar
2.Modificar
3.Agregar

0.Salir

Opcion :""")

if op == "1":
        if eliminarUsuario():
            input("usuario eliminado correctamente")
        else:
            input("hubo un error al eliminar el usuario")
elif op == "2":
        if modificarUsuario(usuarios):
            input("Usuario modificado correctamente")
        else:
            input("hubo un error al eliminar el usuario")
elif op == "3":
        if crearUsuario():
            input("Usuario agregado correctamente")
        else:
            input("hubo un error al agregar el usuario")

