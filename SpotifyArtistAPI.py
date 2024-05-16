import pandas as pd
import numpy as np
from flask import jsonify

df = pd.read_csv("CLEANED_Spotify_artist_info.csv")

def artists():
    l = list(df['names'].unique())
    l.sort()
    return {'artists': l}

def artistpopularity(artist):
    popularity = int(df.loc[df['names'] == artist, 'popularity'].values[0])
    Monthly_Listeners= int(df.loc[df['names'] == artist, 'monthly_listeners'].values[0])
    ID= df.loc[df['names'] == artist, 'ids'].values[0]
    followers= int(df.loc[df['names'] == artist, 'followers'].values[0])
    genre= str(df.loc[df['names'] == artist, 'genres'].values[0])
    return {'ID': ID, 'Name': artist, 'Popularity Score': popularity, 'Monthly Listeners': Monthly_Listeners, 'Followers': followers, 'genre': genre}

def artistsTracks(artist):
    num_of_tracks = int(df.loc[df['names'] == artist, 'num_tracks'].values[0])
    num_of_releases = int(df.loc[df['names'] == artist, 'num_releases'].values[0])
    ID= df.loc[df['names'] == artist, 'ids'].values[0]
    genre= str(df.loc[df['names'] == artist, 'genres'].values[0])
    return {'Name':artist, 'ID': ID, 'Number of Tracks(solo)': num_of_tracks, 'Number of Releases': num_of_releases, 'genre': genre}

def artistTracksRelease(artist):
    first_release = int(df.loc[df['names'] == artist, 'first_release'].values[0])
    last_release = int(df.loc[df['names'] == artist, 'last_release'].values[0])
    ID= df.loc[df['names'] == artist, 'ids'].values[0]
    genre= str(df.loc[df['names'] == artist, 'genres'].values[0])
    return {'Name':artist, 'first_release': first_release, 'last_release': last_release, 'ID': ID, 'genre': genre}

def top5artists():
    sorted_df = df.iloc[df['followers'].sort_values(ascending = False).index]
    names = list(sorted_df['names'][:5])
    return {'Top 5 artists':names}    

def top5genres():
    sorted_df = df.iloc[df['followers'].sort_values(ascending = False).index]
    genres = list(sorted_df['genres'][:5])
    return {'Top 5 genres': genres}

def compareArtists(artist1, artist2):
    artist1Info = df.loc[df['names'] == artist1]
    artist2Info = df.loc[df['names'] == artist2]
    no_of_followers_artist1 = int(artist1Info['followers'].values[0])
    no_of_followers_artist2 = int(artist2Info['followers'].values[0])
    popularity_score_artist1 = int(artist1Info['popularity'].values[0])
    popularity_score_artist2 = int(artist2Info['popularity'].values[0])
    genre_artist1 = str(artist1Info['genres'].values[0])
    genre_artist2 = str(artist2Info['genres'].values[0])
    return {'no of followers of artist 1': no_of_followers_artist1, 'no of followers of artist 2': no_of_followers_artist2, 'popularity score of artist 1': popularity_score_artist1, 'popularity score of artist 2': popularity_score_artist2, 'Genre artist 1': genre_artist1, 'Genre artist 2': genre_artist2, 'name of artist 1': artist1, 'name of artist 2': artist2}


def allApis():
    return {'Fetch list of artists': '/names', 'Fetch popularity of a certain artist': '/artistPopularity', 'Fetch info about tracks by artist': '/artistTracks', 'Fetch info about artists first and last release': '/artistFirstLastRelease', 'Fetch top 5 artists follower wise': '/top5Artists', 'Fetch top 5 genres followers wise': '/top5Genres'}

