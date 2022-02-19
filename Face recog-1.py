# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:30:02 2021

@author: sahil
"""

import cv2
#create a cascade classifier object 
face_classifier = cv2.CascadeClassifier("C:/Users/sahil/Downloads/haarcascade_frontalface_default.xml")

#reading the image as it is
img = cv2.imread("C:/Users/sahil/OneDrive/Desktop/SEM-7/IP/standard_test_images/lena_color_256.tif",0)


#reading the image as gray scale image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#SEARCH the co-ordinates of the image 
faces = face_classifier.detectMultiScale(gray,1.3,5)
                                            #scalefactor = 1.3
                                            #minNeighbors = 5
                                            
#rectangular face box
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)       
                                    
print(type(faces))
print(faces)