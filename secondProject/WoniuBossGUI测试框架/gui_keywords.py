from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from functools import wraps
import time
class Keywords:
    """关键字框架类"""
    def writeLog(func):
        """执行日志装饰器"""
        @wraps(func)
        def wrapFunction(*args,**kwargs):
            re,title=func(*args,**kwargs)
            msg = f"{re}：{title}"+"\n"
            with open("gui_testlog.txt","a",encoding="utf-8") as f:
                f.write(msg)
        return wrapFunction
    @classmethod
    def goto(cls,driver,karg):
        """进入"""
        driver.get(karg[1])
    @classmethod
    def input(cls,driver,karg):
        """输入"""
        if karg[1].startswith('xpath'):
            find_data = karg[1][6:]
            driver.find_element('xpath',find_data).send_keys(karg[2])
        else:
            find_data = karg[1][3:]
            driver.find_element('id',find_data).send_keys(karg[2])
    @classmethod
    def singleclick(cls,driver,karg):
        """单击"""
        if karg[1].startswith('xpath'):
            find_data = karg[1][6:]
            driver.find_element('xpath', find_data).click()
        else:
            find_data = karg[1][3:]
            driver.find_element('id', find_data).click()

    @classmethod
    @writeLog
    def checklen(cls,driver,karg,title):
        """检查长度"""
        if karg[1].startswith('xpath'):
            find_data = karg[1][6:]
            ele = driver.find_elements('xpath', find_data)
        else:
            find_data = karg[1][3:]
            ele = driver.find_elements('id', find_data)
        if len(ele) == int(karg[2]):
            print('验证成功。实际查询结果的数量为',len(ele),".",'定义的查询结果数量为',karg[2])
            return "测试成功",title
        else:
            print('验证失败！际查询结果的数量为',len(ele),".",'定义的查询结果数量为',karg[2])
            return "测试失败",title

    @classmethod
    @writeLog
    def checktext(cls,driver,karg,title):
        """检查文本"""
        if karg[1].startswith('xpath'):
            find_data = karg[1][6:]
            content = driver.find_element('xpath',find_data).text
        else:
            find_data = karg[1][3:]
            content = driver.find_element('id',find_data).text
        if karg[2] == content:
             print('验证成功，需求文本内容为:',karg[2]+',实际内容为:',content,'.')
             return "测试成功",title
        else:
            print('验证失败，需求文本内容为:',karg[2]+',实际内容为:', content,'.')
            return "测试失败",title

    @classmethod
    @writeLog
    def checkin(cls,driver,karg,title):
        """检查元素是否在文本中"""
        if karg[1].startswith('xpath'):
            find_data = karg[1][6:]
            content = driver.find_element('xpath', find_data).text
        else:
            find_data = karg[1][3:]
            content = driver.find_element('id', find_data).text
        if karg[2] in content:
            print('验证成功，需求文本内容为:', karg[2]+',在', content,'中.')
            return "测试成功",title
        else:
            print('验证失败，需求文本内容为:', karg[2]+',不在', content,'中.')
            return "测试失败",title

    @classmethod
    def delay(cls,driver,karg):
        """等待时间"""
        time.sleep(int(karg[1]))

    @classmethod
    def over(cls,driver,karg):
        """结束"""
        driver.close()

    @classmethod
    def hover(cls,driver,karg):
        """悬浮窗口"""
        if karg[1].startswith('xpath'):
            find_style=karg[1][:5]
            find_data = karg[1][6:]
        else:
            find_style = karg[1][:2]
            find_data = karg[1][3:]
        if karg[2].startswith('xpath'):
            hav_style=karg[2][:5]
            hav_data = karg[2][6:]
        else:
            hav_style = karg[2][:2]
            hav_data = karg[2][3:]
        setting = driver.find_element(find_style,find_data)
        ActionChains(driver).move_to_element(setting).perform()
        time.sleep(1)
        driver.find_element(hav_style, hav_data).click()

    @classmethod
    def switchwindow(cls,driver,karg):
        """切换窗口"""
        now_window = driver.current_window_handle
        for window in driver.window_handles:
            if now_window != window:
                driver.switch_to.window(window)

    @classmethod
    def pull_down(cls,driver,karg):
        """下拉框"""
        if karg[1].startswith('xpath'):
            find_style = karg[1][:5]
            find_data = karg[1][6:]
        else:
            find_style = karg[1][:2]
            find_data = karg[1][3:]
        seting = driver.find_element(find_style,find_data)
        Select(seting).select_by_value(karg[2])

    @classmethod
    def pop_window(cls,driver,karg):
        """弹窗处理"""
        pass

    @classmethod
    def file_upload(cls,driver,karg):
        """文件上传"""
        if karg[1].startswith('xpath'):
            find_data = karg[1][6:]
            find_path = karg[2]
            content = driver.find_element('xpath', find_data).send_keys(find_path)
        else:
            find_data = karg[1][3:]
            find_path = karg[2]
            content = driver.find_element('id', find_data).send_keys(find_path)

    @classmethod
    def default(cls,driver,karg):
        """切换句柄"""
        driver.switch_to.default_content()