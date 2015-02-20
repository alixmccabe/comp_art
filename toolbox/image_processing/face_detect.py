""" Experiment with face detection and image filtering using OpenCV """
import cv2
import numpy as np

def draw_eyes(size, color, frame,x,y):
    #this draws the white circle and blue iris for our left eye!
    cv2.circle(frame, (x+70,y+80), size, (255, 255, 255), thickness=-1, lineType=8, shift=0)
    cv2.circle(frame, (x+75,y+75), size/2, (color), thickness=-1, lineType=8, shift=0)

    #this draws the white circle and blue iris for our right eye!
    cv2.circle(frame, (x+140,y+80), size, (255, 255, 255), thickness=-1, lineType=8, shift=0)
    cv2.circle(frame, (x+135,y+85), size/2, (color), thickness=-1, lineType=8, shift=0)

def draw_ellipse(width, height, thickness, frame,x,y):
    #this draws a part of an ellipse as a red mouth for our cartoon face!
    cv2.ellipse(frame, (x+90,y+145), (width, height),0, 0, 180, (0,0,255),thickness)
    cv2.ellipse(frame, (x+140,y+145), (width, height),180, 0, 180, (0,0,255),thickness)

def draw_face():
    kernel = np.ones((21,21),'uint8')
    cv2.destroyAllWindows()
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

    while(True):
        #capture frame-by-frame
            
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
        for (x,y,w,h) in faces:
            frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)

            draw_eyes(20, (255,255,0), frame,x,y)

            draw_ellipse(25,25,5,frame,x,y)

        #Display resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    draw_face()