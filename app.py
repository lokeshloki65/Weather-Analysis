from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "299f7e5492f50649ab43582bb6c3e279"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.json['city'].strip().title()  # Formatting the input
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200 or "main" not in response.json():
        return jsonify({"error": "City not found in API"}), 404

    data = response.json()
    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["main"],
        "wind_speed": data["wind"]["speed"]
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
