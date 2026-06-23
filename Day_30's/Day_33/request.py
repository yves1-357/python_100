import requests
from datetime import datetime
# response = requests.get(url ="http://api.open-notify.org/iss-now.json")
# print(response )
MY_Lat = " 50.634140"
MY_long = "4.610670"
my_format ="0"

parameters ={
    "lat":MY_Lat,
    "lng": MY_long,
    "formatted": my_format
    }
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T"))

time_now = datetime.now()