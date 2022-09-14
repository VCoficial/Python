from controller.post import agregar
from controller.post import actualizarUsuario
from controller.post import eliminarUsuario
from controller.post import miraruno



def crearUsuarios ():

     nombre=input("ingrese nombre: ")
     Telefono=input("ingrese telefono: ")
    

     return agregar([nombre,Telefono])


def eliminar():
     id =input("Seleccione el id a eliminar: ")
     return eliminarUsuario(id)

def buscar():
     id =input("Seleccione el id : ")
     return miraruno(id)


""" def editarUsuario():
     iduser = input("Seleccione el usuario a editar: ")
     for i in :
          print (i["id"], iduser)
          if str(i["id"]) ==iduser:
               nombre = input("Modificar nombre"+i["nombre"]+"por: ")
               Telefono = input("Modificar telefono"+i["Telefono"]+"por: ")
               return actualizarUsuario([nombre,Telefono,iduser]) """






