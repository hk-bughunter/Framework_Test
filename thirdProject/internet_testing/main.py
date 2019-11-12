from pyquery import PyQuery as py
import requests, csv, re, time, os
from internet_testing.captcha import query
from fake_useragent import UserAgent


class Main:
    # 针对后台管理页面 作为管理员登陆获得cookies
    def __init__(self):

        self.session = requests.session()
        img = self.session.get("http://192.168.3.123:8081/tinyshop3/index.php?con=index&act=captcha&h=40&w=120&bc=1a78c2&c=ffffff")
        with open("./captcha.jpg", "wb") as file:
            file.write(img.content)

        captcha_path = os.path.abspath("./captcha.jpg")
        captcha_content = query(captcha_path)

        url = "http://192.168.3.123:8081/tinyshop3/index.php?con=admin&act=check"

        self.headers= {
            "User-Agent": str(UserAgent().random)
        }
        data = {
            "name": "admin",
            "password": "123456",
            "verifyCode": captcha_content
        }

        self.session.request(method="post", url=url, verify=False, data=data)

    def run(self, url, method, assertion, data=None):
        response = self.session.request(method=method, data=data, url=url, verify=False)
        assert assertion in response.text
        print("Ok")


if __name__ == '__main__':
    m = Main()
    m.run("http://192.168.3.123:8081/tinyshop3/index.php?con=admin&act=theme_list", "get", "主题设置-TinyShop商城")





