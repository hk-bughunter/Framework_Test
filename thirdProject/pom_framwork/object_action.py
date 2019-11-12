from pom_framwork.page_login import LoginPom
from pom_framwork.page_sell import SellPom
from selenium import webdriver
import time
class action:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://localhost:8080/woniusales/')
        self.driver.implicitly_wait(10)
    def test_login(self):
        login=LoginPom(self.driver)
        login.do_login('admin','Milor123')
        time.sleep(1)
        try :
            login.driver.find_element_by_link_text('注销')
            print('登录成功')
        except:
            print('登录失败')

    def test_sell(self):
        sell=SellPom(self.driver)
        sell.do_sell('6955203636348')

    def start_test(self):
        self.test_login()
        self.test_sell()

    def __del__(self):
        self.driver.close()

if __name__ == '__main__':
    ac=action()
    # ac.test_login()
    # ac.test_sell()

