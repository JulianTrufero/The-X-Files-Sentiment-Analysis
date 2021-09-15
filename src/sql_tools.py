from config.config import engine
import pandas as pd

def damepersonaje(personaje):
    query = f"""
SELECT * FROM Characters
WHERE `Character` = '{personaje}'
"""
    datos = pd.read_sql_query(query,engine)

    return datos.to_json(orient="records")