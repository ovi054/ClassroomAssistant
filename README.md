:star: Please star this project. It helps a lot.

**[Project Report]**

> **CSE 3200: System Development Project**

**Classroom Assistant**

![](.//media/image1.jpeg)

> **Project Team**

**Avi Pal (Roll - 1607054)**

**Ashiqur Rahman (Roll - 1607056)**

**Supervised by**

**Mr. Al-Mahmud**

**Assistant Professor**

**Dept. of Computer Science and Engineering**

**Khulna University of Engineering & Technology**

Table of Contents 
=================

[INTRODUCTION](#introduction)

[Background](#background)

[Purpose](#purpose)

[OBJECTIVES](#objectives)

[Design (Flowchart)](#design-flowchart)

[IMPLEMENTATION](#implementation)

[Hardware Requirement](#hardware-requirement)

[Software Requirement](#software-requirement)

[Web Scraping](#web-scraping)

[How System Works](#how-system-does-work)

[Attendance System:](#attendance-system)

[Conclusion and Recommendation](#conclusion-and-recommendation)

[Challenges](#challenges)

[Limitations](#limitations)

[Future Activities](#future-activities)

[References](#references)

INTRODUCTION
============

Background
----------

Classroom Assistant is a face recognition, web scrapping python-based
classroom management system. It takes attendance of students and show
study related photo and play video from google with single voice
command. Attendance system implemented with OpenCV, Face Recognition
API.

Here, face recognition is a biometric technology that goes beyond just
detecting human faces in an image or video. It goes a bit further to
determine whose face it is. A facial recognition system works by taking
an image of a face and predicting whether the face matches another face
stored in a dataset (or whether a face in one image matches a face in
another).

Web scraping is used for extracting data from websites. Web scraping
software may access the World Wide Web directly using the Hypertext
Transfer Protocol, or through a web browser.

Purpose
-------

The main purpose of this software to help teachers to make the classroom
more digital. In most classroom teachers take attendance by calling
students names one by one. So, it takes quite a lot of time. Again,
students sometimes may not able to hear when teachers calling his/her
name, as he/she gets absent in that day. To avoid those confusion this
software can take attendance of students by detecting their face in the
camera and if it matches then the student will get present automatically
otherwise, he/she will get absent. Also, this software can show images
and play any video from google. Teachers can show and play educational
related video by voice command. This will save many time and teachers
can teach students more efficiently.

OBJECTIVES
==========

1.  To developing an attendance system based on face recognition

2.  To detect as many faces as possible in the training images

3.  To minimum detection of non-process and Multiple

4.  To digitalize Classroom

5.  To teach more efficiently

6.  To show study related images with single voice command

7.  To play study related video with single voice command

Design (Flowchart)
==================

![](.//media/image2.png){width="6.853472222222222in"
height="8.341666666666667in"}

Fig.1: Flow Chart of Classroom Assistant

IMPLEMENTATION
==============

Hardware Requirement
--------------------

-   Camera

Software Requirement
--------------------

-   Anaconda

-   OpenCV

-   dlib

-   face\_recognition library

-   speech\_recognition by google

-   pyaudio

-   google\_images\_download

-   pafy

-   VLC media player

Face Detection
--------------

First, we take images of students and put those in a file. Given the
input images, we apply face detection to train the images and detect the
location of a face in the image. Optionally, we can compute facial
landmarks, enabling us to preprocess and align the face.

Face alignment, as the name suggests, is the process of (1) identifying
the geometric structure of the faces and (2) attempting to obtain a
canonical alignment of the face based on translation, rotation, and
scale.

We apply Convolutional Neural Network (CNN) and OpenCV together. Here's
short summary of the process of face detection:

![](.//media/image3.jpg){width="6.5in" height="4.223611111111111in"}

Fig 2: An overview of the OpenCV face recognition pipeline. The key step
is a CNN feature extractor that generates 128-d facial embeddings

1.  We apply face detection, which detects the presence and location of
    a face in an image

2.  Compute the 128-d face embeddings to quantify a face

3.  Train a Support Vector Machine (SVM) on top of the embeddings

4.  Recognize faces in images and video streams

Web Scraping
------------

1.  First, it extracts the desired data from the website

2.  The data is retrieved in HTML format, after which it is carefully
    parsed to extricate the raw data from the noise surrounding it.

3.  Ultimately, the data is stored in the format and to the exact
    specifications of the project.

![](.//media/image4.jpg){width="6.486111111111111in"
height="2.2083333333333335in"}

Fig 3: Parse data using web scraping

How System Does Work
====================

Attendance System:
------------------

First user has to say something so that system can recognize and do the
task.1

\`![](.//media/image5.PNG){width="5.479931102362205in"
height="0.541742125984252in"}

Now, to take attendance one has to say "take attendance". If system
recognize "attendance" word then the system will start to detect the
faces and put present.

![](.//media/image6.PNG){width="2.908333333333333in"
height="0.3854166666666667in"}

After hearing the voice command, the system will open a video panel and
take input video so that it can match the face encodings that is saved
in a file.

![](.//media/image7.PNG){width="5.85in" height="2.683333333333333in"}

Face encodings are made from trained images from a file where we saved a
certain number of images of students.

![](.//media/image8.PNG){width="6.5in" height="4.091666666666667in"}

Saved Image Files

After that we save that encodings in a txt file so that we can use that
file every time we run the system. This is efficient because we don't
have to train the images again and again.

![](.//media/image9.PNG){width="5.980001093613298in"
height="1.1147386264216972in"}

Encodings are kept in a list

![](.//media/image10.PNG){width="6.5in" height="4.298611111111111in"}

Face Encodings List

![](.//media/image11.PNG){width="4.3756102362204725in"
height="0.635505249343832in"}

Face Encodings Write to a txt file

After examine the faces if it can able to detect the person in the video
then it will put present as "P" in the data file. But if it can not
match any face that is on the saved encodings then it will put absent as
"A" to that student data file. The system will put present only those
faces that can be detected in the input video. There is very less chance
that the system will do a mistake in putting present to a wrong person.
This process is very much accurate. So, there will hardly be any wrong
attendance.

![](.//media/image12.PNG){width="6.5in" height="3.316666666666667in"}

This is output video where we can see the person's face is matched and
system has detected those faces.

![](.//media/image13.PNG){width="6.5in" height="2.4944444444444445in"}

Before Taking Attendance

![](.//media/image14.PNG){width="6.5in" height="2.484027777777778in"}

After Taking Attendance

If a student is detected and get present then the data file will be
updated and his percentage of attendance will change automatically. It
means that if a person gets present his percentage will increase
otherwise it will decrease.

Parse Photo and Video:
----------------------

If user say "show photo of something" (Here, something as car, apple,
any figure) then an image will be shown in the console.

![](.//media/image15.PNG){width="5.683333333333334in"
height="0.7333333333333333in"}

Here SDLC diagram will be parsed from google and viewed it to the
console

![](.//media/image16.PNG){width="6.5in" height="2.925in"}

Now, if user say "Play video of something" then the system will play a
video that user wanted. It uses web scraping to load the video and show
it to the console

![](.//media/image17.PNG){width="6.008333333333334in"
height="0.8583333333333333in"}

Now a video will start in a media player

![](.//media/image18.PNG){width="6.5in" height="2.75in"}

Conclusion and Recommendation
=============================

Challenges
----------

The designed algorithm was effectively able to detect the different type
of faces specified on this project and recognize those faces which are
known and put present in the sheet and if it is unknown then it puts
absent in the sheet. It will save a lot time from calling student one by
one to know if he/she is present or not. By this way teacher can get
more time to teach the students. Also, there will be no misconception.
Because many students try to save his friends by giving present on
behalf of his friend. In this way camera will detect face and only if
he/she is matched then he/she will get the present. As this software is
called Classroom Assistant it also has other features such as it can
show any photo or play video with a single voice command. It will help
teachers to show study related concept to students. This will bring a
digital classroom. This system's accuracy is almost 90%.

Limitations
-----------

If bright light appears behind object, the system takes times to detect
it but when the system detects the faces it's easily recognizes it. In
voice command the user have to speak clearly otherwise the system will
recognize it as noise.

Future Activities
-----------------

In future, this system will be faster and more accurate. Also, face will
easily detect doesn't matter there will be any light effect behind the
system. In every light combination, the system will able to recognize
the face more accurately. Also, we want to add features like hand
gesture in system.

References
==========

\[1\] Facial recognition system' by Wikipedia

<https://en.wikipedia.org/wiki/Facial_recognition_system>

\[2\] Face recognition with OpenCV, Python, and deep learning

[https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-
learning/](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-%20%20%20%20%20%20learning/)

\[3\] OpenCV documentation

<https://docs.opencv.org/2.4/>

\[4\] Face Recognition package

<https://face-recognition.readthedocs.io/en/latest/face_recognition.html>

\[5\] Goggle\_Images\_Download Documentation

<https://google-images-download.readthedocs.io/en/latest/examples.html>

\[6\] IPython API documentation

<https://ipython.org/ipython-doc/dev/api/generated/IPython.display.html>

\[7\] urllib. request module documentation

<https://docs.python.org/3/library/urllib.request.html>

\[8\] Beautiful Soup documentation

<https://sethc23.github.io/wiki/Python/Beautiful_Soup_Documentation.pdf>

\[9\] Pafy documentation

<https://pythonhosted.org/Pafy/>

- In case of any help you may need from me, please contact avi.pal357@gmail.com directly without any hesitation! I will be glad to help you.

## Author
Avi Pal, Ashiqur Rahman

avi.pal357@gmail.com

Student at Department of Computer Science and Engineering

Khulna University of Engineering & Technology, Khulna

Bangladesh


** Supervised under **

Mr. Al Mahmud

Assistant Professor

Dept. of Computer Science and Engineering

Khulna University of Engineering & Technology


## Licensing

The code in this project is licensed under GNU GPLv3 license.
