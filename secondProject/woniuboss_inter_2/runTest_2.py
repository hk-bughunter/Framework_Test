from woniuboss_inter_2.readExcel_2 import readExcel
from woniuboss_inter_2.woniubossMethod_2 import Woniuboss

def runtest():
    url = "http://192.168.3.180:8080/woniuboss/login/userLogin"
    dataone = {'userName': 'WNCD000', 'userPass': 'woniu123', 'checkcode': '0000', 'remember': 'Y'}
    woniuboss=Woniuboss(url,dataone)
    datalist=readExcel()

    with open('log.txt',"w",encoding="utf-8") as f:
        f.write("")

    for i in datalist:
        try:
            requst_type=i[4].strip()
            title=i[0]
            url=i[5]
            data=i[6]
            code=i[7]
            text=i[9]
            asertMethod = i[8].strip()
            if requst_type=="post":
                content=woniuboss.req_post(url,data)
                # print(data)
                # if i[6]=="":
                #     content = woniuboss.req_post(url,i[6])
                # else:
                #     content=woniuboss.req_post(url,eval(i[6]))
                # content=getattr(woniuboss,"req_"+i[4])(url,data)
                # getattr(woniuboss,"asert"+i[8].strip())
                # 判断是否以状态码断言
                if asertMethod == "code":
                    woniuboss.asertcode(content, code,title)
                # 判断响应正文是否相等
                elif asertMethod == "text":
                    woniuboss.asertText(content, text,title)
                # 判断响应正文是否包含
                elif asertMethod == "json":
                    woniuboss.asertjson(content, text,title)
                # 判断响应头部
                elif asertMethod == "header":
                    woniuboss.asertHeaders(content, text,title)
                else:
                    print("断言方法有问题")
            elif requst_type=="get":
                content = woniuboss.req_get(url)
                # 判断是否以状态码断言
                if asertMethod == "code":
                    woniuboss.asertcode(content, text,title)
                # 判断响应正文是否相等
                elif asertMethod == "text":
                    woniuboss.asertText(content, text,title)
                # 判断响应正文是否包含
                elif asertMethod == "json":
                    woniuboss.asertjson(content, text,title)
                # 判断响应头部
                elif asertMethod == "header":
                    woniuboss.asertHeaders(content, text,title)
                else:
                    print("断言方法有问题")
            else:
                print("请求方法有问题",i[4])
        except:
            print("异常，测试失败 ",i[0])

if __name__ == '__main__':

        runtest()

