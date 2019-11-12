from woniubossTest.woniubossMethod import Woniuboss
from woniubossTest.readExcel import readExcel
import json

"""执行测试用例"""
def runTestcase():
    url = "http://192.168.3.180:8080/woniuboss/login/userLogin"
    dataone = {'userName': 'WNCD000', 'userPass': 'woniu123', 'checkcode': '0000', 'remember': 'Y'}
    woniuboss=Woniuboss(url,dataone)
    datalist=readExcel()
    #遍历读取到的excel数据
    for i in datalist:
        data=eval(i[2].strip())
        # print(i[2])
        # data=json.loads(i[2].strip)
        # print(data)
        #判断是否为post请求
        if i[0]=="post":
            content=woniuboss.req_post(i[1].strip(), data)
            asertMethod=i[4].strip()
            #判断是否以状态码断言
            if asertMethod=="code":
                woniuboss.asertStaus(content,i[3])
            #判断响应正文是否相等
            elif asertMethod=="equal":
                woniuboss.asertText_equal(content,i[5])
            #判断响应正文是否包含
            elif asertMethod=="substring":
                woniuboss.asertText_in(content,i[5])
            #判断响应头部
            elif asertMethod=="header":
                woniuboss.asertText_in(content,i[5])
            else:
                print("断言方法有问题")
                # break
        #判断是否为get请求
        elif i[0].strip()=="get":
            print("----------")
            content=woniuboss.req_get(i[1].strip())
            asertMethod = i[4].strip()
            print("00000000000000000")
            # 判断是否以状态码断言
            if asertMethod == "code":
                woniuboss.asertStaus(content, i[3])
            # 判断响应正文是否相等
            elif asertMethod == "equal":
                woniuboss.asertText_equal(content, i[5])
            # 判断响应正文是否包含
            elif asertMethod == "substring":
                woniuboss.asertText_in(content, i[5])
            # 判断响应头部
            elif asertMethod == "header":
                woniuboss.asertText_in(content, i[5])
            else:
                print("断言方法有问题")
        else:
            print("请求方法输入错误")
if __name__ == '__main__':
    runTestcase()