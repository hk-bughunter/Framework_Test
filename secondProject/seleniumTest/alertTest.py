from selenium import webdriver
import time
driver=webdriver.Chrome()
# driver.get('https://www.w3school.com.cn/tiy/t.asp?f=hdom_alert')
# driver.get('https://www.w3school.com.cn/jsref/met_win_alert.asp')

def alert_demo():
    # driver.find_element('partial link text','显示一个对话框').click()
    # time.sleep(3)
    driver.switch_to.frame(driver.find_element('id','iframeResult'))
    driver.find_element('xpath','//body/input').click()
    alert=driver.switch_to.alert
    alert.accept()

def confirm_demo():
    driver.get('https://www.w3school.com.cn/tiy/t.asp?f=hdom_confirm')
    driver.switch_to.frame(driver.find_element('id','iframeResult'))
    driver.find_element('xpath', '//body/input[@value="Show a confirm box"]').click()
    alert=driver.switch_to.alert
    alert.dismiss()
    alert.accept()
    # driver.switch_to.default_content()

def prompt_demo():
    driver.get('https://www.w3school.com.cn/tiy/t.asp?f=hdom_prompt')

    driver.switch_to.frame(driver.find_element('id','iframeResult'))
    driver.find_element('xpath', '//body/input[@value="Show a confirm box"]').click()
if __name__ == '__main__':
    # alert_demo()
    confirm_demo()
