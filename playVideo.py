# -*- coding: utf-8 -*-
import urllib.request
import vlc,pafy
from bs4 import BeautifulSoup

def playVideo(str):
    textToSearch = str
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    urls=[]
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    #print('https://www.youtube.com' + vid['href'])
        urls.append('https://www.youtube.com' + vid['href'])

    url = urls[0]
    video = pafy.new(url)
    best = video.getbest()
    media= vlc.MediaPlayer(best.url)
    media.play()