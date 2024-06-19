#!/usr/bin/python
# -*- coding: utf-8 -*-
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

from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk


class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.vid_path = ''
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title('Grp 44-Helmet Detection')
		menu = Menu(self.master)
		self.master.config(menu=menu)

        # menu

		file = Menu(menu)
		file.add_command(label='Save')
		file.add_command(label='Exit', command=self.close)
		menu.add_cascade(label='File', menu=file)

		edit = Menu(menu)
		edit.add_command(label='Redo')
		edit.add_command(label='Undo')
		menu.add_cascade(label='Edit', menu=edit)

        # Select the video feed from your Device

		pic_button = Button(root, text='Get the Video File', fg='black', bg='#66ccff', width=20, command=self.add_vid)
		pic_button.place(x=75,y=40)

        # Add the selected Video

		add = Button(root, text='Add', fg='black', bg='#66ccff', width=12,command=self.load_vid)
		add.place(x=100,y=80)

		close = Button(root, text='Close', fg='white', bg='black', width=12,command=self.close)
		close.place(x=100,y=120)

	def add_vid(self):
		self.vid_path = filedialog.askopenfilename(initialdir='/',title='Select an image file', filetypes=(('MP4 files','*.mp4'), ('All files', '*.*')))
		print(self.vid_path)

	def b():
		time.sleep(70)
		while True:
			print("start")
			print("[INFO] starting video stream...")

			# Loading the video file
			cap = cv2.VideoCapture('helmet-detected-op.avi') 
			d=0
			# Starting the FPS calculation
			fps = FPS().start()
			while True:
				try:
					ret,frame = cap.read()
					frame = imutils.resize(frame,width=500,height=450)
					time.sleep(0.25)
				except:
					pass

				cv2.imshow('Frame',frame)
				key = cv2.waitKey(1) & 0xFF
				
				if key == ord('q'): # if 'q' key is pressed, break from the loop
					quit()
				fps.update()

			fps.stop()
			cv2.destroyAllWindows()
			cap.release()

	def load_vid(self):
		execution_path = os.getcwd()
		video_detector = CustomVideoObjectDetection()
		video_detector.setModelTypeAsYOLOv3()
		video_detector.setModelPath('detection_model-ex-024--loss-0012.095.h5')
		video_detector.setJsonPath('detection_config.json')
		video_detector.loadModel()
		th = threading.Thread(target=Window.b)
		th.start()
		video_detector.detectObjectsFromVideo(input_file_path=self.vid_path,output_file_path=os.path.join(execution_path,'helmet-detected-op'), frames_per_second=15,minimum_percentage_probability=40,log_progress=True)
		th.join()

	def close(self):
		exit()

root = Tk()
root.geometry('300x200')

if __name__ == '__main__':
    app = Window(root)

root.mainloop()
