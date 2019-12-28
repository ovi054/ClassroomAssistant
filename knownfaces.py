# -*- coding: utf-8 -*-
#import cv2
import face_recognition
import pandas as pd
import os
import pickle
df = pd.read_csv(r"data.csv")

#Storing face encoding of students in a list 
known_faces=[]
for i in range(0,60):
    known_faces.append('')
    known_faces[i] = face_recognition.load_image_file(df['Image'][i])
    known_faces[i] = face_recognition.face_encodings(known_faces[i])[0]
    

with open('known_faces.txt', 'wb') as f:
    pickle.dump(known_faces, f)   


