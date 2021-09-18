
from flask import Flask, request
import src.sql_tools as sql

app = Flask(__name__)

@app.route("/")
def inicial():
    return "hola mundo"

@app.route("/character/<name>")
def personaje(name):
    print(name)
    personaje = sql.choosecharacter(name)
    return personaje

#FRASES
#Todas las frases, frases por episodio, frases por personaje, 

@app.route("/phrases/<number>")
def phrases(number):
    print(number)
    phrase = sql.quote(number)
    return phrase


if __name__ == '__main__':
    app.run(debug=True)

