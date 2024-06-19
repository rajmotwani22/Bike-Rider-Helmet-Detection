from imageai.Detection.Custom import CustomObjectDetection
import os

execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("detection_model-ex-024--loss-0012.095.h5") 
detector.setJsonPath("detection_config.json")
detector.loadModel()

i=1
directory = 'Images'
for filename in os.listdir(directory):
	print(os.path.join(directory, filename))
	
	detections = detector.detectObjectsFromImage(input_image=os.path.join(directory,filename), output_image_path=os.path.join('Detected-Images',"helmet-detected"+str(i)+".png"))
	i=i+1
	for detection in detections:
		if (detection["name"]=="Without Helmet"):
			print("Success")
		print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])



