import cv2
cap=cv2.VideoCapture(0) #for one more webcom videocapture(0)

while True:
    ret,img=cap.read() #img object for video reading
    cv2.imshow ('Webcom',img) #add cv object with GUI and img object
    k=cv2.waitKey(10) #key for resume the webcam video
    if k==27: #click the escape then webcam is break(off)
        break;

cap.release() #close the videocapture
cv2.destoryAllWindow() #close the cv