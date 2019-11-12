__author__ = "Epiphyllum"

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time, os, random, re, cv2
from PIL import ImageGrab, Image
from functools import wraps
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from POM.common.support import Support
from selenium.common.exceptions import UnexpectedTagNameException as UTNE


class Base:

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()

    # 点击
    def click(self, method, position):
        # 初始化支持模块
        support = Support(self.driver)
        # 检验find_element方式是否正确
        mode = support._checkmode(method, position)

        try:
            # 检验元素是否存在
            support._checkele(mode)
            # 获得driver元素实例
            driver =self.driver.find_element(mode[0], mode[1])

            # 如果通过name, id查找元素则进行骚操作
            support._js(mode)
            # 点击
            driver.click()

        # 如果元素不存在
        except TimeoutException:
            # 输出元素不存在错误日志 并截图
            support._error_timeout(mode, "CLICK")
        # 如果查找元素方式错误
        except TypeError:
            #   输出查找方式错误日志 并截图
            support._error_type(method, "CLICK")

    # 切换句柄点击 适用范围: 销售主页上面"官方网站"类型
    def handle_click(self, method, position):
        support = Support(self.driver)
        mode = support._checkmode(method, position)

        try:
            support._checkele(mode)
            # 获得当前句柄
            current = self.driver.current_window_handle

            driver = self.driver.find_element(mode[0], mode[1])
            support._js(mode)
            # 这里click指的是打开新的页面
            driver.click()

            # 获得所有句柄 与初始句柄进行比较 找出新开窗口句柄
            for handle in self.driver.window_handles:
                if handle != current:
                    self.driver.switch_to_window(handle)
            self.sleep(3)
            # 关闭新开窗口
            self.driver.close()
            #返回初始窗口
            self.driver.switch_to_window(current)

        except TimeoutException:
            support._error_timeout(mode, "HADNLE_CLICK")
        except TypeError:
            support._error_type(method, "HANDLE_CLICK")

    # 输入 会先执行clear操作
    def input(self, method, position, content):
        support = Support(self.driver)
        mode = support._checkmode(method, position)

        try:
            support._checkele(mode)
            driver = self.driver.find_element(mode[0], mode[1])
            support._js(mode)
            # 执行clear操作 清空输入框
            driver.clear()
            driver.send_keys(content)

        except TimeoutException:
            support._error_timeout(mode, "INPUT")
        except TypeError:
            support._error_type(method, "INPUT")

    # 悬浮
    def chains(self, method, position):
        support = Support(self.driver)
        mode = support._checkmode(method, position)

        try:
            support._checkele(mode)
            element = self.driver.find_element(mode[0], mode[1])
            support._js(mode)
            # 悬停于悬浮框上
            ActionChains(self.driver).move_to_element(element).perform()

        except TimeoutException:
            support._error_timeout(mode, "SUSPENSION")
        except TypeError:
            support._error_type(method, "SUSPENSION")

    # 下拉框
    def select(self, method, position, index):
        support = Support(self.driver)
        mode = support._checkmode(method, position)

        try:
            support._checkele(mode)
            support._js(mode)
            # 实例化下拉框对象
            select = Select(self.driver.find_element(mode[0], mode[1]))
            # 通过下标选择下拉框项
            select.select_by_index(int(index))

        except TimeoutException:
            support._error_timeout(mode, "SELECT")
        except TypeError:
            support._error_type(method, "SELECT")
        # 如果使用index外选择方式
        except UTNE:
            # 输出选择方式有误错误报告 并截图
            support._error_sele("SELECT")

    # 识别验证码
    def captcha(self, method, position):
        support = Support(self.driver)
        mode = support._checkmode(method, position)

        try:
            support._checkele(mode)
            support._js(mode)
            driver = self.driver.find_element(mode[0], mode[1])

            # 接收验证码的字符串
            verify_code = support._captcha(driver)

            # 返回验证码 请自行将这里输出值放入input操作中第三个参数
            # 比如 self.input("id", "verify-code", self.captcha(method, position))
            return verify_code

        except TimeoutException:
            support._error_timeout(mode, "VERIFY")
        except TypeError:
            support._error_type(method, "VERIFY")

    # 断言操作
    def verdict(self, method, position, text):
        support = Support(self.driver)
        mode = support._checkmode(method, position)

        try:
            support._checkele(mode)
            driver = self.driver.find_element(mode[0], mode[1])
            support._js(mode)

            if driver.text == text:
                msg = f"断言成功! {driver.text} 等于 {text}"
                print(msg)
                with open("../log/assert.log", "a+", encoding="GBK") as file:
                    file.write(f"\n{msg}")

            else:
                msg = f"断言失败! {driver.text} 不等于 {text}"
                print(msg)
                with open("../log/assert.log", "a+", encoding="GBK") as file:
                    file.write(f"\n{msg}")

        except TimeoutException:
            support._error_timeout(mode, "ASSERT")
        except TypeError:
            support._error_type(method, "ASSERT")

    # 暂停操作
    def sleep(self, sleep=1):
        time.sleep(sleep)

    # 退出浏览器
    def quit(self):
        self.driver.quit()



