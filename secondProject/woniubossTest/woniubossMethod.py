import requests
from woniubossTest.readExcel import *

class Woniuboss():
    """用构造函数获取session"""
    def __init__(self,url,data):
        self.session = requests.session()
        self.session.post(url,data)
    """发送get请求"""
    def req_get(self, url):
        content=self.session.get(url=url)
        return content
    """"发送post请求"""
    def req_post(slef, url, data):
        content=slef.session.post(url=url,data=data)
        return content
    """根据状态码断言"""
    def asertStaus(self,content,status):
        if content.status_code==status:
            print("测试成功")
        else:
            print("测试失败预期状态码：{0},实际状态码：{1}".format(int(status),content.status_code))
    """根据响应正文是否相等断言"""
    def asertText_equal(self,content,text):
        if content.text == text:
            print("测试成功")
        else:
            print("响应正文不相等，预期响应：{0},实际响应{1}".format(text, content.text))
    """根据是否包含响应正文断言"""
    def asertText_in(self,content,text):
        if content.text in text:
            print("测试成功")
        else:
            print("响应正文不包含，预期响应：{0},实际响应不包含该正文".format(text,content.text))
    """根据包含响应头部断言"""
    def asertHeaders_in(self,content,header):
        if header in content.headers:
            print("测试成功")
        else:
            print("测试失败响应头部不包含，预期响应：{0},实际响应：{1}".format(header, content.headers))

if __name__ == '__main__':
    reqlist = readExcel()
    Woniuboss=Woniuboss()

