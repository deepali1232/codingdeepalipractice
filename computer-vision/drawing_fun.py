import cv2
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
cap=cv2.VideoCapture(r"C:\Users\HP\Downloads\videoplayback.webm")

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    edges=cv2.Canny(frame,100,200)
    if not ret:
        print("can't receive frame")
        break
    #cv2.imshow("video",frame)
    cv2.rectangle(frame,(100,100),(300,300),(0,255,0),3)
    cv2.circle(frame,(300,300),100,(0,0,255),2)
    cv2.putText(frame,'created by divya',(50,400),font,1,(255,0,255),1)
    cv2.imshow("drawing",frame)
    if cv2.waitKey(1) == 27: 
        break              #if you press escape
cap.release()
cv2.destroyAllWindows()

