import cv2, sys

# Get user supplied values
imgPath = "face2.JPG"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
recognizer = cv2.createLBPHFaceRecognizer()

class Face():

	def preprocessing(self, img):

		RP = img.shape[0] / 800 if img.shape[0] <= img.shape[1] else img.shape[1] / 800
		imgResized = cv2.resize (img, (img.shape[1] / RP, img.shape[0] / RP))
		gray = cv2.cvtColor(imgResized, cv2.COLOR_BGR2GRAY)
		return gray, imgResized

	# Detect faces in the image
	def detectFace(self, gray):
		faces = faceCascade.detectMultiScale(
		    gray,
		    scaleFactor = 1.1,
		    minNeighbors = 5,
		    minSize = (30, 30),
		    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		print "Found {0} faces!".format(len(faces))
		return faces

	# Draw a rectangle around the faces
	def RectAroundFace(self, faces, imgResized):
		for (x, y, w, h) in faces:
		    cv2.rectangle(imgResized, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# Face Recognizer


img = cv2.imread(imgPath)
Faceobj = Face()
imgPreProcessed, imgResized = Faceobj.preprocessing(img)
faces = Faceobj.detectFace(imgPreProcessed)
Faceobj.RectAroundFace(faces, imgResized)
cv2.imshow("Faces found", imgResized)
cv2.waitKey(0)
	# print img.shape, imgResized.shape