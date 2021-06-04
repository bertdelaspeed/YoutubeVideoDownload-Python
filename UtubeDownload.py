# ydl1.py
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}#no option specified here
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=1DCnOSWZWiM']) #

#Here is the version with option
'''#ydl2.py
from __future__ import unicode_literals
import youtube_dl

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',       
    'outtmpl': '%(id)s',        
    'noplaylist' : True,        
    'progress_hooks': [my_hook],  
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['Just paste the link of the video here then run the program'])'''