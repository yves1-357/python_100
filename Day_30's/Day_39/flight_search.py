import requests

class FlightSearch:
    def __init__(self):
        self.codes_simules = {
            "Paris": "PAR",
            "Berlin": "BER",
            "New-York": "NYC",
            "Stockholm": "STO",
            "Milan": "MIL",
            "Boston": "BOS",
            "Bali": "DPS",
            "Tokyo": "TYO"
        }

    def get_destination_code(self, city_name):
        nom_propre = city_name.strip()

        return self.codes_simules.get(nom_propre, "N/A")
