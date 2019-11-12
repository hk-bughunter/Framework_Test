from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
class Keydriver():
    @classmethod
    def goto(cls,driver,data):
        driver.get(data[1])

    @classmethod
    def input(cls,driver,data):
        if 'xpath' in data[1]:
            # locater=data.split(',')[1][6:]
            # print(locater)
            driver.find_element('xpath',data[1][6:]).send_keys(data[2])
        else:
            locater=data[1][3:]
            print(locater)
            driver.find_element('id',locater).send_keys(data[2])

    @classmethod
    def singleclick(cls,driver,data):
        if data[1].startswith('xpath'):
            # locater=data.split(',')[1][6:]
            # print(locater)
            driver.find_element('xpath', data[1][6:]).click()
        elif data[1].startswith('id'):
            locater = data[1][3:]
            # print(locater)
            driver.find_element('id', locater).click()
        else:
            print("你的输入不规范")

    @classmethod
    def checklen(cls,driver,data):
        if 'xpath' in data[1]:
            locater=data[1][6:]
            # print(locater)
            ele=driver.find_elements('xpath', locater)
        else:
            locater = data[1][3:]
            # print(locater)
            ele=driver.find_elements('id', locater).click()
        if len(ele)==data[2]:
            print('长度正确')
        else:
            print("长度不正确")

    @classmethod
    def delay(cls,driver,data):
        t=int(data[1])
        time.sleep(t)

    @classmethod
    def checktext(cls,driver,data):
        if 'xpath' in data[1]:
            locater=data[1][6:]
            ele=driver.find_element('xpath', locater).text
        else:
            locater = data[1][3:]
            ele=driver.find_element('id', locater).text
        if ele==data[2]:
            print("文本正确")
        else:
            print("文本错误")

    @classmethod
    def over(cls,driver,data):
        driver.quit()

    @classmethod
    def suspenchoice(cls,driver,data):
        if data[1].startswith('xpath'):
            ele_move=driver.find_element('xpath', data[1][6:])
            ActionChains(driver).move_to_element(ele_move).perform()
            if data[2].startswith('xpath'):
                ActionChains(driver).move_to_element(ele_move).perform()
                driver.find_element('xpath',data[2][6:]).click()
            else:
                ActionChains(driver).move_to_element(ele_move).perform()
                driver.find_element('id',data[2][3:]).click()
        else:
            locater = data[1][3:]
            ele_move=driver.find_element('id', locater)
            if data[2].startswith('xpath'):
                ActionChains(driver).move_to_element(ele_move).perform()
                driver.find_element('xpath',data[2][6:]).click()
            else:
                ActionChains(driver).move_to_element(ele_move).perform()
                driver.find_element('id',data[2][3:]).click()
