import cv2

class Camera:
    # Constructor, id will define what camera is selected
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.video = cv2.VideoCapture(self.id)

    def __del__(self):
        self.video.release()

    def getFrame(self):
        success, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    # Saves actual frame
    def takePhoto(self, path, img):
        cv2.imwrite(path, img)

    # Returns camera capture read
    def getVideo(self):
        return self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def motionDetector(camera):
    ret, frame1 = camera.getVideo()
    ret, frame2 = camera.getVideo()
    counter = 0

    while camera.video.isOpened():
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
                camera.takePhoto("motion.jpeg", frame1)
                counter += 1
            elif counter > 100:
                counter = 0
            else:
                counter += 1

        # Contour drawing
        # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        frame1 = frame2
        ret, frame2 = camera.getVideo()

        if cv2.waitKey(50) == 27:
            break

    camera.video.release()
    cv2.destroyAllWindows()

motionCam = Camera("Motion Camera", 0)