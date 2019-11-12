from pykeyboard import PyKeyboard
from pymouse import PyMouse
import random,time,uiautomation,os
class folishMonkey:
    def __init__(self):
        self.keyboard=PyKeyboard()
        self.mouse=PyMouse()
    def random_location(self):
        x = random.randint(0, 1300)
        y = random.randint(0, 800)
        return (x,y)

    #随机移动
    def random_move(self):
        x,y=self.random_location()
        self.mouse.move(x,y)

    #单击
    def click(self):
        x,y=self.random_location()
        self.mouse.click(x,y)
    #双击
    def double_click(self):
        x,y=self.random_location()
        self.mouse.click(x,y,n=2)

    #右击
    def right_click(self):
        x,y=self.random_location()
        self.mouse.click(x,y,button=2)
    #随机移动后输入字符串
    def input_str(self):
        self.random_move()
        self.keyboard.type_string("hello")
    #随机按键
    def presskey(self):
        key_list=[self.keyboard.control_key,self.keyboard.shift_key,self.keyboard.backspace_key]
        key=random.choice(key_list)
        self.keyboard.press_key(key)
        self.keyboard.release_key(key)
    #组合按键
    def presskeys(self):
        keys_list=[[self.keyboard.control_key,self.keyboard.shift_key],[self.keyboard.enter_key,'c'],
                   [self.keyboard.tab_key,self.keyboard.alt_key,'v']]
        keys=random.choice(keys_list)
        self.keyboard.press_keys(keys)
        self.keyboard.release_key(keys)
    #打开应用
    def open_application(self,exe):
        os.popen(exe)
    #获取窗口矩形
    def get_appRectangle(self,name):
        window=uiautomation.WindowControl(name)
        con=window.BoundingRectangle
    # def write_log(self):

    #运行函数
    def start(self,count):
        for i in range(0,count):
            num=random.randint(0,100)
            if num<20:
                self.random_move()
            elif num<40:
                self.click()
            elif num<50:
                self.double_click()
            elif num<60:
                self.right_click()
            elif num<80:
                self.input_str()
            else:
                self.presskey()
            time.sleep(1)

if __name__ == '__main__':

    monkey=folishMonkey()
    monkey.start(20)


