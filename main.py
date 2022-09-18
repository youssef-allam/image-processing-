import cv2 as cv
import numpy as np
#get all needed images
image = cv.imread('photos/Gray-wolf.jpg', 0)
image1 = cv.imread('photos/Gray-wolf1.jpg', 0)
image2 = cv.imread('photos/img1.jpg', 0)
image3 = cv.imread('photos/img3.jpg', 0)
image4 = cv.imread('photos/wolf.jpg', 0)

#making all imgs at same size
image = cv.resize(image , (480 ,270))
image1 = cv.resize(image1 , (480 ,270))
image2 = cv.resize(image2 , (480 ,270))
image3 = cv.resize(image3 , (480 ,270))
image4 = cv.resize(image4 , (480 ,270))

#rotaing and image for feature matching 
image1_R = cv.rotate(image1 , cv.ROTATE_180)

########################################## Task 1 ################################

def display4imges(img1,img2, img3 , img4):
   
    #collecting 4 images in 2X2 figure
    new_img1 = np.concatenate((img2 , img1), axis = 1)
    new_img2 = np.concatenate((img3 , img4), axis = 1)
    new_img = np.concatenate((new_img1 , new_img2), axis = 0) 
    #display the window of images
    cv.imshow('4 imgs', new_img)
    cv.waitKey(0)
    cv.destroyAllWindows

# display4imges(image, image1,image2 , image3)


########################################### Task 2 ###############################

def BFmatcher_ORB(img1,img2):
    # Initiate ORB detector
    orb = cv.ORB_create()
    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)
    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1,des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)
    # Draw first 10 matches.
    img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:4000],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow('BFmather_ORB', img3)
    cv.waitKey(0)
    cv.destroyAllWindows

# BFmatcher_ORB(image1, image1_R)

def BFmatcher_SIFT(img1 , img2):
    # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    # BFMatcher with default params
    bf = cv.BFMatcher(cv.NORM_L2 )
    matches = bf.knnMatch(des1,des2,k=2)
    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    # cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow('BFmatcher_SIFT' , img3)
    cv.waitKey(0)
    cv.destroyAllWindows


# BFmatcher_SIFT(image1 , image1_R)

def F_BMatcher(img1 , img2):
    # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    
    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]

    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matchesMask[i]=[1,0]

    draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = cv.DrawMatchesFlags_DEFAULT)
    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    cv.imshow('FlaNN_macther' , img3)
    cv.waitKey(0)
    cv.destroyAllWindows

# F_BMatcher(image1 , image1_R)

########################################### Task 3 #############################

def to_zeros(img, threshold):
    # THRESH_TOZEROS using Numpy
    imgx = img.astype(int) 
    imgx[imgx < threshold] = 0 
    img = imgx.astype('uint8')
    #show the image 
    cv.imshow('TO_ZEROS' , img)
    cv.waitKey(0)
    cv.destroyAllWindows

# to_zeros(image1 , 20)

########################################### Task 5 #############################

def sharpen(img , amount):
    a = np.array([[0, 0 , 0],
                [0, 1 ,0],
                [0, 0 , 0]])

    b = np.array([[0, -1 , 0],
                [-1, 5 ,-1],
                [0, -1 , 0]])
    
    kernel = a + b*amount #calculating the kernel

    filterd_img = cv.filter2D(img, -1 ,kernel)
    cv.imshow('sharpen' , filterd_img)
    cv.waitKey(0)
    cv.destroyAllWindows

# sharpen(image1, 1)

########################################### Task 6 #############################


def canny_edge(img):
    img =cv.GaussianBlur(img,(5,5),0) # bluring the image 
    canny_img = cv.Canny(img,78,69) #edge detection
    cv.imshow('canny-edged' , canny_img)
    cv.waitKey(0)
    cv.destroyAllWindows

# canny_edge(image4)

################### the code to get best values for canny thresholds ###############

# def catch(Lower=0):
#     Lower = cv.getTrackbarPos('Lower', 'canny')
#     Upper = cv.getTrackbarPos('Upper', 'canny')
#     edge = cv.Canny(image, Lower, Upper)
#     cv.imshow('canny', edge)

# while True:
#     image=image4.copy()
#     image=cv.GaussianBlur(image,(5,5),0)
#     cv.namedWindow('canny')
#     Lower=1
#     Upper=1
#     cv.createTrackbar('Lower','canny',Lower,255,catch)
#     cv.createTrackbar('Upper','canny',Upper,255,catch)
#     cv.imshow('Frame',image4)
#     k = cv.waitKey(0)
#     if k : 
#         break
# cv.destroyAllWindows()