import requests, json

url = "http://127.0.0.1:3000/api/usuarios"
datos = {
    "usuario": "julio",
    "password": "Python"
}
headers = {
    "Conten-type": "application/json",
    "access-token": "123456"
}

# en caso de necesitar se puede cambiar put como metodo
response = requests.post(url, params = "", json = datos, headers = headers)
print (response.url)

if response.status_code == 200:
    print (json.loads(response.content))