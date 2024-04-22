import config
import time
import re
import pyperclip
import requests
from base64 import b64encode

def get_spotify_access_token():
    # Obtain the access token from Spotify
    credentials = f"{config.SPOTIFY_CLIENT_ID}:{config.SPOTIFY_CLIENT_SECRET}"
    encoded_credentials = b64encode(credentials.encode()).decode('utf-8')
    auth_url = "https://accounts.spotify.com/api/token"
    auth_headers = {"Authorization": f"Basic {encoded_credentials}"}
    auth_data = {"grant_type": "client_credentials"}
    response = requests.post(auth_url, headers=auth_headers, data=auth_data)
    return response.json().get('access_token')

def fetch_youtube_details(video_id):
    youtube_api_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={config.YOUTUBE_API_KEY}"
    response = requests.get(youtube_api_url)
    response_json = response.json()
    if response_json.get('items', []):
        title = response_json['items'][0]['snippet']['title']
        return title
    return None

def search_spotify(track_name, spotify_token):
    headers = {'Authorization': f'Bearer {spotify_token}'}
    params = {'q': track_name, 'type': 'track', 'limit': 1}
    spotify_search_url = "https://api.spotify.com/v1/search"
    response = requests.get(spotify_search_url, headers=headers, params=params)
    response_json = response.json()
    if response_json.get('tracks', {}).get('items'):
        spotify_url = response_json['tracks']['items'][0]['external_urls']['spotify']
        return spotify_url
    return None

def watch_clipboard():
    spotify_access_token = get_spotify_access_token()
    previous_clipboard = pyperclip.paste()
    while True:
        time.sleep(1)
        current_clipboard = pyperclip.paste()
        if current_clipboard != previous_clipboard:
            video_id_match = re.search(r"(?<=v=)[^&#]+", current_clipboard) or re.search(r"(?<=youtu.be/)[^&#]+", current_clipboard)
            if video_id_match:
                video_id = video_id_match.group(0)
                track_name = fetch_youtube_details(video_id)
                if track_name:
                    spotify_url = search_spotify(track_name, spotify_access_token)
                    if spotify_url:
                        pyperclip.copy(spotify_url)
                        print(f"Spotify link copied to clipboard: {spotify_url}")
            previous_clipboard = current_clipboard

if __name__ == "__main__":
    watch_clipboard()
