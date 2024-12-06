import cv2

# id of the default video capturing device to open.abs
# by default the inbuild video will open
capture = cv2.VideoCapture(0)

while True:
    _,frame = capture.read()
    cv2.imshow("Capture from Webcam", frame)

    if cv2.waitKey(1) == 27: # ASCII code for escape is 27.
        break

capture.release()
cv2.destroyAllWindows()

