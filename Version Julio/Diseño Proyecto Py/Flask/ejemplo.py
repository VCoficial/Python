from flask import Flask  #importamos Flask

app = Flask(__name__)  #creamos un objeto

@app.route('/')  #wrap o decorador
def index():
    return "hola mundo gatico"

@app.route("/contacto")
@app.route("/contactos")
@app.route("/contactame")
def contacto():
    return "pato"

if __name__ == '__main__':  #lanzador del servidor
    app.run(debug=True, port=8080)  #El modo debug es el modo administrador