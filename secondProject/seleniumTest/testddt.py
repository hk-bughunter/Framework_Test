import unittest
from selenium import webdriver
import BSTestRunner,time,ddt
@ddt.ddt
class woniusaleUnit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://192.168.3.182:8081/agileone/Agileone_1.2/')
        self.driver.implicitly_wait(3)
    def tearDown(self):
        self.driver.close()
    # def get_data(self):
    #     testdata=[('dy','','登录失败，请重新登录.'),
    #     ('','','登录失败，请重新登录.'),('','DY123','登录失败，请重新登录.'),('dd','dd','登录失败，请重新登录.')]
    #     return testdata
    @ddt.data(testdata=[('dy','','登录失败，请重新登录.'),
                        ('','','登录失败，请重新登录.'),
                        ('','DY123','登录失败，请重新登录.'),
                        ('dd','dd','登录失败，请重新登录.')])
    @ddt.unpack
    def testWoniusalesLogin(self,username,pwd,result):
        testdata=self.get_data()
        for data in testdata:
            self.driver.find_element('id', 'username').clear()
            self.driver.find_element('id','username').send_keys(data[0])
            self.driver.find_element('id', 'password').clear()
            self.driver.find_element('id', 'password').send_keys(data[1])
            self.driver.find_element('id', 'verifycode').clear()
            a=input("输入验证码")
            self.driver.find_element('id','verifycode').send_keys(a)
            self.driver.find_element('xpath', "//button[contains(@onclick,'Login')]").click()
            time.sleep(2)
            # self.driver.find_element('id','verifycode')
            result=self.driver.find_element('xpath',"/html/body/div[6]/div/div/div[2]/div").text
            print(result)
            self.driver.find_element('xpath','/html/body/div[6]/div/div/div[3]/button').click()
            time.sleep(2)
            self.assertEqual(data[2], result)
            # alert.accept()


        # for data in testdata:
        #     self.driver.find_element('id', 'username').clear()
        #     self.driver.find_element('id','username').send_keys(data[0])
        #     self.driver.find_element('id', 'password').clear()
        #     self.driver.find_element('id', 'password').send_keys(data[1])
        #     time.sleep(6)
        #     self.driver.find_element('xpath', "//button[contains(@onclick,'Login')]").click()
        #     result=self.driver.find_element('css selector',"div[class='bootbox-body']").text
        #     self.driver.find_element('xpath','/html/body/div[6]/div/div/div[3]/button').click()
        #     # result=self.driver.switch_to.alert.text
        #     # alert=self.driver.switch_to.alert
        #     self.assertEqual(data[2], result)
        #     # alert.accept()
if __name__ == '__main__':
    unittest.main()