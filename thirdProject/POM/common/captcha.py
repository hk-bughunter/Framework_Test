# -*- coding: cp936 -*-
import os
import sys
from ctypes import *

def query(path):
    """
    ���ô���ƽ̨������֤��
    """
    folder = os.path.abspath('../') + "\\common\\yundamaAPI.dll"
    YDMApi = windll.LoadLibrary(folder)

    # ���ù�
    appId = 1
    appKey = b'22cc5376925e9387a23cf797cb9ba745'
    # �û�����
    username = b'epiphany'
    password = b'qwer9979'
    # �ڴ˲�ѯ�������� http://www.yundama.com/price.html
    codetype = 5000
    # ����30���ֽڴ��ʶ����
    result = c_char_p(b"                              ")
    # ʶ��ʱʱ�� ��λ����
    timeout = 60
    # ��֤���ļ�·��
    filename = bytes(path ,encoding="utf-8")
    # ����ʶ��
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
    # �����ַ���
    return str(result.value, encoding="utf-8")



