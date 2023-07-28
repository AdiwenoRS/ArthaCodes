# Proofreading Tool
# pip install pytube
from pytube import YouTube
import os
def downloader(url):
    yt_vid = YouTube(url).streams.filter(progressive=True)
    yt_vid.order_by('resolution').desc().first().download()
    print("video downloaded")
downloader("https://www.youtube.com/watch?v=nUG3QGcMrYQ")