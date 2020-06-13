from spotify_client import SpotifyAPI
from lyrics_scraper import ColorCodedLyrics

spotify = SpotifyAPI()
lyrics = ColorCodedLyrics(song_name = "", artist_name = "")

spotify.get_scopes()
spotify.auth_code = input("Enter Code: ")
spotify.perform_auth()
