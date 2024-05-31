from flask import Flask

app = Flask(__name__)

@app.route('/saludo/<Naiara>')
def saludo(Naiara):
    return f"hola {Naiara}"

if __name__ == '__main__':
    app.run(debug=True, port=3000)