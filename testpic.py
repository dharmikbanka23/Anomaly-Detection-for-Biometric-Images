import cv2
import sys
imagePath=sys.argv[1]

image=cv2.imread(imagePath)
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces=faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(int(image.shape[1]*0.3),int(image.shape[1]*0.3)))

if len(faces)==1:
	print("1")
else:
	print("0")

"""for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

status = cv2.imwrite('faces_detected.jpg', image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)"""