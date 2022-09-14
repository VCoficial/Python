from http.client import GATEWAY_TIMEOUT
import requests, json

url = "http://127.0.0.1:5000/api/usuarios"

def mirarapi ():
    response = requests.get(url)

    if response.status_code == 200:
   
   
        print (json.loads(response.content))

url2="http://127.0.0.1:5000/api/usuarios/"
def miraruno (id):
    gato= url2+id
    response = requests.get(gato)
    if response.status_code == 200:
        print (json.loads(response.content))
        """ return sl==(json.loads(response.content)) """

