from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
open_driver=webdriver.Chrome()
open_driver.get('http://localhost:8081/agileone/Agileone_1.2/')
open_driver.find_element('css selector',"input[id='username']").send_keys('admin')
open_driver.find_element('css selector',"input[id='password']").send_keys('admin')
open_driver.find_element('xpath',"//input[@id='login']").click()
# before=open_driver.current_window_handle
# time.sleep(3)
open_driver.implicitly_wait(3)
open_driver.find_element('partial link text',"公告管理").click()
arr_element=open_driver.find_elements('css selector','input[type="text"]')
print(arr_element)
for i in arr_element:
        i.send_keys('test')
# time.sleep(5)
# open_driver.find_element_by_xpath("(//a[@href='/note'][@target='_blank'])[0]").click()
# open_driver.close()
time.sleep(5)
open_driver.close()



