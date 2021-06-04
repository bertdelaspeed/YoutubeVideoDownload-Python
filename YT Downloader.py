from pytube import YouTube
from tkinter import *
from PIL import ImageTk, Image
import pyautogui
from threading import Thread


hd1080p = "1080p"
hd720p = "720p"
hd480p = "480p"
hd360p = "360p"
hd240p = "240p"
hd144p = "144p"


# vidObj = YouTube

def goFunction(self):
    pyautogui.hotkey("ctrl", "v")


def cleanfucntion(self):
    Search.delete(0.0, END)


def dlFunction(self):
    vidResolution = choice.get()
    if vidResolution == "":
        pyautogui.alert("Select the resolution ")
    else:
        YtLink = Search.get('1.0', END)
        vidObj = YouTube(YtLink)
        try:
            pyautogui.alert("Trying to Download ... Please click OK and wait !")
            success = vidObj.streams.get_by_resolution(vidResolution)
            vidObj.streams.get_by_resolution(vidResolution).download()
            if success:
                pyautogui.alert("Download Completed !")
        except:
            pyautogui.alert("Couldn't download | Try some other resolution ")
    t = Thread(target=dlFunction, args=(self))
    t.start()



window = Tk()
window.title("YT Downloader")
window.geometry("500x360")
window.iconbitmap("E:\Programming\Python\PycharmProjects\YoutubeDownload\YoungMe.ico")

Name = Label(window, font=('Lucida Fax', 15, 'bold'), text="Laspeed Youtube Downloader", fg="red")
Name.place(relx=.045, rely=.038)

Search = Text(window, width=52, height=2)
Search.place(relx=.045, rely=.2)

GoBtn = ImageTk.PhotoImage(Image.open("E:\Programming\Python\PycharmProjects\YoutubeDownload\gobtn2.png"))
panel = Label(window, image=GoBtn)
panel.place(relx=0.8, rely=.2)
panel.bind("<Button-1>", goFunction)

clearbtn = ImageTk.PhotoImage(Image.open("E:\Programming\Python\PycharmProjects\YoutubeDownload\cleaner.png"))
clearpanel = Label(window, image=clearbtn)
clearpanel.place(relx=.8, rely=.35)
clearpanel.bind("<Button-1>", cleanfucntion)

choice = StringVar()
HD720p = Radiobutton(text="720P", variable=choice, value=hd720p)
HD720p.place(relx=.3, rely=.4)
HD360p = Radiobutton(text="360P", variable=choice, value=hd360p)
HD360p.place(relx=.1, rely=.5)
HD1080p = Radiobutton(text="1080", variable=choice, value=hd1080p)
HD1080p.place(relx=.1, rely=.4)
HD240p = Radiobutton(text="240P", variable=choice, value=hd240p)
HD240p.place(relx=.30, rely=.5)
HD480p = Radiobutton(text="480P", variable=choice, value=hd480p)
HD480p.place(relx=.5, rely=.4)
HD144p = Radiobutton(text="144P", variable=choice, value=hd144p)
HD144p.place(relx=.5, rely=.5)

DownloadBtn = ImageTk.PhotoImage(Image.open("E:\Programming\Python\PycharmProjects\YoutubeDownload\download1.png"))
panel2 = Label(window, image=DownloadBtn)
panel2.place(relx=.16, rely=.68)
panel2.bind("<Button-1>", dlFunction)

window.mainloop()
