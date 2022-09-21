from tkinter import Frame
import numpy as np 
import cv2 as cv 

# variables
low_H = 0
low_S = 0
low_V = 0
high_H = 100
high_S = 100
high_V = 100
max_value_V_S = 255
max_value_H = 180

cap= cv.VideoCapture(0) #get video for the camera


#Extraction of Colors
def extract_color(img, min_value:np.ndarray, max_value:np.ndarray):
    hsv_img= cv.cvtColor(img, cv.COLOR_BGR2HSV) # convert to HSV 
    mask= cv.inRange(hsv_img,min_value,max_value) # threshold to make wanted color white
    extracted_img = cv.bitwise_and(img,img,mask=mask)# extract wanted color
    return extracted_img

#seting values 
def l_h(x) :
    global low_H
    low_H = x
def h_h(x) : 
    global high_H
    high_H = x    
def l_s(x) : 
    global low_S
    low_S = x 
def h_s(x) :  
    global high_S
    high_S = x 
def l_v(x) : 
    global low_V
    low_V = x
def h_v(x) : 
    global high_V
    high_V = x



# trackbars window
cv.namedWindow('TrackBars')
cv.resizeWindow("TrackBars", 400, 330)
cv.createTrackbar('Low_H', 'TrackBars' , low_H , max_value_H   , l_h)
cv.createTrackbar('Low_S', 'TrackBars' , low_S, max_value_V_S  , l_s)
cv.createTrackbar('Low_V', 'TrackBars' , low_V, max_value_V_S  , l_v)
cv.createTrackbar('High_H', 'TrackBars' , 180, max_value_H  , h_h)
cv.createTrackbar('High_S', 'TrackBars' , 255, max_value_V_S, h_s)
cv.createTrackbar('High_V', 'TrackBars' , 255, max_value_V_S, h_v)


while True:
    ret,frame= cap.read() #reading frames
    cv.imshow('Color-Extracted',extract_color(frame, (low_H,low_S,low_V),(high_H,high_S,high_V)))

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()
    