import cv2
import config
from camera import motionCam
import bot

def start():
    ret, frame1 = motionCam.cap.read()
    ret, frame2 = motionCam.cap.read()
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
            if cv2.contourArea(contour) < 900:
                continue
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: {}".format('Puma detectado!'), (10, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                       1, (255, 0, 0), 3)

            if counter == 100:
                motionCam.take_picture("/home/rdvl/Proyectos/cat-detector/data/motion.jpeg", frame1)
                bot.send_foto("/home/rdvl/Proyectos/cat-detector/data/motion.jpeg")
                counter += 1
            elif counter > 100:
                counter = 0
            else:
                counter += 1

        # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        #cv.imshow("Video", frame1)
        frame1 = frame2
        ret, frame2 = motionCam.cap.read()

        if cv2.waitKey(50) == 27:
            break

    motionCam.cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start()