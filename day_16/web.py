""" 
Crawling = discovering page
Scapping = exctrating data from pages

API call = send request and wait for response
"""

# API Calling
# https://itunes.apple.com/search?term=Kishorekumar&entity=song&limit=5


# Project Environment -> # package install
# python3 -m venv my_env
# source my_env/bin/activate

import requests
# inputName = input("Enter singer name: ")
# count = int(input("Enter number of tracks: "))
inputName = "Kishore"
count = 5
# res = requests.get(f'https://sdfkhsdlkfshdkfjh.apple.com/search?term={inputName}&entity=song&limit={count}')
res = requests.get(f'https://itunes.apple.com/search?term={inputName}&entity=song&limit={count}')

if res.status_code == 200:
    songs = res.json()
    print(f"Track: {songs['results'][0]}")
else:
    print("Some error")
    
    # track.artworkUrl100
    # track.trackName
    # track.previewUrl