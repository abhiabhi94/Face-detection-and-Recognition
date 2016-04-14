import cv2, numpy as np

faces = np.load("FaceData.npy")
labels = np.load("FaceClassifier.npy")

ImgPath = ""
CascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(CascadePath)

img = cv2.imread(ImgPath)
