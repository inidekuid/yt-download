from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

playlist = Playlist("https://www.youtube.com/playlist?list=PLX5sCtu_TCxa11l-mfbfEehrmKfYvP4Wj")

#mencetak setiap url video, yang sama seperti melakukan iterasi playlist.video_urls
for url in playlist:
    print(url)
#mencetak alamat setiap objek YouTube di playlist
for vid in playlist.videos:
    print(vid)

for url in playlist:
   YouTube(url).streams.filter(only_audio=True).first().download()

for url in playlist:
    YouTube(url).streams.first().download('C:\\Users\\muslih-sma1jp\\Desktop\\pytube')

folder = "C:\\Users\\muslih-sma1jp\\Desktop\\pytube"

for file in os.listdir(folder):
  if re.search('mp4', file):
    mp4_path = os.path.join(folder,file)
    mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
    new_file = mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path)
    os.remove(mp4_path)
