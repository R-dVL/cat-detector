import cv2

class Camera:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.cap = cv2.VideoCapture(self.id)

    def take_picture(self, path, img):
        cv2.imwrite(path, img)

motionCam = Camera("Motion", 1)