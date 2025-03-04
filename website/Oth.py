#Main page links
import requests
from flask import Flask
from flask import Blueprint, render_template, request


#Authentication links

Oth = Blueprint('Oth',__name__)

def get_weather_data(cityoption)

    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    api_key = "f22d7397d3b69de53f3df6ae2d87946e"
    url = f"{base_url}{cityoption}&appid={api_key}"

    response = requests.get(url).json()

    return response

@Oth.route('/', methods=["POST","GET"])   # Focus here
def Home():
    if request.method == 'POST':
    


        




        return render_template('home.html')
    
    return render_template('home.html')