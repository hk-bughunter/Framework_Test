from selenium import webdriver
import time
# lista=['123','123123','55']
# b=len(lista)
# print(b)



driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element('xpath',"//input[@id='kw']").send_keys('python')
driver.find_element('id','su').click()
time.sleep(3)
b=driver.find_element('name','tj_login').text
print(b)
a=driver.find_elements('xpath',"//div[@id='content_left']//h3")
time.sleep(2)
print(a)
print(len(a))
driver.find_element_by_xpath('//div[@id="content_left"]//h3')
print(len(a))
driver.close()