import cv2

# Load the cascade
face_cascade1 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade2 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frame = 0
# To capture video from webcam. 
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

# To set main camera to 0
cam0 = True

while True:
    # Read the frame
    _, img1 = cap1.read()
    _, img2 = cap2.read()
    # Convert to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    face1 = face_cascade1.detectMultiScale(gray1, 1.1, 10)
    face2 = face_cascade2.detectMultiScale(gray2, 1.1, 10)

    # Frame delay to stop flickering
    if frame >10:
        #select the Camera with most faces in it
        if (len(face2)>=len(face1)):
            cam0 = False
            frame = 0
        else:
            cam0 = True
            frame = 0
    # Choose camera to output
    if cam0:
        face = face1
        img = img1
    else:
        face = face2
        img = img2
    frame +=1
    
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap1.release()
cap2.release()
