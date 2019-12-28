# -*- coding: utf-8 -*-
import speech_recognition as sr
import takeAttendence as take
import showPhoto
import playVideo
#import takeAttendence
#take.take_Attensence()
#showPhoto.showPhoto("")
#watchVideo.watchVideo("Operating System")

def get_audio():
    r = sr.Recognizer()   #Speech recognition
    with sr.Microphone() as source:
        print("Say something!")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        #message = r.recognize_google(audio)
        #print("Check: "+message)
    try:
        print("User: " + r.recognize_google(audio))
        return r.recognize_google(audio)
    except Exception:
        pass
    except UnknownValueError: 
        pass
while True:
    str = get_audio()
    if("attendance" in str):
        take.take_Attensence()
        #continue
    elif("photo" in str):
        if(str.startswith("show photo of")):
            str.replace('show photo of','')
            showPhoto.showPhoto(str)
        elif(str.startswith("photo of")):
            str.replace('photo of','')
            showPhoto.showPhoto(str)
        else:
            showPhoto.showPhoto(str)
    elif("video" in str):
        if(str.startswith("play video of")):
            str.replace('play video of','')
            playVideo.playVideo(str)
        elif(str.startswith("video of")):
            str.replace('video of','')
            playVideo.playVideo(str)
        else:
            playVideo.playVideo(str)
    elif("stop" in str):
        break
    else:
        continue
        
    
        

        
