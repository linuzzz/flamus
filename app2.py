import datetime
import requests
import os
from flask import Flask, render_template

app = Flask(__name__)

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
