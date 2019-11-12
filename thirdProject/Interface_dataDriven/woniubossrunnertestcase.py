from Interface_dataDriven.woniubossdata import Parse
from Interface_dataDriven.woniuBosskeywords import WoniuBossTest
from Interface_dataDriven.exportreport import Export_Excelreport

import requests

data = {"userName":"WNCD000","userPass":"woniu123","checkcode":"0000","remember":"Y"}
url = "http://192.168.3.233:8080/woniuboss/login/userLogin/"
con = requests.post(url=url,data=data)
cookie = con.cookies     #获取一个cookie

with open('WoniuBossTestLog.txt','w',encoding='utf-8') as ff:  #处理日志文件
    ff.write("")            #清空日志文件

test_case = Parse.get_data()          #获取测试用例
for i in test_case:
    """根据请求调用测试方法和断言方法"""
    try:                #异常处理
        if i[4] == "get":             #根据请求方式调用接口
            con = getattr(WoniuBossTest,i[4])(i[5],cookie)
        else:
            if i[6] != "":       #处理data数据为空时
                con = getattr(WoniuBossTest,i[4])(i[5],eval(i[6]),cookie)
            else:
                con = getattr(WoniuBossTest,i[4])(i[5],i[6],cookie)

        respons = con.text       #获取相应正文
        code = con.status_code      #获取状态码
        if i[8] == "code":          #通过断言方式，分别调用对应的断言方法
            title = getattr(WoniuBossTest, "check" + i[8])(i[7],code,i[0])
        else:
            title = getattr(WoniuBossTest, "check" + i[8])(i[9],respons,i[0])
    except:
        msg ="测试失败：" +">>>异常>>>"+ i[0] +"\n"
        print(i[0] + ":该条用例数据有问题，执行失败！")
        with open('WoniuBossTestLog.txt','a', encoding='utf-8') as err:  #写入异常用例
            err.write(msg)
        continue
getattr(Export_Excelreport,"makeExcel")()  #生成EXCEL报告