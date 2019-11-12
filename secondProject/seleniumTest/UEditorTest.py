from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# current=driver.current_window_handle
# driver.find_element('id','kw').send_keys('富文本框')
driver.implicitly_wait(5)
driver.get('https://ueditor.baidu.com/website/onlinedemo.html')
# driver.find_element('xpath', '//input[@value="zh-cn"]').click()

driver.switch_to.frame(driver.find_element('id','ueditor_0'))
JS='var j=document.getElementsByTagName("p")[0];j.innerText="hello"'
driver.execute_script(JS)
# def UEditor_demo():
#     # driver.find_element('id','kw')
#     driver.switch_to.frame(driver.find_element('id','ueditor_0'))
#     JS='var j=document.getElementsByTagName("p")[0];j.innerText("hello");'
#     driver.execute_script(JS)
# if __name__ == '__main__':
#     UEditor_demo()