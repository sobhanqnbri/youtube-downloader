from tkinter import *
import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog
from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
from os import path
import shutil

root = Tk()
canvas=Canvas(root,width=200,height=200)

root.title('YouTube Downloader')

root.geometry("400x400")

root.resizable(width=False,height=False)

def path_link():
 path=filedialog.askdirectory()
 path_label.config(text=path)


def download_file():
 get_link=entry.get()
 path_user=path_label.cget("text")
 mp4 = YouTube(get_link).streams.get_highest_resolution().download()
 video = VideoFileClip(mp4)
 video.close()
 shutil.move(mp4,path_user)


path_btn=Button(root,text='select', command=path_link)

path_label=Label(root,text="Select path:",font=("arial",12))

img=(Image.open(r'download.png'))

img_resize=img.resize((300,100))

logo=ImageTk.PhotoImage(img_resize)
label=Label(root,image=logo)
label.pack()


entry=Entry(root,width=40)
entry1=Label(root,text="Enter Link: ", font=('arial',15))

btn=Button(root,text='Download',fg='white', background='red', width=30,command=download_file)
btn.place(x=100,y=340)
entry.place(x=90,y=220)
entry1.place(x=90,y=170)
label.place(x=55,y=10)
path_label.place(x=120,y=250)
path_btn.place(x=190,y=290)




root.mainloop()