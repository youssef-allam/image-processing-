import cv2 as cv
import numpy as np

image = cv.imread('photos/Gray-wolf.jpg')
image1 = cv.imread('photos/Gray-wolf1.jpg')
image2 = cv.imread('photos/img1.jpg')
image3 = cv.imread('photos/img3.jpg')



def display4imges(img1,img2, img3 , img4):
    #make all imgs at same size
    img1 = cv.resize(img1 , (480 ,270))
    img2 = cv.resize(img2 , (480 ,270))
    img3 = cv.resize(img3 , (480 ,270))
    img4 = cv.resize(img4 , (480 ,270))
    #collecting 4 images in 2X2 figure
    new_img1 = np.concatenate((img2 , img1), axis = 1)
    new_img2 = np.concatenate((img3 , img4), axis = 1)
    new_img = np.concatenate((new_img1 , new_img2), axis = 0) 
    #display the window of images
    cv.imshow('4 imgs', new_img)
    cv.waitKey(0)
    cv.destroyAllWindows

#display4imges(image, image1,image2 , image3)



