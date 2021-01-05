import cv2
import numpy as np
import face_recognition
import os
from skimage.io import imread_collection
from datetime import datetime
from csv import writer


pathImg = './ImagesAttendance/*.jpg'
pathCls = './ImagesAttendance/'

images = imread_collection(pathImg)
ClassNames = [x.split('.')[0] for x in os.listdir(pathCls)]


def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeList.append(face_recognition.face_encodings(img)[0])
    return encodeList


def markAttendance(name):
    with open('Attendance.csv', 'a+', newline='\n') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        now = datetime.now()
        timeStr = now.strftime('%H:%M')
        datestr = now.strftime('%d:%m:%Y')
        csv_writer.writerow([name,timeStr,datestr])



encodeListKnownFaces = findEncoding(images)
print('Encoding Complete.')

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(imgS)
    encodesCurrentFrame = face_recognition.face_encodings(imgS, facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnownFaces, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnownFaces, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = ClassNames[matchIndex].upper()
            # print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)


    cv2.imshow('Webcam', img)
    cv2.waitKey(1)


