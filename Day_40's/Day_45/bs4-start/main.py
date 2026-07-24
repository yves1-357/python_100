import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "lxml")
articles = soup.find_all(name="h3", class_="title")
all_data = []
if articles is not None:
    for article in articles:
        data = {
            "text":article
        }

        article_text = article.get_text()
        all_data.append(article_text)
    data_inverser = all_data[::-1]
    with open('movies.txt', 'w', encoding='utf-8') as f:
        for movie in data_inverser:
            f.write(f"{movie}\n")







# print(soup.prettify) pour voir contenu du html 
# all_data = []
# if articles is not None:
#     for article in articles:
#         data = {
#             "text": article
            
#         }

#         article_data = article.get_text()
#         all_data.append(article_data)

# print(all_data)



# response = requests.get("https://quotes.toscrape.com")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "lxml")
# article_tag = soup.find(name="span", class_="text")
# article_text = article_tag.get_text()
# print(article_text)