import SpotifyAPI from spotify_client.py
import ColorCodedLyrics from lyrics_scraper.py

spotify = SpotifyAPI(client_id = client_id, client_secret = client_secret)

spotify.get_scopes()
spotify.auth_code = input("Enter Code: ")
spotify.perform_auth()
