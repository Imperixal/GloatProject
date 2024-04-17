import requests


class WeatherAPI:
    BASE_URL = "http://api.openweathermap.org/geo/1.0/zip"
    FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"
    API_KEY = "95f2538884d4510ad89341c61de60918"

    def __init__(self, zip_code, country='US'):
        self.zip_code = zip_code
        self.country = country

    def get_geolocation(self):
        params = {
            'zip': f"{self.zip_code},{self.country}",
            'appid': self.API_KEY
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()

    def get_forecast(self, lat, lon):
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.API_KEY,
            'units': 'metric',
            'count': 16
        }
        response = requests.get(self.FORECAST_URL, params=params)
        response.raise_for_status()
        return response.json()
