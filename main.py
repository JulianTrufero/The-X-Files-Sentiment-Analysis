
from flask import Flask, request
import src.sql_tools as sql

app = Flask(__name__)

@app.route("/")
def inicial():
    return "hola mundo"

@app.route("/personajes/<name>")
def personaje(name):
    print(name)
    personaje = sql.damepersonaje(name)
    return personaje

if __name__ == '__main__':
    app.run(debug=False)

