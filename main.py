from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def index():
    return "Hola Mundo"
@app.route('/chau')
def chau():
    return "Chau"

app.run()