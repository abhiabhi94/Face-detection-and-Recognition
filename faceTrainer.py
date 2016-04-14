import cv2, os, numpy as np

ResizedWidth = 65
ResizedHeight = 65

CascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(CascadePath)

images = []
labels = []
for i in xrange(1, 41):
	
	for j in xrange(1, 10):

		imagepath = './Dataset 1/s' + str(i) + '/' + str(j) + ".pgm"
		img = cv2.imread(imagepath, 0)
		faces = faceCascade.detectMultiScale(img)
		
		for (x, y, w, h) in faces:
			face = img[y: y + h, x: x + w ]
			cv2.imshow("Adding face to the detector", face)
			face = cv2.resize(face, (ResizedWidth, ResizedHeight))
			# face = face.reshape((1, ResizedWidth * ResizedHeight))
			# images = np.array(np.append(images, face, 0), np.float32)
			images.append(face)
			labels.append("s" + str(i))
			cv2.waitKey(50)

# images = np.array(images)
# print images, labels
# print images.shape
np.save("FaceData.npy", images)
np.save("FaceClassifier.npy", labels)