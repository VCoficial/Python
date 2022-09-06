import requests, json

url = "http://127.0.0.1:3000/api/usuarios"
args = {
    "nombre": "julio",
    "curso": "Python"
}

response = requests.get(url, params = args)
print (response.url)

if response.status_code == 200:
    print (json.loads(response.content))