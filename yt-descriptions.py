import json
import os.path
import sys
from datetime import datetime
from typing import List, Dict

from yt_dlp import YoutubeDL


def get_iso_date():
    return datetime.now().isoformat().replace(":", "-")


def get_playlist_path(playlist_: Dict[str, str]) -> str:
    return os.path.join('descriptions', playlist_['title'])


logs_file_path = f'{get_iso_date()}_{os.path.basename(__file__)}.log'
sys.stdout = open(logs_file_path, 'w')  # python redirect stdout to file -> https://stackoverflow.com/a/4675744/17299754
playlists: List[Dict[str, str]] = json.load(open('input.json', 'r'))

for idx, playlist in enumerate(playlists):
    print(f"Processing playlist {idx + 1}/{len(playlists)}: {playlist['title']}")
    ydl_options = {'cookiesfrombrowser': ('chrome', None, None, None), 'skip_download': True, 'writedescription': True,
                   'paths': {'home': get_playlist_path(playlist)}}
    with YoutubeDL(ydl_options) as ydl:
        result = ydl.download([f"https://www.youtube.com/playlist?list={playlist['playlistId']}"])
        print(f'{os.path.basename(__file__)} ydl.download({playlist["title"]}) result: {result}')
print(f"Logs saved to '{logs_file_path}'")
