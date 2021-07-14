import cv2

cap=cv2.VideoCapture(r"C:\Users\HP\Downloads\videoplayback.webm")

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    edges=cv2.Canny(frame,100,200)
    if not ret:
        print("can't receive frame")
        break
    cv2.imshow("video",frame)
    cv2.imshow("edges",edges)
    if cv2.waitKey(1) == 27: 
        break              #if you press escape
cap.release()
cv2.destroyAllWindows()
