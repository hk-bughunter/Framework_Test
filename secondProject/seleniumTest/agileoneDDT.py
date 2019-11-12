import unittest
from selenium import webdriver
import time,ddt
def get_data():
    test_data=(['admin','','出错啦: 密码输入错误 ...'],
                        ['','admin','出错啦: 用户名不能为空 ...'],
                        ['','DY123','出错啦: 用户名不能为空 ...'])
    return test_data
def get_rightdata():
    test_data=[('admin','admin','晚上好: Administrator admin')]
    return test_data
@ddt.ddt
class agileoneTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://192.168.3.182:8081/agileone/Agileone_1.2/')
        self.driver.implicitly_wait(3)
    def tearDown(self):
        self.driver.quit()
    # @ddt.data(['admin','','出错啦: 密码输入错误 ...'],
    #                     ['','admin','出错啦: 用户名不能为空 ...'],
    #                     ['','DY123','出错啦: 用户名不能为空 ...'])
    @ddt.data(*get_data())
    @ddt.unpack
    def testAgileonLogin(self,name,pwd,expected):
        self.driver.find_element('id', 'username').clear()
        self.driver.find_element('id', 'username').send_keys(name)
        self.driver.find_element('id', 'password').clear()
        self.driver.find_element('id', 'password').send_keys(pwd)
        self.driver.find_element('id', 'login').click()
        time.sleep(1)
        result=self.driver.find_element('id','msg').text
        self.assertEqual(expected,result)
    @ddt.data(*get_rightdata())
    @ddt.unpack
    def testAgileoneRight(self,name,pwd,expeted):
        self.driver.find_element('id', 'username').clear()
        self.driver.find_element('id', 'username').send_keys(name)
        self.driver.find_element('id', 'password').clear()
        self.driver.find_element('id', 'password').send_keys(pwd)
        self.driver.find_element('id', 'login').click()
        time.sleep(1)
        result = self.driver.find_element('id', 'welcome').text
        self.assertEqual(expeted, result)
if __name__ == '__main__':
    unittest.main()
    # tc=unittest.TestSuite()
    # tc.addTests([agileoneTest('testAgileonLogin'),agileoneTest('testAgileoneErr')])
    # unittest.TextTestRunner().run(tc)