import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = '49293b5a02efce8b20b02f71dc3f9f49'
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None
    icon_url = ""
    if request.method == 'POST':
        city = request.form['city']
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(WEATHER_URL, params=params)
        if response.ok:
            weather = response.json()
            icon_code = weather['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"



    return render_template('index.html', weather=weather, icon_url=icon_url)



if __name__ == '__main__':
    app.run(debug=True)