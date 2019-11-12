# -*- coding: cp936 -*-
import os
import sys
from ctypes import *

def query(path):
    """
    调用打码平台返回验证码
    """
    folder = os.path.abspath('../') + "\\common\\yundamaAPI.dll"
    YDMApi = windll.LoadLibrary(folder)

    # 不用管
    appId = 1
    appKey = b'22cc5376925e9387a23cf797cb9ba745'
    # 用户密码
    username = b'epiphany'
    password = b'qwer9979'
    # 在此查询所有类型 http://www.yundama.com/price.html
    codetype = 5000
    # 分配30个字节存放识别结果
    result = c_char_p(b"                              ")
    # 识别超时时间 单位：秒
    timeout = 60
    # 验证码文件路径
    filename = bytes(path ,encoding="utf-8")
    # 调用识别
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
    # 返回字符串
    return str(result.value, encoding="utf-8")



