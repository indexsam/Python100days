#!/usr/bin/env python

import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials


import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_SECRET_ID"),
        show_dialog=True,
        cache_path="token.txt",
        username="Sam", 
    )
)

user_id = sp.current_user()["id"]

#-------------step 2-------------------

date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ").strip()

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")

songs = soup.select("li ul li h3")
song_names = [title.getText().strip() for title in songs]


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print("Final list created ...!!")
# print(song_uris)

#-----final step --------

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"playlist created in Spotify for used ID: {user_id}")
