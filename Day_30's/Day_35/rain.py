import os
import requests

API_KEY = os.environ.get("OWM_API_KEY")
if not API_KEY:
    raise ValueError("Set OWM_API_KEY as an environment variable.")

parameters = {
    "lat": 50.634140,
    "lon": 4.610670,
    "appid": API_KEY,
    "cnt": 4,
}
# URL = "api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}"
URL = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(URL, params=parameters)
print(response.json())
