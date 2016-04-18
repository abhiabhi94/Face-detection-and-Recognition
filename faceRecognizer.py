import cv2, numpy as np
from faceDetector import Face
faceDB = np.load("friendlyFaces.npy")
labels = np.load("friendlyFacesClassifier.npy")
imgPath = "sample 5.JPG"
count = 0  # For stopping the program from running infinetly by limiting the rotation
# CascadePath = "haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(CascadePath)
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.train(faceDB, labels)

def FaceDetection(img):
	imgPreProcessed, imgResized = Faceobj.preprocessing(img)
	faces = Faceobj.detectFace(imgPreProcessed)
	return imgPreProcessed, imgResized, faces

def match(i):
	m={
		1 : "Abheet",
		2 : "Abhyudai",
		3 : "Deepesh",
		4 : "Diksha",
		5 : "Harshit",
		6 : "Karan",
		7 : "Prerit",
		8 : "Ved"
	}
	return m[i]


img = cv2.imread(imgPath)
Faceobj = Face()
imgPreProcessed, imgResized, faces = FaceDetection(img)

while (len(faces) == 0 and count < 3):
	print "Now Rotating..."
	count += 1
	# print count
	# cv2.imshow("  ", imgPreProcessed)
	rows, cols, channel = imgResized.shape
	# print imgPreProcessed.shape[0], imgPreProcessed.shape[1]
	img = cv2.warpAffine(imgResized,
						cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1) ,
						(cols, rows)
	)
	# cv2.imshow("Rotated Image", img)
	# cv2.waitKey(1000)

	imgPreProcessed, imgResized, faces = FaceDetection(img)

Faceobj.RectAroundFace(faces, imgResized)


for face in faces:
	(x, y, w, h) = face
	newFace = imgResized[y : y + h, x : x + w]
	# cv2.imshow("Face", newFace)
	# cv2.waitKey(100)
	# cv2.destroyAllWindows()
	newFace = cv2.cvtColor(newFace, cv2.COLOR_BGR2GRAY)
	predictedFace, conf = recognizer.predict(newFace)
	cv2.putText(imgResized, match(predictedFace), (x - 2, y + 1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
	print "{} predicted with a confidence {}".format(match(predictedFace), conf)




cv2.imshow("Faces found", imgResized)
cv2.waitKey(0)