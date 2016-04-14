import cv2, os, numpy as np

ResizedWidth = 60
ResizedHeight = 60

CascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(CascadePath)

images = np.zeros((0,60 * 60))
labels = []
for i in xrange(1, 41):
	
	for j in xrange(1, 10):

		imagepath = './Dataset 1/s' + str(i) + '/' + str(j) + ".pgm"
		img = cv2.imread(imagepath, 0)
		faces = faceCascade.detectMultiScale(img)
		print img.shape
		
		for (x, y, w, h) in faces:
			face = img[y: y + h, x: x + w ]
			cv2.imshow("Adding face to the detector", face)
			face = cv2.resize(face, (ResizedWidth, ResizedHeight))
			face = face.reshape((1, ResizedWidth * ResizedHeight))
			images = np.array(np.append(images, face, 0), np.float32)
			labels.append("s" + str(i))
			cv2.waitKey(50)

# images = np.array(images)
print images, labels
print images.shape
np.savetxt("FaceData.txt", images)
np.savetxt("FaceClassifier.txt", labels,  fmt = '%s')