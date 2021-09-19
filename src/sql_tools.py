from config.config import engine
import pandas as pd

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

#Phrases by character

def quote_c(character):
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
