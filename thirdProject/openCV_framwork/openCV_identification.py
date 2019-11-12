import cv2,os,time
from PIL import ImageGrab
#
class MyCv:
#     def __init__(self):
#         path=os.path.abspath('.')
#         name=time.strftime('%H%M%s.png')
#         self.file=path+'\\'+name
#         print(self.file)
#
#     def find_image(self):
#         small=cv2.imread('login.png')
#         ImageGrab.grab().save(self.file)
#         big=cv2.imread(self.file)
#         result=cv2.matchTemplate(big,small,cv2.TM_CCOEFF_NORMED)
#         pos=cv2.minMaxLoc(result)
#         small_rg=small.shape
#         print(pos)
#         print(small_rg)
#
#
# if __name__ == '__main__':
#     d=MyCv()
#     d.find_image()


    def __init__(self):
        os.popen(r"C:\Users\Administrator.USER-20190305CL\AppData\Local\Google\Chrome\Application\chrome.exe")
        time.sleep(2)
        path = os.path.abspath(".")
        self.file = path+"\\"+"big.png"
        big = ImageGrab.grab().save(self.file)
    def getImg(self):
        small = cv2.imread("login.png")
        big = cv2.imread(self.file)
        result = cv2.matchTemplate(big,small,cv2.TM_CCOEFF_NORMED)
        pos = cv2.minMaxLoc(result)
        small_re = small.shape
        print(pos)
        print(small_re)

if __name__ == '__main__':
    cv = MyCv()
    cv.getImg()