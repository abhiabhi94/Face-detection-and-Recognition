import cv2, numpy as np
from faceDetector import Face
faceDB = np.load("FaceData.npy")
labels = np.load("FaceClassifier.npy")
imgPath = "face3.JPG"
# count = 0
# CascadePath = "haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(CascadePath)
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.train(faceDB, labels)

match = {
	1 : "Abheet",
	2 : "Abhyudai",
	3 : "Deepesh",
	4 : "Diksha",
	5 : "Harshit",
	6 : "Karan",
	7 : "Prerit",
	8 : "Ved"
}

img = cv2.imread(imgPath)
Faceobj = Face()
imgPreProcessed, imgResized = Faceobj.preprocessing(img)
faces = Faceobj.detectFace(imgPreProcessed)
Faceobj.RectAroundFace(faces, imgResized)

for face in faces:
	(x, y, w, h) = face
	newFace = imgResized[y : y + h, x : x + w]
	cv2.imshow("Face", newFace)
	cv2.waitKey(100)
	cv2.destroyAllWindows()
	newFace = cv2.cvtColor(newFace, cv2.COLOR_BGR2GRAY)
	predictedFace, conf = recognizer.predict(newFace)
	cv2.putText(imgResized, match[predictedFace](), (x + 3, y + 3), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0))



cv2.imshow("Faces found", imgResized)
cv2.waitKey(0)