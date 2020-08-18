import cv2,os

# list all the files in the directory
files=os.listdir('images/')

for file in files:
    img=cv2.imread('images/'+file, 1)

    resized=cv2.resize(img,(1254,576))
    
    cv2.imwrite('images/'+file, resized)


print('Done!')
