from POM_GUI.case.LoginCase import Login
from POM_GUI.case.ShopCase import Shop
import pytest
from POM_GUI.data.gui_data import *


# 基于单个模块构建的单个事件组装为自己需要的测试套件 不会的请参阅群里的pytest笔记
class Test_Login():
    def setup_class(self):
        # self.driver = Login()
        self.driver=Shop()
    def teardown_class(self):
        self.driver.close()


    # @pytest.mark.parametrize(argnames=error_username[0], argvalues=error_username[1])
    # @pytest.mark.parametrize(argnames=error_passwd[0], argvalues=error_passwd[1])
    # def test_errorlogin(self, username, passwd):
    #     self.driver.username(username)
    #     self.driver.password(passwd)
    #     self.driver.verify()
    #     self.driver.login()
    #     self.driver.assertion("xpath", '//*[@id="login"]/div/div', "用户名或者密码错误")


    # @pytest.mark.parametrize(argnames=correct_login[0], argvalues=correct_login[1])
    # def test_correctlogin(self, username, passwd):
    #     self.driver.username(username)
    #     self.driver.password(passwd)
    #     self.driver.verify()
    #     self.driver.login()
    #     self.driver.assertion("xpath", '//*[@id="content"]/div/div[1]/table/tbody/tr[1]/td[2]/p[2]/a', "授权查询")

    def test_shoping(self):
        self.driver.username("123456@163.com")
        self.driver.password("123456")
        self.driver.login()
        self.driver.clothing()
        self.driver.commodity()
        self.driver.color()
        self.driver.size()

if __name__ == '__main__':
    pytest.main(['test_Login.py', '-q', '--html=../result/report.html', '--self-contained-html'])

