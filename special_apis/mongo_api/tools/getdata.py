from config.configuration import db, collection

<<<<<<< HEAD
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
=======

def mensajes():
    """
    Función que devuelve todas las frases de Dumbledore :)
    """
    query = {"character_name": "Albus Dumbledore"}
    frases = list(collection.find(query,{"_id": 0}))
    return frases



def mensajespersonaje(personaje):
    """
    Función que devuelve todas las frases un personaje
    """
    query = {"character_name": f"{personaje}"}
    frases = list(collection.find(query,{"_id": 0}))
    return frases

>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
