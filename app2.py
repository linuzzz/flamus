import requests
import os
from flask import Flask, render_template, jsonify, request
#sqlite3 built into python, no need to pip install anything
import sqlite3

import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

import datetime

app = Flask(__name__, static_url_path='/static')

def get_db_connection():
    conn = sqlite3.connect('music.db')
    #conn.row_factory = sqlite3.Row
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

    return render_template('index-css-grid.html', artists=artists)
    
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
	#sqlquery = 'select artist,count(artist) from music group by artist order by count(artist) desc limit 20'
	sqlquery = 'select artist,track,count(track) from music group by track order by count(track) desc limit 20'
	queryresults = listreturn(sqlquery)
	print(queryresults)
	return render_template('start.html', results=queryresults)
	
#This is a route/function called by javascript ajax	
@app.route('/refresh/<range_type>/<chart_type>/')
def refresh(range_type,chart_type):
	print(chart_type)
	
	endtime = datetime.datetime.today().timestamp()
	starttime = (datetime.datetime.today() - datetime.timedelta(31)).timestamp()
	
	print(endtime)
	print(starttime)
	sqlquery = 'select artist,track,count(track) from music where uts > ' + str(starttime) + ' group by track order by count(track) desc limit 20'
	queryresults = listreturn(sqlquery)
		
	return jsonify(queryresults)


def listreturn(sqlquery):
	print(sqlquery)
	queryresults_dict = {}
	conn = get_db_connection()
	#DO NOT execute fetchall !!!
	#results = conn.execute(sqlquery).fetchall()
		
	#DO NOT USE row_factory
	#conn.row_factory = sqlite3.Row
	#conn.row_factory = lambda cursor, row: row
	
	'''
	This is a sample of how the dictionary is built:
	{
	0: ['underground_vandalz.jpg', 'Underground Vandalz', 'The Threshold Of Death', 219], 
	1: ['the_mahones.jpg', 'The Mahones', 'Drunken Lazy Bastard', 194], 
	2: ['the_distillers.jpg', 'The Distillers', 'Hall of Mirrors', 73], 
	3: ['yungblud_ft_machine_gun_kelly.jpg', 'YUNGBLUD ft Machine Gun Kelly', 'Acting Like That', 73], 
	4: ['acdc.jpg', 'AC/DC', 'Moneytalks', 72], 
	5: ['umberto_tozzi.jpg', 'Umberto Tozzi', 'Tu', 70], 
	6: ['rancid.jpg', 'Rancid', 'Ghost of a Chance', 70], ...
	}

	
	'''	
		
	c = conn.cursor()
	results = c.execute(sqlquery)
	index = 0
	for row in results:
		#output = ""
		queryresults_list = []
		#row[0] contains the artist name, with spaces and upper/lower cases
		#remove spaces and convert to lowercase for image jpg match of artist
		artist_name_imgfile = row[0].replace(" ", "_").lower()+".jpg"
		#AC/DC FILE ISSUE MANAGEMENT :-)
		artist_name_imgfile = artist_name_imgfile.replace("/","")
		spoty_get_artist_img(row[0], os.path.join(app.root_path, 'static/images', artist_name_imgfile))
		queryresults_list.append(artist_name_imgfile)
		for item in row:
			queryresults_list.append(item)
			#output = output + str(item) + "|"
		#Slicing method to remove last char from a string
		#output = output[:len(output)-1]
		
		#print("------", output)
		queryresults_dict[index] = queryresults_list  
		
		index = index + 1

	#return music_results, artist_name_imgfile
	return queryresults_dict
	
def spoty_get_artist_img(artist_name, artist_name_imgfile):
	if os.path.isfile(artist_name_imgfile):	
		print("ciao " + artist_name)
	else:
		print("non ci sono")
		
		spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

		results = spotify.search(q='artist:' + artist_name, type='artist')
		items = results['artists']['items']
		if len(items) > 0:
			#spotify find results but maybe without url images
			artist = items[0]
			try:
				print(artist['name'], artist['images'][0]['url'])
				url = artist['images'][0]['url']
			except:
				print("No image for ", artist['name'])
				url = 'https://guardian.ng/wp-content/uploads/2020/10/Music-art.-Photo-Pinterest-870x598.jpg'
		else:
			#generic pic if no spotify image is available
			print("No image for ", artist['name'])
			url = 'https://guardian.ng/wp-content/uploads/2020/10/Music-art.-Photo-Pinterest-870x598.jpg'
			
		response = requests.get(url)
		with open(os.path.join(app.root_path, 'static/images', artist_name_imgfile), "wb") as f:
			f.write(response.content)
			
			