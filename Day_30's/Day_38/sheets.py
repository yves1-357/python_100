import os
import requests
from datetime import datetime

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
Sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

if not APP_ID or not API_KEY or not Sheety_endpoint:
    raise ValueError(
        "Set NUTRITIONIX_APP_ID, NUTRITIONIX_API_KEY and SHEETY_ENDPOINT "
        "as environment variables."
    )

Nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

user_params = {
    "query": "swam for 1 hour",
    "weight_kg": 70,                  
    "height_cm": 175,                
    "age": 30,                       
    "gender": "male",
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=Nutrition_endpoint, json=user_params, headers=headers)
data = response.json()  
nom_exercice = data["exercises"][0]["name"]
duree_exercice = data["exercises"][0]["duration_min"]
calories_exercice = data["exercises"][0]["nf_calories"]

moment_actuel = datetime.now()
today_date = moment_actuel.strftime("%d/%m/%Y")
today_hour = moment_actuel.strftime("%H:%M:%S")
# Exemple si la feuille s'appelle "workout"
donnees_sheet = {
    "sheet1": {
        "date": today_date, # Vous pouvez mettre du texte brut pour tester
        "time": today_hour,
        "exercise": nom_exercice.title(), # Rend la première lettre majuscule
        "duration": duree_exercice,
        "calories": calories_exercice
    }
}
response_sheety = requests.post(url=Sheety_endpoint, json=donnees_sheet)
print(response_sheety)

