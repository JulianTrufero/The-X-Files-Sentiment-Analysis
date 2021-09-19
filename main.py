
from flask import Flask, request
import src.sql_tools as sql

app = Flask(__name__)

#FRASES
#Phrases by episodes

@app.route("/phrasesbyepisode/<name>")
def phrase_by_epi(name):
    phrases = sql.quote_e(name)
    return phrases

#Phrases by character
@app.route("/phrasesbycharacter/<name>")
def phrase_by_charac(name):
    phrases = sql.quote_c(name)
    return phrases

#Phrases by character and episode
"""
@app.route("/phrases/<number>")
def phrases(character, episode):
    print('ok')
    phrase = sql.quote_ce(character, episode)
    return phrase
"""

if __name__ == '__main__':
    app.run(debug=True)

