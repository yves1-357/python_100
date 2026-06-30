import requests
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

# Créez vos objets
data_manager = DataManager("https://sheety.co")
flight_search = FlightSearch()


# On récupère la liste des lignes de votre tableau
sheet_data = data_manager.obtenir_données()
pprint(sheet_data)
