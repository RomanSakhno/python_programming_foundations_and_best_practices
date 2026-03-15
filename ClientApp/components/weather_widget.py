# ClientApp/components/weather_widget.py
import requests

WEATHER_ICONS = {
    0: "☀️", 1: "🌤", 2: "⛅", 3: "☁️",
    45: "🌫", 48: "🌫",
    51: "🌦", 53: "🌦", 55: "🌧",
    56: "🌧❄️", 57: "🌧❄️",
    61: "🌧", 63: "🌧", 65: "🌧🌩",
    66: "🌧❄️", 67: "🌧❄️",
    71: "❄️", 73: "❄️", 75: "❄️",
    77: "❄️",
    80: "🌦", 81: "🌦", 82: "🌧",
    85: "❄️", 86: "❄️",
    95: "⛈", 96: "⛈", 99: "⛈"
}


def render_weather(lat: float, lon: float) -> str:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()

        if "current_weather" not in data:
            return "<p style='font-size:12px;'>Weather info not available</p>"

        weather = data["current_weather"]
        temp = weather["temperature"]
        wind = weather.get("windspeed", 0)
        code = weather.get("weathercode", 0)
        desc = WEATHER_ICONS.get(code, "❔")  # иконка
        weather_text_map = {
            0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Rime fog",
            51: "Drizzle", 53: "Drizzle", 55: "Dense drizzle",
            56: "Freezing drizzle", 57: "Freezing drizzle",
            61: "Rain", 63: "Rain", 65: "Heavy rain",
            66: "Freezing rain", 67: "Freezing rain",
            71: "Snow", 73: "Snow", 75: "Heavy snow",
            77: "Snow grains",
            80: "Rain showers", 81: "Rain showers", 82: "Violent rain showers",
            85: "Snow showers", 86: "Snow showers",
            95: "Thunderstorm", 96: "Thunderstorm hail", 99: "Thunderstorm hail"
        }
        text_desc = weather_text_map.get(code, "Unknown")

        html = f"""
        <div style="display:flex; justify-content:flex-end;">
            <div style="
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 8px;
                background-color: #f0f0f0;
                text-align: center;
                font-family: sans-serif;
                font-size: 12px;
                width:120px;
            ">
                <div style="font-size:20px;">{desc}</div>
                <strong>{temp}°C</strong><br>
                {text_desc}<br>
                Wind: {wind} km/h
             </div>
        </div>
        """
        return html

    except Exception as e:
        return f"<p style='font-size:12px;'>Error loading weather: {e}</p>"