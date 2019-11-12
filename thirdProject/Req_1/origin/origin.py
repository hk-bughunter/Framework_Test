import requests, time, os, re, random
from fake_useragent import UserAgent
from urllib.parse import unquote


class Base():

    def __init__(self):
        self.session = requests.session()

    def check(self, method, url, cookies=None, data=None):

        # 检查method格式
        if method.lower() != "get" and method.lower() != "post":
            message = f"\nmethod 格式错误; 当前mehod格式为 {method} :请传入get或者post"
            print(message)
            with open("../log/error.log", "a+", encoding="GBK") as file:
                file.write(message)
            return None

        # 检查url
        reg = re.compile("https?://.*")
        if not reg.findall(url.lower()):
            message = f"\nurl 格式错误; 当前url格式为 {url} :请传入正确url"
            print(message)
            with open("../log/error.log", "a+", encoding="GBK") as file:
                file.write(message)
            return None

        # 检查cookies
        if cookies != None and cookies.lower() != "none" and len(cookies.replace(" ", "")) < 10 and cookies != "" and cookies != " ":
            message = f"\ncookie不正确; 当前cookie为 {cookies}, 检查是否输入空值"
            print(message)
            with open("../log/error.log", "a+", encoding="GBK") as file:
                file.write(message)
            return None
        else:
            if cookies != None and len(cookies.replace(" ", "")) < 10:
                cookies = None

        # 检查data
        if method.lower() == "get" and data != None and data.lower() != "none" and len(data.replace(" ", "")) < 10 and data != "" and data != " ":
            message = f"\ndata不正确; 当前data为 {data}, get请求data应为None"
            print(message)
            with open("../log/error.log", "a+", encoding="GBK") as file:
                file.write(message)
            return None
        else:
            if data != None and len(data.replace(" ", "")) < 10:
                data = None

        # 构造header
        if cookies != None:
            headers = {
                "User-Agent": UserAgent().random,
                "Cookie" : cookies
            }
        else:
            headers = {
                "User-Agent": UserAgent().random
            }

        # 构造data 骚操作
        if data != None:
            source_list = data.split("&")

            data = {}

            for source in source_list:
                data_list = unquote(source).split("=")
                data[data_list[0]] = data_list[1]

        return (method, url, headers, data)

    def assertion(self, result, content):
        assert result in content

    def connect(self, method, url, cookies, data, result):

        args = self.check(method, url, cookies, data)
        if not args:
            return None

        response = self.session.request(method=args[0], url=args[1], headers=args[2], data=args[3])

        self.assertion(result, response.text)










