import cv2, os, numpy as np

CascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(CascadePath)

images= np.empty((0, 100))
labels = []
for i in xrange(1, 41):
	
	for j in xrange(1, 10):

		imagepath = './Dataset 1/s' + str(i) + '/' + str(j) + ".pgm"
		img = cv2.imread(imagepath, 0)
		faces = faceCascade.detectMultiScale(img)
		print img.shape
		
		for (x, y, w, h) in faces:
			face = img[y: y + h, x: x + w ]
			print face.shape
			face = cv2.resize(face, (100, 100))
			images= np.array(np.append(images, face, 0), np.float32)
			labels.append("s" + str(i))
			cv2.imshow("Adding face to the detector", face)
			cv2.waitKey(50)

# images = np.array(images)
np.savetxt("FaceData.txt", images)
np.savetxt("FaceClassifier.txt", labels,  fmt = '%s')