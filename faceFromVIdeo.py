import cv2
from threading import Thread
from faceDetector import Face

cap = cv2.VideoCapture(0)

# class T1(Thread):
# 	def  __init__(self):
# 		Thread.__init__(self)
# 		ret, self.frame = cap.read()
# 		self.imgResized = None

# 	def run(self):
# 		self.imgResized, self.faces = FaceDetection(self.frame)


		
# class  T2(Thread):
# 	def __init__(self, img, faces):
# 		Thread.__init__(self)
# 		self.img = img
# 		self.faces = faces

# 	def run(self):
# 		Faceobj.RectAroundFace(self.faces, self.img)
# 		# cv2.imshow("faces in video", self.img)
		
# class T3(Thread):
# 	def __init__(self, img):
# 		Thread.__init__(self)
# 		self.img = img

# 	def run(self):
# 		cv2.imshow("faces in video", self.img)


class t1(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.img = cap.read()[1]
		# self.imgResized = None

	def run(self):
		# self.imgResized, self.faces = FaceDetection(self.img)
		Faceobj = Face()
		self.imgResized =  Faceobj.preprocessing(self.img)[1]
		# Faceobj.RectAroundFace(self.faces, self.imgResized)
		# cv2.imshow("Frame", self.imgResized)

class t2(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.img = cap.read()[1]
		# self.imgResized = None

	def run(self):
		self.imgResized, self.faces = FaceDetection(self.img)
		# Faceobj = Face()
		# Faceobj.RectAroundFace(self.faces, self.imgResized)
		# cv2.imshow("Frame", self.imgResized)

class t3(Thread):
	def __init__(self, frame, faces):
		Thread.__init__(self)
		# ret, self.img = cap.read()
		self.imgResized = frame
		self.faces = faces

	def run(self):
		# self.imgResized, self.faces = FaceDetection(self.img)
		Faceobj = Face()
		# Faceobj.RectAroundFace(self.faces, self.imgResized)
		Faceobj.RectAroundFace(self.faces, self.imgResized)
		cv2.imshow("Frame", self.imgResized)

		

def FaceDetection(img):
	imgPreProcessed, imgResized = Faceobj.preprocessing(img)
	faces = Faceobj.detectFace(imgPreProcessed)
	return imgResized, faces

Faceobj = Face()

while (cap.isOpened):

	# ret, frame = cap.read()
	
	# print cap.get(cv2.cv.CV_CAP_PROP_FPS)
	# cap.set(cv2.cv.VC_CAP_PROP_FPS, 60)
	
	# if not ret :
	# 	break

	# thread_1 = T1()
	# thread_1.start()
	# thread_1.join()
	# thread_2 = T2(thread_1.imgResized, thread_1.faces)
	# # thread_2()
	# thread_2.start()
	# thread_3 = T3(thread_2.img)
	# # thread_2.join()
	# thread_3.start()
	# thread_3.join()
	T1 = t1()
	T1.start()
	# T1.join()
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