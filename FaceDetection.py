import cv2  #open cv

alg="haarcascade_frontalface_default.xml"  #accessed the xml file
haar_cascade=cv2.CascadeClassifier(alg)    #loading xml file with cv2

cam=cv2.VideoCapture(0)   #initializing camera

while True:  #infinte loop
	_,img=cam.read()  #read the frames of the camera
	grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     #convert img into gray image
	face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)
	for (x,y,w,h) in face:  #coordinates of face
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.imshow("FaceDetection",img)
	key=cv2.waitKey(0)
	if key==27:  #esc key value
		break
cam.release()
cv2.destroyAllWindows()
