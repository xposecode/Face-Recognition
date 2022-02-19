# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 00:38:16 2021

@author: Sahil
"""

import cv2
face_classifier = cv2.CascadeClassifier('C:/Users/sahil/Downloads/haarcascade_frontalface_default.xml')
def face_extractor(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces():
        return None
    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]
        return cropped_face
    cap = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count+=1
            face = cv2.resize(face_extractor(frame),(200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = 'C:/Users/sahil/OneDrive/Desktop/SEM-7/IP/standard_test_images/'+str(count)+'.jpg'
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('Face Cropper',face)

        else:
            print("Face not found")
            pass
        cv2.imshow("Video",frame)
        if cv2.waitKey(1)==13 or count==100:
            break
        cap.release()
cv2.destroyAllWindows()
print('Collecting samples complete!!!')
