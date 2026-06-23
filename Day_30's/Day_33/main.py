import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 51.507351
MY_LONG = -0.127758

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL", MY_EMAIL)


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (
        MY_LAT - 10 <= iss_latitude <= MY_LAT + 10
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    )


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    return time_now >= sunset or time_now <= sunrise


def send_email():
    if not MY_EMAIL or not MY_PASSWORD:
        print("Identifiants email manquants (MY_EMAIL / MY_PASSWORD).")
        return
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky.",
        )


while True:
    time.sleep(60)
    try:
        if is_iss_overhead() and is_night():
            send_email()
            print("Email envoye : regarde le ciel !")
    except requests.exceptions.RequestException as e:
        print(f"Erreur API : {e}")



