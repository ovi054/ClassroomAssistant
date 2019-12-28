# -*- coding: utf-8 -*-

from google_images_download import google_images_download 
import sys
from IPython.display import display, Image
from IPython.display import YouTubeVideo
def showPhoto(str):
    orig_stdout = sys.stdout
    f = open('URLS.txt', 'w')
    sys.stdout = f
    response = google_images_download.googleimagesdownload()

    arguments = {"keywords"     : str,
             "limit"        : 1,
             "print_urls"   : True,
             }
    #paths = response.download(arguments)
    try:
        paths = response.download(arguments)
    except: 
        pass


                     
    sys.stdout = orig_stdout
    f.close()


    with open('URLS.txt') as f:
        content = f.readlines()
        f.close()

    urls = []
    for j in range(len(content)):
        if content[j][:10] == 'Evaluating':
            urls.append(content[j+2][11:-1])   
    #print(urls)
    if(len(urls)):
        img = Image(urls[0])
        display(img)
    #vid = YouTubeVideo("bfmFfD2RIcg")
    #YouTubeVideo("bfmFfD2RIcg")
    #display(vid)
