import requests


class OpenWeatherClient:
    def __init__(self, api_key):
        self.OPEN_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("API key must be a non null string")
        self.__api_key = value

    def fetch(self, city: str):
        try:
            response = requests.get(
                self.OPEN_WEATHER_URL,
                params={
                    "q": city,
                    "appid": self.api_key,
                    "units": "metric",
                    "lang": "us"
                },
                timeout=10
            )
            response.raise_for_status()
            return self._format(response.json())

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        return None

    @staticmethod
    def _format(data: dict) -> dict:
        weather = data.get("weather", [{}])[0]
        main = data.get("main", {})
        wind = data.get("wind", {})
        sys = data.get("sys", {})
        clouds = data.get("clouds", {})

        return {
            "name": data.get("name", "N/A"),
            "country": sys.get("country", "N/A"),
            "timezone": data.get("timezone", "N/A"),

            "temp": main.get("temp", "N/A"),
            "feels_like": main.get("feels_like", "N/A"),
            "temp_min": main.get("temp_min", "N/A"),
            "temp_max": main.get("temp_max", "N/A"),
            "pressure": main.get("pressure", "N/A"),
            "humidity": main.get("humidity", "N/A"),

            "description": weather.get("description", "N/A"),
            "weather_icon": weather.get("icon", "N/A"),
            "cloudiness": clouds.get("all", "N/A"),

            "wind_speed": wind.get("speed", "N/A"),
            "wind_deg": wind.get("deg", "N/A"),

            "visibility": data.get("visibility", "N/A"),

            "sunrise": sys.get("sunrise", "N/A"),
            "sunset": sys.get("sunset", "N/A"),

            "lon": data.get("coord", {}).get("lon", "N/A"),
            "lat": data.get("coord", {}).get("lat", "N/A")
        }
