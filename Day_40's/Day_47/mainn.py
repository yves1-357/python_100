import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "lxml")
articles = soup.find(name="span", class_="a-price-whole")
article_text1 = articles.get_text().strip()

articlesSymbol = soup.find(name="span", class_="a-price-symbol")
article_text2 = articlesSymbol.get_text().strip()

articlesFraction = soup.find(name="span", class_="a-price-fraction")
article_text3 = articlesFraction.get_text()

articleFusion = article_text1 + article_text3
prix_final = float(articleFusion)


Prix_cible = 100
if prix_final > Prix_cible:
    print("Le prix est le meme ")
else:
    print(f"Alerte, le prix à baissé, il est à {prix_final}{article_text2}")
