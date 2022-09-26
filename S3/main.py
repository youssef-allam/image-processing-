import cv2 as cv
import numpy as np


#images are in a folder called photos
# image to process
image = cv.imread('photos\Screenshot from 2022-09-23 06-16-40.png')

#rescaling the image
def scale_size(img , scale):
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)
    return cv.resize(img,  (width,height) )
image = scale_size(image , 0.70)

i = 0 # counter



# red Star Mask as a reference 
RedStar = scale_size(cv.imread('Screenshot from 2022-09-23 06-14-31.png'), 0.70)[110:326]
RedStar = RedStar.astype(int)
RedStar += 100
RedStar[RedStar>255] = 255
RedStar = RedStar.astype(np.uint8)
RedStar= cv.cvtColor(RedStar, cv.COLOR_BGR2HSV)[:, int(RedStar.shape[1]*2//3):]
RedStarMask = cv.inRange(RedStar,(160,50,70), (180, 255, 255))
Cnt_Star, hi = cv.findContours(RedStarMask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.imshow('reference' , RedStarMask)



# processing
def extract_color(img):
    global i , Cnt_Star
    img = img.astype(int)
    img += 100
    img[img>255] = 255
    img = img.astype(np.uint8)
    img = cv.medianBlur(img,7)
    hsv_img= cv.cvtColor(img, cv.COLOR_BGR2HSV) # convert to HSV    
    maskRed = cv.inRange(hsv_img,(160,50,70), (180, 255, 255)) # threshold to make red color white 
    maskYellow = cv.inRange(hsv_img , (20, 100, 100), (30, 255, 255)) # threshold to make yellow color white
   
    i+=1 #counter
    mean1 = np.mean(maskRed)
    mean2 = np.mean(maskYellow)
    #contours
    Cnt , h = cv.findContours(maskRed,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    arr2ofCircles = []
    matches = [] 
    minvalue = 10
    #matching contours for the red star
    if len(Cnt) > 0:
        for x in range(min(len(Cnt), len(Cnt_Star))):
            matches.append(cv.matchShapes(Cnt_Star[x],Cnt[x],1,0.0))
        if matches:
            minvalue = min(matches)
    
    #number of enclosing Circle from contours
    for c in Cnt:
        arr2ofCircles.append(cv.minEnclosingCircle(c))
        
    print(minvalue)
    print(len(arr2ofCircles))
    #return result
    if mean1 > 2 or mean2 > 2:
        if mean1 > mean2:
            if minvalue < .1 or len(arr2ofCircles) <= 5 :
                return 'Red Star'
            else:
                return 'Otherwise'   
        else:
            return 'Yellow Square'
    else:
        return 'Otherwise' 

#croping variables
Y1 = None
Y2 = None
segment = None

#croping the image
def crop(event, x, y ,flags , param):
    global segment , Y1 , Y2 , i
    if event == cv.EVENT_LBUTTONDBLCLK:
        if Y1 is None:
            Y1 = y
        else:
            Y2 = y
    if Y1 != None and Y2 != None:
        segment = image.copy()[min(Y1,Y2) : max(Y1,Y2) , : ]
        width = segment.shape[1]
        parts = [ segment[:, :width//3] , segment[:, width//3:int(width*2//3)]  ,segment[:, int(width*2//3):] ]
        
        #color detection and showing the image
        for part in parts:   
            label = extract_color(part)
            print(label)
            part = cv.putText(part, label , (0,part.shape[0]-10), cv.FONT_HERSHEY_SIMPLEX, 1.0,(0,255,0), 3, cv.LINE_AA, False)
            cv.imshow(f'{i}', part)

        Y1 = None 
        Y2 = None

cv.namedWindow('image')  
cv.setMouseCallback('image',crop)        

while(True):  
    cv.imshow('image',image)
    if cv.waitKey(1) & 0xFF == 27:  
        break 

cv.destroyAllWindows