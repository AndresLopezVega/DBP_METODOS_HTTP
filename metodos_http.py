from flask import Flask
import json

def cargar_animes():
    with open('animes.json') as archivo_anime:
        datos_animes = json.load(archivo_anime)
    return datos_animes

def obtener_info_animes():
    animes = cargar_animes()
    info = ""
    for anime in animes:
        info += "Título: {}<br>".format(anime["titulo"])
        info += "Puntaje: {}<br>".format(anime["puntaje"])
        info += "Tipo: {}<br>".format(anime["tipo"])
        info += "Temporada: {}<br>".format(anime["season"])
        info += "Géneros: {}<br><br>".format(", ".join(anime["generos"]))
    return info

def obtener_info_animes_id(ID):
    animes = cargar_animes()
    info = ""
    for anime in animes:
        if anime["id"]==ID:
            info += "Título: {}<br>".format(anime["titulo"])
            info += "Puntaje: {}<br>".format(anime["puntaje"])
            info += "Tipo: {}<br>".format(anime["tipo"])
            info += "Temporada: {}<br>".format(anime["season"])
            info += "Géneros: {}<br><br>".format(", ".join(anime["generos"]))
   
    return info


app = Flask(__name__)

"""METODO GET"""
@app.route("/anime", methods=["GET"])
def animes():
    info = obtener_info_animes()
    return info

"""METODO GET ID"""

@app.route("/anime/<int:id>",methods=["GET"])

def anime_id(id):
    info_ID=obtener_info_animes_id(id)
    return info_ID



"""METODO POST"""

"""METODO PUT"""

"METODO DELETE"

if __name__ == "__main__":
    app.run()
