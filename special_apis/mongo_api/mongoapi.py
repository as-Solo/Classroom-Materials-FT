from flask import Flask, request
<<<<<<< HEAD
import tools.getdata as get
import tools.postdata as post
import json
from flask import jsonify
import markdown.extensions.fenced_code

#json.encode(analytics, cls=JSONEncoder)

app = Flask(__name__)



@app.route('/')
def index():
    readme_file = open('Readme.md', 'r')
    ms_template = markdown.markdown(readme.file.read(), extensions = ['fenced_code'])

=======
from flask import jsonify
import json
import markdown.extensions.fenced_code
import tools.getdata as get
import tools.postdata as pos




app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f


@app.route("/frases")
def frases():
<<<<<<< HEAD
    frases = get.mensaje_personaje()
    #print (frases)
    return jsonify(frases)


@app.route("/frases/<name>")
def frases_p(name):
    frases = get.mensaje_personajes(name)
    #print (frases)
    return jsonify(frases)


# De normal, flask entiende que por defecto el método es Get, pero si queremos hacer un 'formulario' tenemos que definir el método como POST
@app.route('/nuevafrase', methods = ['POST'])
def insertmensaje():
    escena = request.form.get('scene')
    personajes = request.form.get('character_name')
    frase = request.form.get('dialogue')
    post.inserta_mensaje(escena, personaje, frase)
    return 'Gracias por tu frase, ya eres libre.'
=======
    frases = get.mensajes()
    return jsonify(frases)



@app.route("/frases/<name>")
def frasespersonaje(name):
    frases = get.mensajespersonaje(name)
    return jsonify(frases)


@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    escena = request.form.get("scene")
    personaje = request.form.get("character_name")
    frase = request.form.get("dialogue")
    pos.insertamensaje(escena, personaje, frase)
    return "Se ha introducido el mensaje en la base de datos"
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f







<<<<<<< HEAD
app.run('localhost', '5000', debug = True)
=======
app.run("0.0.0.0", 5000, debug=True)
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
