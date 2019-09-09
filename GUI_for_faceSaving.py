from tkinter import *
import cv2
import numpy as np
from PIL import Image
import os


def face_trainer():
    path = 'dataset'

    recognizer = cv2.face.createLBPHFaceRecognizer()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #Function to get the images and label data

    def getImagesAndLabel(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            PIL_image = Image.open(imagePath).convert('L')  #Convert it to gray scale

            img_numpy = np.array(PIL_image, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples, ids
    print("\n [INFO] Training faces. It will take a few seconds. Wait ... ")
    faces, ids = getImagesAndLabel(path)
    recognizer.train(faces, np.array(ids))

    #Save the model into trainer/trainer.yml
    recognizer.save('trainer/trainer.yml')
    #Print the number of faces trained and end the program
    print("\n [INFO] {0} faces trained. Exiting program".format(len(np.unique(ids))))



faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

def takePictures():
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height
    Name = name.get()
    Age = age.get()
    Gen = gen.get()
    Class = clas.get()
    Id = ID.get()
    face_id = Id
    count = 0
    while True:
        ret, img =cap.read()
        img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (20, 20),
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
    
app = Tk()
app.title("REGISTRATION")
app.geometry('300x200')
L1 = Label(app, text='NAME:').grid(row=0, column=0)
name = StringVar()
E1 = Entry(app, textvariable=name).grid(row=0, column=1)
L2 = Label(app, text='AGE:').grid(row=1, column=0)
age = StringVar()
E2 = Entry(app, textvariable=age).grid(row=1, column=1)
L3 = Label(app, text='GENDER:').grid(row=2, column=0)
gen = StringVar()
E3 = Entry(app, textvariable=gen).grid(row=2, column=1)
L4 = Label(app, text='CLASS:').grid(row=3, column=0)
clas = StringVar()
E4 = Entry(app, textvariable=clas).grid(row=3, column=1)
L5 = Label(app, text="ID:").grid(row=4, column=0)
ID = StringVar()
E5 = Entry(app, textvariable=ID).grid(row=4, column=1)
B1 = Button(app, text='TAKE PICTURES',command=takePictures).grid(row=5, column=1)
B2 = Button(app, text='TRAINER', command=face_trainer).grid(row=5, column=2)
T1 = Text(app, width=20, height=1).grid(row=6, column=1, columnspan=1)


app.mainloop()
