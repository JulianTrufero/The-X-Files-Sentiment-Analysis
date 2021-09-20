from config.config import engine
import pandas as pd
from nltk.corpus import stopwords
import re
import string
import spacy
from textblob import TextBlob

#General check function
def check(something,string):
    """
    """
    if something == "episode":
        query = list(engine.execute(f"SELECT Episode FROM Episodes WHERE Episode = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif something == "character":
        query = list(engine.execute(f"SELECT `Character` FROM Characters WHERE `Character` = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
    
    elif something == "phrase":
        query = list(engine.execute(f"SELECT Phrase FROM Phrases WHERE Phrase = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False

#Tokenize and polarity functions 

def tokenizer(txt):
    """
    """
    nlp = spacy.load("en_core_web_sm")
    tokens = nlp(txt)
    filtradas = []
    
    for word in tokens:
        if not word.is_stop:
            lemma = word.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma):
                filtradas.append(lemma)
            
    return " ".join(filtradas)

def polarity(phrase):
    """
    """
    blob = TextBlob(f"{phrase}")
    
    return blob.sentiment[0]

#Phrases by character

def quote_c(character):
    """
    """
    if check('character', character):
        query = list(engine.execute(f"SELECT idCharacters FROM Characters WHERE `Character` = '{character}'"))
        c = query[0][0]
    else: 
        return "The character doesn't exist or match with the ones in the db"
    
    query = f"""
    SELECT * FROM Phrases
    WHERE (Characters_idCharacters = {c})
    """
    datos = pd.read_sql_query(query,engine)

    return datos.to_json(orient="records")

#Phrases by episode

def quote_e(episode):
    """
    """
    if check('episode', episode):
        query = list(engine.execute(f"SELECT idEpisodes FROM Episodes WHERE Episode = '{episode}'"))
        e = query[0][0]
    else: 
        return "The episode doesn't exist or match with the ones in the db"
    
    query = f"""
    SELECT * FROM Phrases
    WHERE (Episodes_idEpisodes = {e})
    """
    datos = pd.read_sql_query(query,engine)
    
    return datos.to_json(orient="records")


#Phrases by character and episode

def quote_ce(character, episode):
    """
    """
    if check('character', character):
        query = list(engine.execute(f"SELECT idCharacters FROM Characters WHERE `Character` = '{character}'"))
        c = query[0][0]
    else: 
        return "The character doesn't exist or match with the ones in the db"
    
    if check('episode', episode):
        query = list(engine.execute(f"SELECT idEpisodes FROM Episodes WHERE Episode = '{episode}'"))
        e = query[0][0]
    else: 
        return "The episode doesn't exist or match with the ones in the db"
    
    query = f"""
    SELECT * FROM Phrases
    WHERE (Characters_idCharacters = {c} AND Episodes_idEpisodes = {e})
    """
    datos = pd.read_sql_query(query,engine)
    
    return datos.to_json(orient="records")

#Insert phrase

def insertphrase(episode,character,phrase):
    """
    """
    if check('episode', episode) == False:
        engine.execute(f""" INSERT INTO Episodes (Episode) VALUES ('{episode}'); """)
        
        if check('character', character) == False:
            engine.execute(f""" INSERT INTO Characters (`Character`) VALUES ('{character}'); """)
        
        query = list(engine.execute(f"SELECT idCharacters FROM Characters WHERE `Character` = '{character}'"))
        c = query[0][0]
        query = list(engine.execute(f"SELECT idEpisodes FROM Episodes WHERE Episode = '{episode}'"))
        e = query[0][0]
        
        engine.execute(f""" INSERT INTO Phrases (Phrase, Characters_idCharacters, Episodes_idEpisodes) 
                            VALUES ("{phrase}", {c}, {e});""")
    else:
        return 'This episode already exists'
        
    return f"The phrase has been correctly included in the db: {episode},{character},{phrase}"

#Modify phrase

def modifyphrase(episode,character,phrase,modification):
    """
    """
    
    if check('episode', episode):
        if check('character', character):
            if check('phrase', phrase):
                query = list(engine.execute(f"SELECT idPhrases FROM Phrases WHERE Phrase = '{phrase}'"))
                p = query[0][0]
                engine.execute(f""" UPDATE Phrases
                                    SET Phrase = '{modification}'
                                    WHERE idPhrases = {p} ;""")
            else:
                return 'This phrase doesn`t exist'
        else:
            return 'This character doesn`t exist'
    else:
        return 'This episode doesn`t exist'
        
    return f"The phrase has been correctly modified in the db: {episode},{character},{modification}"

#SENTIMENT ANALYSIS FUNCTIONS
#Sentiment for episode and character

def quote_sent(character, episode):
    """
    """
    if check('character', character):
        query = list(engine.execute(f"SELECT idCharacters FROM Characters WHERE `Character` = '{character}'"))
        c = query[0][0]
    else: 
        return "The character doesn't exist or match with the ones in the db"
    
    if check('episode', episode):
        query = list(engine.execute(f"SELECT idEpisodes FROM Episodes WHERE Episode = '{episode}'"))
        e = query[0][0]
    else: 
        return "The episode doesn't exist or match with the ones in the db"
    
    query = f"""
    SELECT * FROM Phrases
    WHERE (Characters_idCharacters = {c} AND Episodes_idEpisodes = {e})
    """
    datos = pd.read_sql_query(query,engine)

    polarities = []
    for i in datos['Phrase']:
        t = tokenizer(i)
        p = polarity(t)
        polarities.append(p)
        
    return polarities
    
#Sentiment for both character and one episode

def quote_doublesent(character1, character2, episode):
    """
    """
    s_1 = quote_sent(character1, episode)
    s_2 = quote_sent(character2, episode)
    double = {f'{character1}': s_1, f'{character2}': s_2}

    """
    double[f'{character1}'] = s_1
    double[f'{character2}'] = s_2
    """
    return double

#Mean sentiment for both character and one episode

def quote_mdoublesent(character1, character2, episode):
    """
    """
    s_1 = quote_sent(character1, episode)
    s_2 = quote_sent(character2, episode)
    m_1 = sum(s_1)/len(s_1)
    m_2 = sum(s_2)/len(s_2)

    double = {}
    double[f'{character1}'] = m_1
    double[f'{character2}'] = m_2
    
    return double