import cv2
from threading import Thread


'''
class camera:
    def __init__(self):
        
        self.cap=cv2.VideoCapture(0)
        _, self.image=self.cap.read()
        
        self.running=True
        
    def start(self):
        Thread(target=self.update, args=()).start()
        return self
    
    def updateCap(self,capturedevice):
        self.cap.release()
        self.cap=cv2.VideoCapture(capturedevice)
        
    def getImg(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        return image
    
    def stop(self):
        self.cap.release()
        self.running=False
    
    def update(self):
        while self.running:
            try:
                _, self.image=self.cap.read()
                #self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
            except Exception as e:
                print(e)
                self.running=False
'''


#sudo camera class 
class camera:
    def __init__(self):
       
        self.image=cv2.imread("test0.jpg")
        
        self.zoom=25
        
        width = int(self.image.shape[1] * self.zoom / 100)
        height = int(self.image.shape[0] * self.zoom / 100)
    
        self.image=cv2.resize(self.image, (width, height), interpolation = cv2.INTER_AREA)
        
    def start(self):
        return self
    
    def updateCap(self,capturedevice):
        pass
        
    def getImg(self):
        return self.image
    
    def stop(self):
        pass
    
