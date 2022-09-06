#Crea un html
import requests #pip install requests

url = "https://www.google.com/"

response = requests.get(url)

if response.status_code == 200:
    o = open("pagina.html", "w")
    o.write (response.content)
    o.close()