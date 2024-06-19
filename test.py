from imageai.Detection.Custom import CustomVideoObjectDetection
import os
import threading
import time

from imutils.video import VideoStream
import numpy as np
from imutils.video import FPS
import imutils
import cv2
from keras.models import load_model
import pyscreenshot as ImageGrab
from datetime import datetime

execution_path = os.getcwd()

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath("detection_model-ex-024--loss-0012.095.h5")
video_detector.setJsonPath("detection_config.json")
video_detector.loadModel()

def a():
	video_detector.detectObjectsFromVideo(input_file_path="vid1.m4v",output_file_path=os.path.join(execution_path, "helmet-detected"),frames_per_second=15,minimum_percentage_probability=40,log_progress=True)

def b():
	pass
	# time.sleep(50)
	# while True:
	# 	print("start")
	# 	print("[INFO] starting video stream...")

	# 	# Loading the video file
	# 	cap = cv2.VideoCapture('helmet-detected.avi') 
	# 	d=0
	# 	# Starting the FPS calculation
	# 	fps = FPS().start()
	# 	while True:
	# 		try:
	# 			ret,frame = cap.read()
	# 			frame = imutils.resize(frame,width=1080,height=1920)
	# 			time.sleep(0.25)
	# 		except:
	# 			pass

	# 		cv2.imshow('Frame',frame)
	# 		key = cv2.waitKey(1) & 0xFF
			
	# 		if key == ord('q'): # if 'q' key is pressed, break from the loop
	# 			break
	# 		fps.update()

	# 	fps.stop()
	# 	cv2.destroyAllWindows()
	# 	cap.release()

threading.Thread(target=a).start()
threading.Thread(target=b).start()


