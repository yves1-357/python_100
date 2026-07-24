import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="https://example.com",
        scope="playlist-modify-private playlist-modify-public",
        cache_path=".cache",
        show_dialog=True 
    )
)

# date = input(f"Quelle année voulez-vous voyager ? YYYY-MM-DD : " )
URL = "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=header)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "lxml")
articles = soup.find_all(name="h3",class_="chart-entry__title")
song_names_spans = soup.select("li ul li h3")
all_data = []
if articles is not None:
    for article in articles:
        data = {
            "text":article
        }

        article_text = article.get_text().strip()
        all_data.append(article_text)
    with open('music.txt', 'w', encoding='utf-8') as f:
        for music in all_data:
            f.write(f"{music}\n")

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
# year = date.split("-")[0]
for song in all_data:
    print(f"Recherche de : '{song}'")
    result = sp.search(q=f"track:{song}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} n'est pas disponible sur Spotify. Ignoré.")

print(song_uris)
nouvelle_playlist = requests.post(
    "https://api.spotify.com/v1/me/playlists",
    json={"name": "Travel Playlist", "public": False},
    headers={
        "Authorization": f"Bearer {sp.auth_manager.get_cached_token()['access_token']}",
        "Content-Type": "application/json"
    }
).json()

play_id = nouvelle_playlist["id"]
sp.playlist_add_items(playlist_id=play_id, items=song_uris)



#-------------------------------------------Debug--------------------------------------------
# Debug : appel direct sans spotipy
# token = sp.auth_manager.get_cached_token()
# print("Scopes actifs :", token["scope"])

# headers = {
#     "Authorization": f"Bearer {token['access_token']}",
#     "Content-Type": "application/json"
# }
# payload = {
#     "name": "Time Travel Playlist",
#     "public": False
# }

# r = requests.post(
#     "https://api.spotify.com/v1/me/playlists",  # ← /me/ au lieu de /users/{id}/
#     json=payload,
#     headers=headers
# )
# print("Status :", r.status_code)
# print("Réponse :", r.json())

#---------------------------------------------to be viewed later----------------------------------------
# nouvelle_playlist= sp.user_playlist_create(user=user_id, name="Time Travel Playlist",public=False)
# play_id = nouvelle_playlist["id"]
# sp.playlist_add_items(playlist_id=play_id ,items=song_uris)
# token = sp.auth_manager.get_cached_token()
# print("Scopes actifs :", token["scope"])


