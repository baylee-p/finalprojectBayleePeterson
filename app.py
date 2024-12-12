from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Weather API Key
API_KEY = "b7b5bc47cf926372433dcd763b4a417e"
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    data = request.json
    location = data.get("games", [])
    weather_data = []

    for location in location:
        params = {
            "q": location,
            "appid": API_KEY,
            "units": "imperial"
        }
        response = requests.get(WEATHER_API_URL, params=params)
        if response.status_code == 200:
            weather_data.append(response.json())

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)