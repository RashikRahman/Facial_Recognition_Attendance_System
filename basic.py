import cv2
import numpy as np
import face_recognition

#Load train data
imgElon = face_recognition.load_image_file('./ImagesBasic/elon1.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

#Load test data
imgElontst = face_recognition.load_image_file('./ImagesBasic/elon2.jpg')
imgElontst = cv2.cvtColor(imgElontst, cv2.COLOR_BGR2RGB)

#Get facial data of train set
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeelon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]), (faceLoc[1],faceLoc[2]), (255,0,255), 2)

#Get facial data of test set
faceLoctst = face_recognition.face_locations(imgElontst)[0]
encodeelontst = face_recognition.face_encodings(imgElontst)[0]
cv2.rectangle(imgElontst,(faceLoctst[3],faceLoctst[0]), (faceLoctst[1],faceLoctst[2]), (255,0,255), 2)

#Comparing faces
results = face_recognition.compare_faces([encodeelon], encodeelontst)
facedis = face_recognition.face_distance([encodeelon], encodeelontst)
print(results,facedis)
cv2.putText(imgElontst,f'{results[0] }{round(facedis[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)

cv2.imshow('Elon', imgElon)
cv2.imshow('Elon test', imgElontst)
cv2.waitKey(0)