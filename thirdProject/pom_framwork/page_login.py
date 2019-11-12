from selenium import webdriver
class LoginPom:
    def __init__(self,dr):
        # self.driver=webdriver.Chrome()
        # self.driver.get('http://192.168.3.180:8080/woniusales/')
        self.driver=dr
    #定位用户名输入框
    def get_username(self):
        self.driver.find_element_by_id('username').clear()
        return self.driver.find_element_by_id('username')
    #定位密码输入框
    def get_password(self):
        self.driver.find_element_by_id('password').clear()
        return self.driver.find_element_by_id('password')
    #定位验证码输入框
    def get_verifycode(self):
        self.driver.find_element_by_id('verifycode').clear()
        return self.driver.find_element_by_id('verifycode')
    #定位登录按钮
    def get_login_button(self):
        return self.driver.find_element_by_xpath('//div/button[contains(@onclick,"doLogin")]')

    #登录action
    def do_login(self,username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_verifycode().send_keys('0000')
        self.get_login_button().click()
