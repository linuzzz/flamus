import datetime
import requests
import os
from flask import Flask, render_template, jsonify

import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())
    

@app.route('/dario/')
def dario():
    return 'ciao Dario'


@app.route('/spo/')
def spo():
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    name = 'Avicii'

    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    print(name)
    if len(items) > 0:
        artist = items[0]
        print(artist['name'], artist['images'][0]['url'])
        
    return render_template('about.html')
    

@app.route('/about/')
def about():
    #url = "https://api.discogs.com/database/search/q=nirvana&type=artist&token=WqPZVKGWxZUTAPtqXjZEnQvihsfPlXUyELwNzTvx"
    #url = 'https://musicbrainz.org/ws/2/artist?query=coldplay&fmt=json'
    #url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getInfo&api_key=aa3c65d69a6a12a3f8570e4e3ae11749&artist=nirvana&format=json`)'
    #url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getInfo&api_key=aa3c65d69a6a12a3f8570e4e3ae11749&artist=nirvana`)'
    #b5c5aaee-cb7b-4bd5-8d8b-b7c09714d5e3
    #aa3c65d69a6a12a3f8570e4e3ae11749
    
    headers = {
        'user-agent': 'Dataquest'
    }

    payload = {
        'api_key': 'aa3c65d69a6a12a3f8570e4e3ae11749',
        'method': 'artist.getInfo',
        'artist': 'nirvana',
        'format': 'json'
    }

    r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    print(r.text)
    
    
    #headers = {
	#    "query": "nirvana",
	#    "type": "artist"
	#"Authorization": "WqPZVKGWxZUTAPtqXjZEnQvihsfPlXUyELwNzTvx"
    #}

    #artist = requests.get(url, headers=headers)
    #artist = requests.get(url)

    #print(artist.json())
    #print(artist.text)
    return render_template('about.html')
    
# ...

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)
    
@app.route('/artist/<id>/')
def artist(id):
    url = "https://deezerdevs-deezer.p.rapidapi.com/artist/" + str(id)
    headers = {
	    "X-RapidAPI-Key": os.environ['rapidapi_deezer_key'],
	    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }

    artist = requests.get(url, headers=headers)

    print(artist.json())
    
    return render_template('artist.html', artist=artist.json())
    
@app.route('/artists/')
def artists():
    artists = { 1905:"The Distillers", 
        809:"OMD", 
        1500: "Rancid", 
        1800:"Sex Pistols",
        3200:"Brody Dalle",
        6400:"The Interrupters"}

    return render_template('music.html', artists=artists)
    
@app.route('/ajax/<timeframe>/')
def ajax(timeframe):
    print(timeframe)
    artists = { 1905:"The Distillers", 
        809:"OMD", 
        1500: "Rancid", 
        1800:"Sex Pistols",
        3200:"Brody Dalle",
        6400:"The Interrupters"}

    return jsonify(artists)
    
@app.route('/ajax4/<start>/<end>/')
def ajax4(start, end):
    print(start)
    print(end)
    artists = { 1905:"The Distillers", 
        809:"OMD", 
        1500: "Rancid", 
        1800:"Sex Pistols",
        3200:"Brody Dalle",
        6400:"The Interrupters"}

    return jsonify(artists)
