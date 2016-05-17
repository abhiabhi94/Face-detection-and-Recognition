import cv2
from threading import Thread
from faceDetector import Face

cap = cv2.VideoCapture(0)


class t1(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.img = cap.read()[1]

	def run(self):
		Faceobj = Face()
		self.imgResized =  Faceobj.preprocessing(self.img)[1]

class t2(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.img = cap.read()[1]

	def run(self):
		self.imgResized, self.faces = FaceDetection(self.img)

class t3(Thread):
	def __init__(self, frame, faces):
		Thread.__init__(self)
		self.imgResized = frame
		self.faces = faces

	def run(self):
		Faceobj = Face()
		Faceobj.RectAroundFace(self.faces, self.imgResized)
		cv2.imshow("Frame", self.imgResized)

		

def FaceDetection(img):
	imgPreProcessed, imgResized = Faceobj.preprocessing(img)
	faces = Faceobj.detectFace(imgPreProcessed)
	return imgResized, faces

Faceobj = Face()

while (cap.isOpened):
	T1 = t1()
	T1.start()
	T2 = t2()
	T2.start()
	T2.join()
	T3 = t3(T1.imgResized, T2.faces)
	T3.start()
	T1.join()
	T3.join()
	# cv2.imshow('frame',frame)
	if (cv2.waitKey(1) & 0xFF == 27):
		break

cv2.destroyAllWindows()