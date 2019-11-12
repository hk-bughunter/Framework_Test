from POM_GUI.common.origin import Base


# 基于提供的框架基本操作构建单个模块的单个事件
class Login(Base):
    # 指定测试模块的URL
    URL = "http://192.168.3.111:8081/tinyshop3.0/index.php?con=admin&act=login&tdsourcetag=s_pctim_aiomsg"

    def __init__(self):
        super().__init__(url=self.URL)

    # 传入用户名 用作测试
    def username(self, content):
        self.input("name", "name", content)

    # 传入密码 用作测试
    def password(self, content):
        self.input("name", "password", content)

    # 验证码
    def verify(self):
        self.input("name", "verifyCode", self.captcha("id", "captcha_img"))

    # 登陆按钮
    def login(self):
        self.click("xpath", '//*[@id="login"]/div/form/ul/li[4]/input[1]')
        self.sleep()

    # 重置按钮
    def reset(self):
        self.click("xpath", '//*[@id="login"]/div/form/ul/li[4]/input[2]')
        self.sleep()

    # 断言
    def assertion(self, method, position, text):
        self.verdict(method, position, text)
        self.sleep(3)

    def close(self):
        self.quit()

