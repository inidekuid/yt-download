from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

playlist = Playlist("https://www.youtube.com/watch?v=S-pDTsEhg4M&list=PLDgzGydIYPL18xgRUaW3fOhL6_KKzeP7O")

#prints each video url, which is the same as iterating through playlist.video_urls
for url in playlist:
    print(url)
#prints address of each YouTube object in the playlist
for vid in playlist.videos:
    print(vid)

for url in playlist:
   YouTube(url).streams.filter(only_audio=True).first().download()

for url in playlist:
    YouTube(url).streams.first().download('C:\\Users\\muslih-sma1jp\\Desktop\\pytube\\lagu')

folder = "C:\\Users\\muslih-sma1jp\\Desktop\\pytube\\lagu"

for file in os.listdir(folder):
  if re.search('mp4', file):
    mp4_path = os.path.join(folder,file)
    mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
    new_file = mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path)
    os.remove(mp4_path)
