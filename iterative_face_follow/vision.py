
import cv2
import sys

class TelloVision:
    """Wrapper class to enable the Tello Vision."""

    def __init__(self,tello):
        self.tello = tello
        cascPath = "./facialRecognitionModel.xml"
        if len(sys.argv) == 2:
            cascPath = sys.argv[1]
        self.faceCascade = cv2.CascadeClassifier(cascPath)

    def getFaceQuadrant(self, x,y,w,h, left, right):
        # Returns the quadrant of the image that the face is in.
        center = x+(w//2)
        # print("x:",x,"w:",w)
        # print("center: ", center)
        if (center < left):
            return -1
        if (center < right):
            return 0
        return 1

    def draw(self):
        """
        Renders the camera footage of Tello along with video changes
        """
        try:
            while not self.stopEvent.is_set():                

            # read the frame for GUI show
                self.frame = self.tello.read()
                if self.frame is None or self.frame.size == 0:
                    continue 
                # print(type(self.frame))
                # print(self.frame.shape)

                gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

                faces = self.faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags = cv2.CASCADE_SCALE_IMAGE
                )

                left = int(960*.4)
                right = int(960*.6)

                if (len(faces) > 0):
                    biggestFaceIndex = 0
                    biggestWidth = 0
                    for idx,box in enumerate(faces):
                        x,y,w,h = box
                        if (w > biggestWidth):
                            biggestFaceIndex = idx
                    x, y, w, h = faces[biggestFaceIndex]
                    quad = self.getFaceQuadrant(x,y,w,h, left, right)
                    cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.rectangle(self.frame, (left, 0), (left + 1, 700), (255, 0, 0), 2)
                cv2.rectangle(self.frame, (right, 0), (right + 1, 700), (255, 0, 0), 2)
            # transfer the format from frame to image         
            # image = Image.fromarray(self.frame)
        except RuntimeError, e:
            print("[INFO] caught a RuntimeError")
