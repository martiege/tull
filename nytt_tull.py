import numpy as np
import cv2
import time
from com_node import notify_detetection

cap = cv2.VideoCapture(0)
detected = False

start_time_CINA = 0
start_time_ML = time.time()

def ML(frame):
    return time.time() - 10 > start_time_ML

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the flipped frame
        if ML(frame) and not detected:
            detected = True
            start_time_CINA = time.time()
            
        
        if detected:
            if (time.time() - 5 < start_time_CINA): 
                out.write(frame)
                cv2.imshow('frame',frame)
            else: 
                notify_detetection('output.avi')
        

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()