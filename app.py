from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

# Weather API Key
API_KEY = "fc05631c503bb4f632e2c952d2743290"
FORECAST_API_URL = "http://api.openweathermap.org/data/2.5/forecast"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    locations = [
        request.form.get("game1"),
        request.form.get("game2"),
        request.form.get("game3"),
    ]
    forecast_date = request.form.get("forecast_date")
    selected_date = datetime.strptime(forecast_date, "%Y-%m-%d")
    weather_data = []

    for location in locations:
        if location:
            params = {
                "q": location,
                "appid": API_KEY,
                "units": "imperial",  # Fahrenheit
            }
            response = requests.get(FORECAST_API_URL, params=params)
            if response.status_code == 200:
                forecast = response.json()
                forecasts_for_date = [
                    {
                        "time": datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%I:%M %p"),  # Format time
                        "temp": entry["main"]["temp"],
                        "description": entry["weather"][0]["description"],
                    }
                    for entry in forecast["list"]
                    if datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S").date() == selected_date.date()
                ]
                if forecasts_for_date:
                    weather_data.append({
                        "location": location,
                        "forecasts": forecasts_for_date,
                    })
                else:
                    weather_data.append({
                        "location": location,
                        "error": f"No forecast data available for {forecast_date}.",
                    })
            else:
                weather_data.append({
                    "location": location,
                    "error": f"Could not fetch forecast for {location}. Status code: {response.status_code}",
                })

    return render_template("results.html", weather_data=weather_data, forecast_date=forecast_date)

if __name__ == "__main__":
    app.run(debug=True)


