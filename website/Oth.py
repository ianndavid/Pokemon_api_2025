#Main page links
import requests
from flask import Flask
from flask import Blueprint, render_template, request


#Authentication links

Oth = Blueprint('Oth',__name__)

def get_pokemon_data(pokemonname):
    get_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonname}")

    return get_response

@Oth.route('/', methods=["POST","GET"])   # Focus here
def Home():
    if request.method == 'POST':
    
        pokemonname = request.form.get("Poke-name")

        




        return render_template('home.html')
    
    return render_template('home.html')