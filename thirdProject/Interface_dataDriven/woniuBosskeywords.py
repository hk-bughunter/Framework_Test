from functools import wraps
import requests

class WoniuBossTest:
    """接口测试框架"""

    def writeLog(func):
        """日志装饰器"""
        @wraps(func)
        def wrapFunction(*args,**kwargs):
            respons = func(*args,**kwargs)
            msg = f"{respons}:{args[3]}"
            with open('WoniuBossTestLog.txt','a',encoding='utf-8') as f:
                f.write(msg + "\n")
        return wrapFunction

    @classmethod
    def get(cls,*args):
        """get请求"""
        re = requests.get(url=args[0],cookies=args[1])
        return re

    @classmethod
    def post(cls,*args):
        """post请求"""
        re = requests.post(url=args[0],data=args[1],cookies=args[2])
        return re

    @classmethod
    @writeLog
    def checktext(cls,*args):
        """判断响应正文是否相等"""
        if args[0] == args[1]:
            print(f"测试成功,需求的文本为:{args[0]}，实际的文本为:{args[1]}")
            restr = "测试成功"
            return restr
        else:
            print(f"测试失败,需求的文本为:{args[0]}，实际的文本为:{args[1]}")
            restr = "测试失败"
            return restr

    @classmethod
    @writeLog
    def checkjson(cls,*args):
        """验证查询结果是否在相应正文中"""
        if args[0] in args[1]:
            print(f"测试成功,'{args[0]}'字段，在响应正文中")
            restr = "测试成功"
            return restr
        else:
            print(f"测试失败,'{args[0]}'字段，不在响应正文中")
            restr = "测试失败"
            return restr

    @classmethod
    @writeLog
    def checkcode(cls,*args):
        """验证状态码是否正确"""
        if args[0] == args[1]:
            print(f"测试成功,需求的状态码为:{args[0]}，实际的状态码为:{args[1]}")
            restr = "测试成功"
            return restr
        else:
            print(f"测试失败,需求的状态码为:'{args[0]}'，实际的状态码为:'{args[1]}'")
            restr = "测试失败"
            return restr




