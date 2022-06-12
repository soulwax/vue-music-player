# Fetch Music Artwork
# Find out song duration
# Add to js file


from asyncio import sleep
from urllib.request import urlopen
import json
import discogs_client
import wave
import contextlib

from os import listdir
from os.path import isfile, join

MUSIC_PATH = '../src/assets/audios'
IMAGE_PATH = '../src/assets/images'

audio_files = [f for f in listdir(MUSIC_PATH) if isfile(join(MUSIC_PATH, f))]
image_files = [f for f in listdir(IMAGE_PATH) if isfile(join(IMAGE_PATH, f))]

d = discogs_client.Client('ExampleApplication/0.1',
                          user_token="pbIVtVDOcWfKnDuXqmgShNJoBTaVzemRhAtVuBES")

for file in audio_files:
    results = d.search(file.title(), type='release')
    results.pages
    if results:
        artist = results[0].artists[0]
        print(artist.name)
    pass
