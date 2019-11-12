import os,time,cv2
from appium import webdriver

class AppSimulate:

    def __init__(self):
        self.path=os.path.abspath(".")
        imgname="big.png"
        self.filepath=self.path+"\\data"+imgname
        self.caps={}
        self.caps["platformName"]="Android"
        self.caps["platformVersion"]="4.4.2"
        self.caps["deviceName"]="Appium"
        self.caps["udid"]="127.0.0.1:62001"
        self.caps["appPackage"]="com.miui.calculator"
        self.caps["appActivity"]=".cal.CalculatorActivity"
        self.driver=webdriver.Remote("http:127.0.0.1:4723/wd/hub",self.caps)
        time.sleep(3)

    # def get_img(self):
    #     self.driver.save_screenshot(self.filepath)
    #     big = cv2.imread(self.filepath)

    def find_img(self,small_file):
        small=cv2.imread(small_file)
        self.driver.save_screenshot(self.filepath)
        big=cv2.imread(self.filepath)
        result=cv2.matchTemplate(big,small,cv2.TM_CCOEFF_NORMED)
        print(result)
        pos=cv2.minMaxLoc(result)
        print(pos)
        x=int(pos[3][0])+int(small.shape[1]/2)
        y=int(pos[3][0])+int(small.shape[0]/2)
        if pos[1]>0.8:
            return x,y
        else:
            print("not found")

    def click(self,small_file):
        x,y=self.get_img(small_file)
        self.driver.tap([(x,y)],20)

if __name__ == '__main__':
    smallpath=os.path.abspath(".")
    smallfile=smallpath+"\\data\\"
    app=AppSimulate()
    time.sleep(2)

    app.click(smallfile+'eight.png')
    time.sleep(2)
    app.click(smallfile+'plus.png')
    time.sleep(1)
    app.click(smallfile+'two.png')
    time.sleep(1)
