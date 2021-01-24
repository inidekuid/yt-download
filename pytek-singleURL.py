import tkinter as tk 
from tkinter import *
from pytube import YouTube

# lokasi penyimpanan 
SAVE_PATH = "C:\\Users\\muslih-sma1jp\\Desktop\\pytube\\vidio"

# tampilan 
ROOT = Tk()
ROOT.geometry('600x400')
ROOT.resizable(0,0)
ROOT.title('Pengunduh vidio Yutube')

#label-label dan notifikasi
Label(ROOT, text="Unduh vidio youtube suka-suka", fg="red", font=("Calibri", 15)).grid(sticky=N, padx=100, row=0)
Label(ROOT, text="Masukkan URL kamu disini: ", font=("Calibri", 15)).grid(sticky=N, row=1, pady=15)
notif = Label(ROOT, font=("Calibri", 12))
notif.grid(sticky=N, pady=1, row=4)

# tangkap url youtube
URLYoutube = StringVar()
Entry(ROOT, width=70, textvariable = URLYoutube).place(x=40, y=32)

def unduhYoutube() :
    url_vidio = URLYoutube.get()
    try: 
        vidio_yt = YouTube(url_vidio)
        vidio = vidio_yt.streams.get_highest_resolution().download()
        vidio.download(SAVE_PATH)
        notif.config(fg="green", text="Unduhan selesai")
    except Exception as e:
        print(e)
        #notif.config(fg="red", text="vidio gagal unduh")

Button(ROOT,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = unduhYoutube).place(x=180 ,y = 150)

ROOT.mainloop()




