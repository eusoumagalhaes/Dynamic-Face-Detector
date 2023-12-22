import cv2
import numpy as np
from random import randint

camera = cv2.VideoCapture(0)
alvo = cv2.CascadeClassifier(r'cascades/haarcascade_frontalface_default.xml')

while True:
    check, img = camera.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objetos = alvo.detectMultiScale(imgGray, minSize=(50,50))
    #print(objetos)
    for x, y, l, a in objetos: 
        cv2.rectangle(img, (x,y),(x+l, y+a), (255, 0, 0), 2)
    cv2.imshow('Câmerazona', img)
    cv2.waitKey(1)