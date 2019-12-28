# -*- coding: utf-8 -*-
import cv2
import face_recognition
import pickle
import pandas as pd
import os
import os.path
import datetime
df = pd.read_csv(r"data.csv")
def take_Attensence():
    currentDT = datetime.datetime.now()
    currentDT = str(currentDT)
    currentDT = currentDT[0:16]
    strin = "Input/" + currentDT[:10] +currentDT[11:13] + currentDT[14:] + "in.mp4"
    print(strin)
    strout = "Output/" + currentDT[:10] +currentDT[11:13] + currentDT[14:] + "out.mp4"
    print(strout)
    with open('known_faces.txt', 'rb') as f:
        known_faces = pickle.load(f)
    #print(my_list)
    video_capture = cv2.VideoCapture(0)
    #video_capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
    codec = int(video_capture.get(cv2.CAP_PROP_FOURCC))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_movie = cv2.VideoWriter(strin, codec, fps, (frame_width,frame_height))
# Get a reference to webcam 


# Initialize variables
    face_locations = []
    frame_number = 0
    while (frame_number<60):
        # Grab a single frame of video
        frame_number = frame_number + 1
        ret, frame = video_capture.read()
    
        # Display the resulting image
        cv2.imshow('Video', frame)

# Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        output_movie.write(frame)

# Release handle to the webcam
    video_capture.release()
    output_movie.release()
    cv2.destroyAllWindows()
    
    
 
    
    #print (currentDT)
    input_movie = cv2.VideoCapture(strin)
    length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)
    #print("Classroom abc")
    face_locations = []
    face_encodings = []
    face_names = []
    frame_number = 0
    
    codec = int(input_movie.get(cv2.CAP_PROP_FOURCC))
    fps = int(input_movie.get(cv2.CAP_PROP_FPS))
    frame_width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_movie = cv2.VideoWriter(strout, codec, fps, (frame_width,frame_height))
    df[currentDT] = 'A'
    while True:
        # Grab a single frame of video
        ret, frame = input_movie.read()
        frame_number += 1
        
        # Quit when the input video file ends
        if not ret:
            break
        
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame, model="fog")
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
            #print(match)
            name = None
            m=len(df)
            for j in range(0,m):
                if match[j]:
                    name = df['Name'][j]
                    df[currentDT][j] = 'P'
                    
                    face_names.append(name)
                    
                    # Label the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            if not name:
                continue

        # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
        print("Writing frame {} / {}".format(frame_number, length))
        output_movie.write(frame)

# All done!
    output_movie.release()
    lengthcolumns = len(df.columns)
    lenrows = len(df)
    for i in range(0,lenrows):
        value = df.loc[i]['Percentage']
        n = lengthcolumns - 4
        a= 0
        if(df.iloc[i,lengthcolumns-1]=='P'):
            a=1
    #print(((n-1)*(value/100) + a)/n)* 100)
    #print((((n-1)*(value/100) + a)/n)*100)
        df.iloc[i,3] = (((n-1)*(value/100) + a)/n)*100
    if os.path.isfile("data.csv"):
        #print ("File exist")
        os.remove("data.csv")
        #print("File Removed!")
        export_csv = df.to_csv (r'data.csv', index = None, header=True)
        print("Database updated")
    
    else:
        print ("File not exist")