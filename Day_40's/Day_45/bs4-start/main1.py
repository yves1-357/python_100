from  bs4 import BeautifulSoup 
import requests
import lxml

# response = requests.get("https://quotes.toscrape.com")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "lxml")
# article_tag = soup.find(name="span", class_="text")
# article_text = article_tag.get_text()
# print(article_text)

response = requests.get("https://quotes.toscrape.com")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "lxml")
articles = soup.find_all(name="span", class_="text")
all_data = []
if articles is not None:
    for article in articles:
        data = {
            "text": article
            
        }

        article_data = article.get_text()
        all_data.append(article_data)

print(all_data)

















# from  bs4 import BeautifulSoup 
# import requests
# import lxml

# response = requests.get("https://news.ycombinator.com/")

# yc_web_page = response.text 

# soup = BeautifulSoup(yc_web_page, "lxml")
# article_tag = soup.find(name="a", class_="storylink")
# article_text = article_tag.get_text()
# print(article_text)

#  La règle d'or.
# find() (Un seul élément) : 
# Cherche le tout premier tag qui correspond à vos critères. 
# Dès qu'il le trouve, il s'arrête.Type renvoyé : 
# Un objet Tag unique.Action : Vous pouvez directement lui appliquer .get_text() ou récupérer un attribut.
# .find_all() (Une collection d'éléments) : '
# 'Parcourt tout le document pour récupérer absolument toutes les correspondances.Type renvoyé : '
# 'Une liste d'objets.Action : Vous ne pouvez pas faire .get_text() directement sur le résultat.
#  Vous devez obligatoirement faire une boucle for pour traiter les éléments un par un.


# # Trouver le titre principal du site (généralement unique)
# titre = soup.find(name="h1")
# print(titre.get_text()) # Fonctionne directement !

# # Trouver le tout premier lien de la page
# premier_lien = soup.find(name="a")
# print(premier_lien["href"]) # Extrait l'adresse URL





























# from  bs4 import BeautifulSoup 
# import lxml
# with open ('website.html', 'r', encoding='utf-8') as fichier:
#     contents = fichier.read()

# soup = BeautifulSoup(contents, "lxml")
# print(soup.title)

# #html.parser = on peux utiliser lxml ( beautiful soup markup )