from imutils.video import VideoStream
import numpy as np
from imutils.video import FPS
import imutils
import time
import cv2
from keras.models import load_model
import pyscreenshot as ImageGrab
from datetime import datetime

print("[INFO] starting video stream...")

# Loading the video file
cap = cv2.VideoCapture('helmet-detected.avi') 
d=0
# Starting the FPS calculation
fps = FPS().start()
while True:
	try:
		ret,frame = cap.read()
		frame = imutils.resize(frame,width=450,height=500)
		time.sleep(0.25)
	except:
		pass

	cv2.imshow('Frame',frame)
	key = cv2.waitKey(1) & 0xFF
	
	if key == ord('q'): # if 'q' key is pressed, break from the loop
		break
	fps.update()

fps.stop()
cv2.destroyAllWindows()
cap.release()