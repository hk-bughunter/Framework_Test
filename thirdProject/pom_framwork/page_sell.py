import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

#driver必须要使用单例模式才能正常使用
class SellPom:
    def __init__(self,dr):
        # self.driver=webdriver.Chrome()
        # self.driver.get('http://192.168.3.180:8080/woniusales/')
        self.driver=dr
    #定位商品条码输入框
    def get_barcode(self):
        self.driver.find_element_by_id("barcode").clear()
        return self.driver.find_element_by_id("barcode")
    #定位商品条码确认按钮
    def get_barcode_button(self):
        return self.driver.find_element_by_xpath('//button[@onclick="queryByBarCode()"]')
    #定位确认收款按钮
    def get_gathering_button(self):
        self.driver.find_element_by_id('submit')

    # def get_

    def do_sell(self,barcode):
        from pom_framwork.page_login import LoginPom
        # login=LoginPom(self.driver).do_login('dy','DY123')
        # time.sleep(2)
        self.get_barcode().send_keys(barcode)
        self.get_barcode_button().click()
        time.sleep(5)