import requests
import os
from flask import Flask, render_template, jsonify, request
#sqlite3 built into python, no need to pip install anything
import sqlite3

import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__, static_url_path='/static')

def get_db_connection():
    conn = sqlite3.connect('music.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def hello():
    artists = {
        "place1":"holder1",
        "place2":"holder2",
        "place3":"holder3",
        "place4":"holder4",
        "place5":"holder5",
        "place6":"holder6",
        "place7":"holder7",
        "place8":"holder8",
        "place9":"holder9",
        "place10":"holder10",
        "place11":"holder11",
        "place12":"holder12",
        "place13":"holder13",
        "place14":"holder14",
        "place15":"holder15",
        "place16":"holder16",
        "place17":"holder17",
        "place18":"holder18",
        "place19":"holder19",
        "place20":"holder20"
    }

    return render_template('music.html', artists=artists)
    

@app.route('/chart/')
def chart():
    artists = { 
        1905:"The Distillers", 
        809:"OMD", 
        1500:"Rancid", 
        1800:"Sex Pistols",
        3200:"Brody Dalle",
        6400:"The Interrupters"}

    return render_template('music.html', artists=artists)
    

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
    
    """
    headers = {
        'user-agent': 'Dataquest'
    }
    """

    """
    payload = {
        'api_key': 'aa3c65d69a6a12a3f8570e4e3ae11749',
        'method': 'artist.getInfo',
        'artist': 'nirvana',
        'format': 'json'
    }
    """

    #r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    #print(r.text)
    
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

'''
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
'''

@app.route('/ajax/<timeframe>/')
def ajax(timeframe):
    print(timeframe)
    artists = { 
        1905:"The Killers", 
        809:"Sharon Van Etten", 
        1500: "Simple Minds", 
        1800:"Nirvana",
        3200:"Lucio Dalla",
        6400:"Claudio Baglioni"}

    return jsonify(artists)
    
@app.route('/ajax4/<start>/<end>/')
def ajax4(start, end):
    print(start)
    print(end)
    artists = { 
        1905:"The Distillers", 
        809:"OMD", 
        1500: "Rancid", 
        1800:"Sex Pistols",
        3200:"Brody Dalle",
        6400:"The Interrupters"}

    return jsonify(artists)


@app.route('/ajax2/<chart_type>/')
def ajax2(chart_type):
	print("---")
	print(chart_type)
	print("---")
	artists = listreturn2()
    
	return jsonify(artists)





@app.route('/report/', methods = ['POST'])
def report():
	if request.method == 'POST':
		try:
			ot = request.form['option_time']
		except KeyError:
			ot = None
        
		try:
			start = request.form['start']
		except KeyError:
			start = None
        
		try:
			end = request.form['end']
		except KeyError:
			end = None
            
		try:
			querytype = request.form['type']
		except KeyError:
			querytype = None
                
		print(start)
		print(end)
		print(ot)
		print(querytype)
    
		return render_template('report.html', artists=listreturn())
    
@app.route('/search/')
def search():
	return render_template('query.html')

@app.route('/start/')
def start():
	#return render_template('start.html')
	listreturn3()
	return render_template('start.html', artists=listreturn3())


def listreturn():
	artists = {
        "place1":"holder1",
        "place2":"holder2",
        "place3":"holder3",
        "place4":"holder4",
        "place5":"holder5",
        "place6":"holder6",
        "place7":"holder7",
        "place8":"holder8",
        "place9":"holder9",
        "place10":"holder10",
        "place11":"holder11",
        "place12":"holder12",
        "place13":"holder13",
        "place14":"holder14",
        "place15":"holder15",
        "place16":"holder16",
        "place17":"holder17",
        "place18":"holder18",
        "place19":"holder19",
        "place20":"holder20"
	}
    
	return artists


def listreturn2():
	artists = {
   	"2place1":"2holder1",
      "2place2":"2holder2",
      "2place3":"2holder3",
      "2place4":"2holder4",
      "2place5":"2holder5",
      "2place6":"2holder6",
      "2place7":"2holder7",
      "2place8":"2holder8",
      "2place9":"2holder9",
      "2place10":"2holder10",
      "2place11":"2holder11",
      "2place12":"2holder12",
      "2place13":"2holder13",
      "2place14":"2holder14",
      "2place15":"2holder15",
      "2place16":"2holder16",
      "2place17":"2holder17",
      "2place18":"2holder18",
      "2place19":"2holder19",
      "2place20":"2holder20"
	}
     
	return artists

def listreturn3():
	artists = {}
	conn = get_db_connection()
	results = conn.execute('SELECT artist FROM music limit 20').fetchall()
	index = 1
	for row in results:
		artists[index]=row[0]
		index = index + 1
		print(row[0])
	conn.close()
	return artists
