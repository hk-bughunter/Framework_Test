from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
# driver.switch_to.frame()
driver.get('https://www.baidu.com')
def suspension_demo():
    moreProduct=driver.find_element('link text','更多产品')
    ActionChains(driver).move_to_element(moreProduct).perform()
    driver.find_element('xpath',"//a[@name='tj_mp3']").click()
# def image_check():
#     driver.find_element('id','kw').send_keys('蜗牛')
#     time.sleep(2)
#     # ActionChains(driver).move_to_element(keywords).perform()
#     driver.find_element('xpath',"//form[@id='form']/div/ul/li[3]").click()
if __name__ == '__main__':
    suspension_demo()
#     image_check()