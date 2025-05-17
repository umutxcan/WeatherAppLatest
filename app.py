from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "1fc1663091f04a172c005b8a1559a99b" # OpenWeatherMap API key

@app.route("/")
def index():
    return "Ad Soyad: Fatih Terim"

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Şehir belirtilmedi"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "Şehir bulunamadı"}), 404

    data = response.json()
    weather_description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    return jsonify({
        "sehir": city,
        "hava": weather_description,
        "nem": f"%{humidity}"
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
