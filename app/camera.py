import cv2

class camera:
    # Constructor, id will define what camera is selected
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.cap = cv2.VideoCapture(self.id)

    # Saves actual frame
    def takePhoto(self, path, img):
        cv2.imwrite(path, img)

    # Returns camera capture read
    def readCap(self):
        return self.cap.read()

motionCam = camera("Motion Camera", 0)