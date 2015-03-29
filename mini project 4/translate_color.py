"""Initial foray into image tracking with colors using OpenCV
adding step of translating images to animations"""
import cv2
import numpy as np
import pygame
import pygame.locals
import sys

kernel = np.ones((21,21),'uint8')
cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
    fram = cv2.blur(frame,(3,3))
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    thresh = cv2.inRange(hsv,np.array(lower_blue),(upper_blue))
    thresh2 = thresh.copy()

    # find contours in the threshold img
    contours,hierarchy= cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt

    # finding centroids of best_cnt and draw a circle there
    M = cv2.moments(best_cnt)
    
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv2.circle(frame,(cx,cy),5,255,-1)

    cv2.imshow('Original',frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""
def move_objects():
    screen = pygame.display.set_mode((640,480))
    screen.fill((255, 255, 255))
    pygame.init()

    while (True):

       # check for quit events
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit(); sys.exit();

       # draw the updated picture
       pygame.draw.rect(screen, (0,255,0), (0,0,10,5), 50)
       pygame.rect.move(cx,cy)
       # update the screen
       pygame.display.update()
       """

#When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
