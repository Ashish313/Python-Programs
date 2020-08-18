import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# read the image
img = cv.imread('images/img_1.jpeg')

# convert the image to gray scale
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# detect the face in the image
faces = face_cascade.detectMultiScale(gray_img,1.05,5)

# create a rectangle surrounding the face
for x,y,w,h in faces:
    img = cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)


cv.imshow('Robert',img)
cv.waitKey(0)
cv.destroyAllWindows()