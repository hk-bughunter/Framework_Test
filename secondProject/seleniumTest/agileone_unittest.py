import unittest
from selenium import webdriver
import BSTestRunner
class agileone(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://192.168.3.182:8081/agileone/Agileone_1.2/")
        self.driver.implicitly_wait(3)
    def tearDown(self):
        self.driver.quit()
    def testAgileoneLogin(self):
        self.driver.find_element('id','username').send_keys('admin')
        self.driver.find_element('id','password').send_keys('admin')
        self.driver.find_element('id','login').click()
        result=self.driver.find_element('id','welcome').text
        self.assertEqual('下午好: Administrator admin',result)

if __name__ == '__main__':
    # unittest.main()
    tc=unittest.TestLoader().loadTestsFromTestCase(agileone)
    outfile=open('test_report.html','w',encoding='utf8')
    runner=BSTestRunner.BSTestRunner(stream=outfile,title='Agileone登录测试',description='Agileone测试报告')
    runner.run(tc)
    # tc = unittest.TestLoader().loadTestsFromTestCase(agileone)
    # outfile = open('test_report.html', 'w', encoding='utf8')
    # runner = BSTestRunner.BSTestRunner(stream=outfile, title='Agileone登录', description='Agileone测试报告0.1')
    # runner.run(tc)

