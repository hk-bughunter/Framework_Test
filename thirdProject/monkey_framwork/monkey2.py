from pykeyboard import PyKeyboard
from pymouse import PyMouse
from functools import wraps
import random,time,uiautomation,os

class clevermonkey:

    def writelog(func):
        @wraps(func)
        def wrapfunction(*args,**kwargs):
            func(*args,**kwargs)
            with open('path','a',encoding='utf-8') as file:
                file

    #生成随机字符串
    # def

    #获取应用窗口
    def get_appRectangle(self,name):
        window=uiautomation.WindowControl(Name=name)
        con=window.BoundingRectangle
        print(con)

if __name__ == '__main__':
    monkey=clevermonkey()
    name='计算器'
    monkey.get_appRectangle(name)
