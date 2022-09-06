#Descarga una imagen
import requests, json
url = "https://www.purina-latam.com/sites/g/files/auxxlc391/files/styles/kraken_generic_max_width_960/public/01_%C2%BFQu%C3%A9-puedo-hacer-si-mi-gato-est%C3%A1-triste-.png?itok=cOA5aYW-"

response = requests.get (url, stream = True) # stream deja la conexion abierta

file = open("imagen.jpg", "wb")
# ciclo for para descargar el contenido
for i in response.iter_content():
    file.write(i)
file.close()
response.close()