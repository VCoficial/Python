from http import cookies
import requests

url = "http://127.0.0.1:3000/api/usuarios"
cookies = {
    "nombre": "julio",
    "curso": "Python"
}

response = requests.get(url, cookies= cookies)
print (response.url)

if response.ok:
    print ("contenido: ")
    print (response.content)