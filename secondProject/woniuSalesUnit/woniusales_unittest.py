import unittest
from selenium import webdriver
import BSTestRunner,time
class woniusaleUnit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.bossqiang.com/milor/')
        self.driver.implicitly_wait(3)
    def tearDown(self):
        self.driver.close()
    def get_data(self):
        testdata=[('dy','','登录失败，请重新登录.'),('','DY123','登录失败，请重新登录.'),('dd','dd','登录失败，请重新登录.')]
        return testdata
    def testWoniusalesLogin(self):
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

        #测试输入正确的条码信息能否查询到信息
    # def testWoniusalesOutware1(self):
    #     self.driver.find_element('id','barcode').send_keys('6955203644985')
    #     self.driver.find_element('xpath',"//button[contains(@onclick,'que')]").click()
    #     result=self.driver.find_element('xpath',"//tbody[@id='goodslist']/tr/td[3]").text
    #     self.assertEqual('泡泡袖衬衣',result)
        #测试输入错误的折扣信息能否弹出错误提示
    # def testWoniusalesOutware2(self):
    #     self.driver.find_element('id','barcode').send_keys('6955203644985')
    #     self.driver.find_element('xpath',"//button[contains(@onclick,'que')]").click()
    #     self.driver.find_element('css selector',"input[value='68']").clear()
    #     self.driver.find_element('css selector',"input[value='68']").send_keys('aaaa')

if __name__ == '__main__':

    unittest.main()
    # tc=unittest.TestLoader().loadTestsFromTestCase(woniusaleUnit)
    # # tc=unittest.TestSuite()
    # # tc.addTests([woniusaleUnit("testWoniusalesOutware1"),woniusaleUnit('testWoniusalesLogin')])
    # # tc.addTests([woniusaleUnit('testWoniusalesLogin')])
    # outfile=open('woniusale_testReport.html','w',encoding='utf8')
    # runner=BSTestRunner.BSTestRunner(stream=outfile,title='woniuSale登录测试',description='woniuSales测试报告')
    # runner.run(tc)