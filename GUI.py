from tkinter import *
import time
import cv2
import sqlite3
import numpy as np
import os
from RPi import GPIO as GPIO
"""
def face_detector()
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height

    face_id = input("\n enter user face id and press <return> ==>> ")
    #Initialize individual face count
    count = 0
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,     
            scaleFactor=1.2,
            minNeighbors=5,     
            minSize=(20, 20)
        )
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            count += 1
            #Save the captured image in the dataset folder
            cv2.imwrite("dataset/user." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        
        cv2.imshow('video',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
        elif count >= 30:
            break
    print("\n[INFO] exiting program and clean up stuff...")
    cap.release()
    cv2.destroyAllWindows()
"""
def Face_recognition():
    recognizer = cv2.face.createLBPHFaceRecognizer()
    recognizer.load('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    #initiate id counter
    #id = 0
    # names related to ids: example ==> Pisoh: id=1,  etc
    names = ['None', 'None','None','None','None','None','None','None','None','None','None','None','Pisoh', 'Clair', 'Aloys'] 
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret, img =cam.read()
        img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # Check if confidence is less than 100 ==> "0" is perfect match 
            if (confidence < 100):
                print(id)
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    # Do a bit of cleanup
    #print("\n [INFO] Exiting Program and cleanup stuff")
def stop_face():        
    cv2.destroyAllWindows()
            
def Night_mode():
    person_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    cap = cv2.VideoCapture('pedestrians.avi')
    while True:
        r, frame = cap.read()
        #frame = cv2.flip(frame, -1)
        if r:
            start_time = time.time()
            frame = cv2.resize(frame,(640,360)) # Downscale to improve frame rate
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # Haar-cascade classifier needs a grayscale image
            rects = person_cascade.detectMultiScale(gray_frame)
                
            for (x, y, w, h) in rects:
                cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
            cv2.imshow("NIGHT MODE", frame)
        k = cv2.waitKey(1)
        if k & 0xFF == ord("q"): # Exit condition
            break



def relay1_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setwarnings(False)
    state = GPIO.input(14)
    if(state is False):
        GPIO.output(14,True)
    else:
        GPIO.output(14, False)
    
def relay1_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setwarnings(False)
    state = GPIO.input(14)
    if(state is True):
        GPIO.output(14, False)
    else:
        GPIO.output(14, True)
def servo_open():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setwarnings(False)
    pwm = GPIO.PWM(15, 50)
    pwm.start(0)
    #while(True):
    def setAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(15, True)
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(15, False)
        pwm.ChangeDutyCycle(0)
        
    setAngle(90)
    pwm.stop()
    GPIO.cleanup()
def servo_close():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setwarnings(False)
    pwm = GPIO.PWM(15, 50)
    pwm.start(0)
    #while(True):
    def setAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(15, True)
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(15, False)
        pwm.ChangeDutyCycle(0)
        
    setAngle(0)
    pwm.stop()
    GPIO.cleanup()

    

window = Tk()
window.title("SCHOOL SECURITY PLATFORM")
window.geometry("500x500")
B2 = Button(window, text='LAUNCH FACE RECOGNITION', command=Face_recognition)
B2.grid(row=1, column=0)
B4 = Button(window, text='LAUNCH NIGHT MODE', command = Night_mode)         #Determine to add this feature to detect people
B4.grid(row=2, column=0)
#Lighting controls
L1 = Label(window, text='LIGHTING')
L1.grid(row=3, column=1)
B6 = Button(window, text='TURN LIGHTS OFF', command = relay1_on)
B6.grid(row=4, column=0)
B7 = Button(window, text='TURN LIGHTS ON', command = relay1_off)
B7.grid(row=5, column=0)
L2 = Label(window, text='MAIN GATE').grid(row=6, column=1)
B8 = Button(window, text = "GATE OPEN", command = servo_open).grid(row=7, column=0)
B9 = Button(window, text = "GATE CLOSE", command = servo_close).grid(row=8, column=0)

window.mainloop()