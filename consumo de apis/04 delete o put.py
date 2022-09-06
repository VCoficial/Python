import requests, json
id = "36"
url = "http://127.0.0.1:3000/api/usuarios/"+id

headers = {
    "Conten-type": "application/json"
}

# en caso de necesitar se puede cambiar put como metodo
response = requests.delete(url)
print(response)
if response.status_code == 200:
    print (json.loads(response.content))