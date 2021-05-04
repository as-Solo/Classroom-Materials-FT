from config.configuration import db, collection

print (''' 
-------------------------------------------------------------------------
-------------------------------------------------------------------------
GETDATA EJECUTÁNDOSE
-------------------------------------------------------------------------
-------------------------------------------------------------------------
''')


def mensaje_personajes(personaje):
    query = {"character_name" : f'{personaje}'}
    frases = list(collection.find(query, {"_id" : 0}))
    return frases

def mensaje_personaje():
    query = {"character_name" : 'Albus Dumbledore'}
    frases = list(collection.find(query, {"_id" : 0}))
    return frases