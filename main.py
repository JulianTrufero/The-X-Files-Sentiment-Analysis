
from flask import Flask, request
import src.sql_tools as sql

app = Flask(__name__)

#FRASES
#Todas las frases, 
#frases por episodio

@app.route("/phrasesbyepisode/<name>")
def phrase_by_epi(name):
    phrases = sql.quote_e(name)
    return phrases

#frases por personaje
@app.route("/phrasesbycharacter/<name>")
def phrase_by_charac(name):
    phrases = sql.quote_c(name)
    return phrases

#frases por personaje y episodio
"""
@app.route("/phrases/<number>")
def phrases(character, episode):
    print('ok')
    phrase = sql.quote_ce(character, episode)
    return phrase
"""

if __name__ == '__main__':
    app.run(debug=True)

