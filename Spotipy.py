import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

auth_manager = SpotifyClientCredentials('your_client_id','your_client_secret')
sp = spotipy.Spotify(auth_manager=auth_manager)

def getAlbumTrackIDs(album_url):
    album_id = album_url.split("/")[-1].split("?")[0]
    album = sp.album(album_id)
    track_ids = [track['id'] for track in album['tracks']['items']]
    return track_ids


def getTrackFeatures(id):
    track_info = sp.track(id)

    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    url = track_info['external_urls']['spotify']

    return [name, album, artist, url]


# Code for creating dataframe of feteched playlist

emotion_dict = {0:"Angry",1:"Disgusted",2:"Fearful",3:"Happy",4:"Neutral",5:"Sad",6:"Surprised"}
music_dist={0:"https://open.spotify.com/album/1CQeKPICg50fn9bkhesH5S?si=aa548c0fafda44d8",1:"https://open.spotify.com/album/1CQeKPICg50fn9bkhesH5S?si=aa548c0fafda44d8 ",
            2:"https://open.spotify.com/album/3qeQAGoVgKyXu5E4uqVgTF?si=whrEGTJoSOm3GVEZ_rBhng",3:"https://open.spotify.com/album/1V3SPr45Sj8uRuAup6Dd2l?si=Rvc5Dcm1T8mhWKP6JJLH6w"
            ,4:"https://open.spotify.com/album/49g8Aqji0Lw9rTeI5Av4Va?si=d2d3819fd15f4c37",5:"https://open.spotify.com/album/3E7llBA1fWbavvRpynlGl1?si=3JxETWsRSwKDZQhCfOi8Jg",
            6:"https://open.spotify.com/album/1V3SPr45Sj8uRuAup6Dd2l?si=Rvc5Dcm1T8mhWKP6JJLH6w"}

'''
Code can def be modularised into a function but i tried to write it when i was extremely sleepy so thought screw it and repeated code block

Uncomment for fetching updated playlists
'''


track_ids = getAlbumTrackIDs(music_dist[0])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist', 'URL'])
 # ,'Release_date','Length','Popularity'
    df.to_csv('songs/angry.csv')
print("CSV Generated")

track_ids = getAlbumTrackIDs(music_dist[1])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist', 'URL'])
 # ,'Release_date','Length','Popularity'
    df.to_csv('songs/disgusted.csv')
print("CSV Generated")

track_ids = getAlbumTrackIDs(music_dist[2])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist', 'URL'])
 # ,'Release_date','Length','Popularity'
    df.to_csv('songs/fearful.csv')
print("CSV Generated")

track_ids = getAlbumTrackIDs(music_dist[3])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist', 'URL'])
 # ,'Release_date','Length','Popularity'
    df.to_csv('songs/happy.csv')
print("CSV Generated")

track_ids = getAlbumTrackIDs(music_dist[4])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist', 'URL'])
 # ,'Release_date','Length','Popularity'
    df.to_csv('songs/neutral.csv')
print("CSV Generated")

track_ids = getAlbumTrackIDs(music_dist[5])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    ddf = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist', 'URL'])
 # ,'Release_date','Length','Popularity'
    df.to_csv('songs/sad.csv')
print("CSV Generated")

track_ids = getAlbumTrackIDs(music_dist[6])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist', 'URL'])
 # ,'Release_date','Length','Popularity'
    df.to_csv('songs/surprised.csv')
print("CSV Generated")