from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def index():
    return "Hola Mundo"

@app.route('/chau')
def chau():
    return "Chau"

@app.route('/saludo/<nombre>/<apellido>')
def saludo(nombre, apellido):
    return f"Hola {nombre} {apellido}"

if __name__ == '__main__':
    app.run()
