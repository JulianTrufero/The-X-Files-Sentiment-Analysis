from config.config import engine
import pandas as pd

def choosecharacter(character):
    query = f"""
SELECT * FROM Characters
WHERE `Character` = '{character}'
"""
    datos = pd.read_sql_query(query,engine)

    return datos.to_json(orient="records")

def quote(episodenumber):
    query = f"""
SELECT * FROM Phrases
WHERE (Characters_idCharacters = 1 AND Episodes_idEpisodes = {int(episodenumber)})
"""
    datos = pd.read_sql_query(query,engine)

    return datos.to_json(orient="records")

