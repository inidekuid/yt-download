import tkinter as tk 
from tkinter import simpledialog
from pytube import YouTube

ROOT = tk.Tk()

ROOT.withdraw()
URLYoutube = simpledialog.askstring(title="Masukkan URL:",
                                    prompt="Masukkan video URL yang mau diunduh")
YouTube(URLYoutube).streams.first().download()

ytlink = YouTube(URLYoutube)

ytlink.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

#print(ytlink.streams)





