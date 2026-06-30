import requests
class DataManager:
    def __init__(self, base_url):
        self.base_url = base_url

    def obtenir_données(self):
        response = requests.get(self.base_url, timeout=5)
        response.raise_for_status()

        return response.json()["sheet1"]
    
    
api = DataManager("https://api.sheety.co/b965736e47a41799bef6705470f3ed28/travel/sheet1")
data = api.obtenir_données()

        