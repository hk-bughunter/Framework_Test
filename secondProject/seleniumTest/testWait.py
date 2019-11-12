from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
print(driver)
print(type(driver))
driver.get('http://localhost:8081/agileone/Agileone_1.2/')
def fill_text():
    driver.find_element('css selector',"#username").send_keys('admin')
    driver.find_element('css selector',"#password").send_keys('admin')
    driver.find_element('css selector',"#login").click()
    #显示等待，until后必须跟函数，所以这里用到匿名函数
    # ele=WebDriverWait(driver,5,0.5).until(lambda driver:driver.find_element('partial link text','公告管理'))
    # ele.click()
    lcoater=(By.PARTIAL_LINK_TEXT,"公告管理")
    WebDriverWait(driver,5,0.5).until(EC.presence_of_all_elements_located(lcoater))
    driver.find_element('partial link text',"公告管理").click()
    Select(driver.find_element('id','newitem')).select_by_value('knowledge')
if __name__ == '__main__':
    fill_text()