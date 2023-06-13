import datetime
import requests
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())
    
# ...
@app.route('/about/')
def about():
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
