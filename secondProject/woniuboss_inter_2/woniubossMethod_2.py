import requests
from woniubossTest.readExcel import *
from functools import wraps

class Woniuboss():
    """用构造函数获取session"""
    def __init__(self,url,data):
        self.session = requests.session()
        self.session.post(url,data)

    def writelog(func):
        @wraps(func)
        def wrapFunction(*args,**kwargs):
            result=func(*args,**kwargs)
            with open("log.txt","a",encoding="utf-8") as file:
                msg=result+": "+args[3]
                file.write(msg+'\n')
        return wrapFunction

    """发送get请求"""
    def req_get(self, url):
        content=self.session.get(url=url)
        return content
    """"发送post请求"""
    def req_post(slef, url, data):
        content=slef.session.post(url=url,data=data)
        return content
    """根据状态码断言"""

    @writelog
    def asertcode(self,content,status):
        if content.status_code==status:
            print("测试成功")
            test_result="测试成功"
        else:
            print("测试失败，预期状态码：{0},实际状态码：{1}".format(int(status),content.status_code))
            test_result = "测试失败"
        return test_result
    """根据响应正文是否相等断言"""
    @writelog
    def asertText(self,*args):
        content = args[0]
        text = args[1]
        if content.text == text:
            print("测试成功")
            test_result = "测试成功"
        else:
            print("测试失败，响应正文不相等，预期响应：{0},实际响应{1}".format(text, content.text))
            test_result = "测试失败"
        return test_result
    """根据是否包含响应正文断言"""
    @writelog
    def asertjson(self,*args):
        content=args[0]
        text=args[1]
        if content.text in text:
            print("测试成功")
            test_result = "测试成功"
        else:
            print("测试失败，响应正文不包含，预期响应：{0},实际响应不包含该正文".format(text,content.text))
            test_result = "测试失败"
        return test_result
    """根据包含响应头部断言"""
    @writelog
    def asertHeaders(self,*args):
        content = args[0]
        header = args[1]
        if header in content.headers:
            print("测试成功")
            test_result = "测试成功"
        else:
            print("测试失败，响应头部不包含，预期响应：{0},实际响应：{1}".format(header, content.headers))
            test_result = "测试失败"
        return test_result

if __name__ == '__main__':
    reqlist = readExcel()
    Woniuboss=Woniuboss()

