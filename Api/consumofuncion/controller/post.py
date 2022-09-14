import requests, json
from controller.get import miraruno


url = "http://127.0.0.1:5000/api/registrarUsuario"

def agregar (data):
    datos = {  
        'nombre':data[0],
        'Telefono':data[1]
        
    }

# en caso de necesitar se puede cambiar put como metodo
    response = requests.post(url, json = datos )
    print (response.url)

    if response.status_code == 200:
        return (json.loads(response.content))



def actualizarUsuario():
    
    id = input("seleccione el id a modificar: ")
    if id != "":
         data = miraruno(id)
    print (data)

    nombre=input("ingrese nombre: ")
    Telefono=input("ingrese telefono: ")

    datos = {
                'id' : id,
                'nombre':nombre,
                'Telefono':Telefono 
        
        }

    
    response = requests.post(url, json = datos )
    
    if response.status_code == 200:
        return (json.loads(response.content))

    

def eliminarUsuario (id):
    
    gato= "http://127.0.0.1:5000/api/usuarios/"+id
    print (gato)

    response = requests.delete(gato)

    if response.status_code == 200:
     return (json.loads(response.content)) 

        