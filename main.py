
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

#SENTIMENT ANALYSIS FUNCTIONS
#Sentiment for episode and character

@app.route("/sentiment/<character>/<episode>")
def sentiment(character, episode):
    sentiment = sql.quote_sent(character, episode)
    return str(sentiment)

#Mean sentiment for episode and character

@app.route("/meansentiment/<character>/<episode>")
def meansentiment(character, episode):
    sentiment = sql.quote_sent(character, episode)
    m = sum(sentiment)/len(sentiment)
    return str(m)

#Sentiment for both character and one episode

@app.route("/sentiment/<character1>/<character2>/<episode>")
def doub_sentiment(character1, character2, episode):
    doub_sentiment = sql.quote_doublesent(character1, character2, episode)
    return doub_sentiment

#Mean sentiment both character and one episode

@app.route("/doublemeansentiment/<character1>/<character2>/<episode>")
def meansentiment2(character1, character2, episode):
    meansentiment2 = sql.quote_mdoublesent(character1, character2, episode)
    return meansentiment2

if __name__ == '__main__':
    app.run(debug=True)

