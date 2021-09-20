
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

@app.route("/phrases/<character>/<episode>")
def phrases(character, episode):
    print('ok')
    phrase = sql.quote_ce(character, episode)
    return phrase


#Insert phrase

@app.route("/newphrase", methods=["POST"])
def newphrase():
    phrase = request.form.get("phrase")
    character = request.form.get("character")
    episode = request.form.get("episode")

    return sql.insertphrase(episode,character,phrase)

#Modify phrase

@app.route("/modphrase", methods=["POST"])
def modphrase():
    phrase = request.form.get("phrase")
    character = request.form.get("character")
    episode = request.form.get("episode")
    modification = request.form.get("modification")

    return sql.modifyphrase(episode,character,phrase,modification)

if __name__ == '__main__':
    app.run(debug=True)

