import cv2
from camera import motionCam

# Motion detection loop, it works comparing pixel differences between frame1 and frame2
def start():
    ret, frame1 = motionCam.readCap()
    ret, frame2 = motionCam.readCap()
    counter = 0

    while motionCam.cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(
            dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)

            # Sensibility
            if cv2.contourArea(contour) < 900:
                continue

            # Draw motion rectangle
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Text in image when something is detected
            cv2.putText(frame1, "Status: {}".format('Gati detectado!'), (10, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                       1, (255, 0, 0), 3)

            # To discard fake motion detection, it waits 100 iterations before taking a picture
            if counter == 100:
                motionCam.takePhoto("motion.jpeg", frame1)
                counter += 1
            elif counter > 100:
                counter = 0
            else:
                counter += 1

        # Contour drawing
        # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        frame1 = frame2
        ret, frame2 = motionCam.readCap()

        if cv2.waitKey(50) == 27:
            break

    motionCam.cap.release()
    cv2.destroyAllWindows()