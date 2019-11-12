import unittest
from selenium import webdriver
class agileone(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com/s?ie=UTF-8&wd=163%E9%82%AE%E7%AE%B1")
        self.driver.implicitly_wait(3)
    def tearDown(self):
        self.driver.quit()
    def testAgileoneLogin(self):
        self.driver.find_element('id','op_email3_username').send_keys('S13322088309')
        self.driver.find_element('id','//input[@type="password"]').send_keys('qy19941004')
        self.driver.find_element('xpat',"//a[@class='c-btn c-btn-large c-btn-primary c-gap-right op_email3_submit OP_LOG_BTN']").click()
        # result=self.driver.find_element('id','welcome').text
        # self.assertEqual('下午好: Administrator admin',result)
if __name__ == '__main__':
    unittest.main()