import os
import stock_data
import requests
from twilio.rest import Client

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_PHONE_NUMBER")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

if not all([ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, MY_NUMBER, NEWS_API_KEY]):
    raise ValueError(
        "Set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER, "
        "MY_PHONE_NUMBER and NEWS_API_KEY as environment variables."
    )

client = Client(ACCOUNT_SID, AUTH_TOKEN)

donnes_brutes = stock_data.data

data_quotidien = donnes_brutes["Time Series (Daily)"]

ma_liste = list(data_quotidien.values())

# TODO_1
prix_hier = float(ma_liste[0]['4. close'])

# TODO_2
prix_avant_hier = float(ma_liste[1]['4. close'])

# TODO_3
difference_brute = abs(prix_hier - prix_avant_hier)
print(difference_brute)

# TODO_4
difference_pourcentage = (difference_brute / prix_hier) * 100

# TODO_5 and TODO_6
if difference_pourcentage > 1:
    print('Get News ')
    parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "searchIn": COMPANY_NAME,
    }


    response = requests.get(NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    # print(f"code HTTP : {response.status_code}")
    # print(f"Contenu reçu : {response.text[:300]}")


    data_news = response.json()

# TODO_7
    liste_articles = data_news['articles'][:3]

# TODO_8
    message_list = [
    f"Headline: {article['title']}\nBrief: {article['description']}"
    for article in liste_articles]

# TODO_9
    for message_unique in message_list:
        message = client.messages.create(
             body=message_unique,
             from_=TWILIO_NUMBER,
             to=MY_NUMBER
        )
        print(message.status)