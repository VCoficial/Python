import requests, json

url = "http://127.0.0.1:3000/python"
datos = {
    "ID": "",
    "Nombre": "",
    "Celular": ""
}
headers = {
    "Conten-type": "application/json",
    "access-token": "123456"
}

# en caso de necesitar se puede cambiar put como metodo
response = requests.post(url, params = "", json = datos, headers = headers )

if response.status_code == 200:
    print (json.loads(response.content))


##************************************************************

def eliminarUsuariosController(iduser):
    url == ("\/"+id)

    response = requests.detelete(url)

    if response.status_code == 200:
        return json.loads(response.content)

##***********************************************************

def agregarUsuarioController(dato):
    datos = {
    "usuario": dato[1],
    "password": dato[2]
}
headers = {
    "Conten-type": "application/json",
    "access-token": "123456"
}

    # en caso de necesitar se puede cambiar put como metodo
    response = requests.post(url, params = "", json = datos, headers = headers)

    if response.status_code == 200:
        respuesta = (json.loads(response.content))

        return respuesta

def verUsuarioController():
    args={
        "ID":"",
        "Nombre":"",
        "Celular":""
    }

    response = requests.get(url, params = args)

if response.status_code == 200:
    print (json.loads(response.content))

        return datos 
    else:
        return{}


