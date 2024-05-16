from flask import Flask, jsonify, request
import SpotifyArtistAPI

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/names')
def names():
    try:
        return jsonify(SpotifyArtistAPI.artists())
    except Exception as e:
        return jsonify({'error': 'unable display the names of artists'})

@app.route('/artistPopularity')
def get_popularity():
    try:
        artist = request.args.get("artist")
        return SpotifyArtistAPI.artistpopularity(artist=artist)
    except Exception as e:
        return jsonify({'error': 'cannot find this artist in the list, maybe try changing the name?'})

@app.route('/artistTracks')
def get_tracks():
    try:
        artist = request.args.get("artist")
        return SpotifyArtistAPI.artistsTracks(artist = artist)
    except Exception as e:
        return jsonify({'error': 'cannot find this artist in the list, maybe try changing the name?'})

@app.route('/artistFirstLastRelease')
def artistFirstLastInfo():
    try:
        artist = request.args.get("artist")
        return SpotifyArtistAPI.artistTracksRelease(artist = artist)
    except Exception as e:
        return jsonify({'error': 'cannot find this artist in the list, maybe try changing the name?'})

@app.route('/top5artists')
def top5artists():
    try:
        return SpotifyArtistAPI.top5artists()
    except Exception as e:
        return jsonify({'error': 'unable to fetch the top 5 artists'})

@app.route('/top5Genres')
def top5genres():
    try:
        return SpotifyArtistAPI.top5genres()
    except Exception as e:
        return jsonify({'error': 'unable to fetch top 5 genres'})

@app.route('/allApis')
def showApis():
    try:
        return SpotifyArtistAPI.allApis()
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/compareartists')
def compare_artists():
    try:
        artist1 = request.args.get("artist1")
        artist2 = request.args.get("artist2")
        return SpotifyArtistAPI.compareArtists(artist1, artist2)
    except Exception as e:
        return jsonify({'error': 'somethingis wrong'})

    
@app.errorhandler(Exception)
def generic_error_handler(error):
    return jsonify({'error': 'Something went wrong'})


app.run(debug = True)