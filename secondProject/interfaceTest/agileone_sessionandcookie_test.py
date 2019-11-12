import http.client
import random,re
#使用http.clien库测试agileone的登录和添加功能
class AgileoneInterTest():
    #获取首页
    # def __init__(self):
    #     conn = http.client.HTTPConnection("localhost", port=8081)
    #     conn.request("GET","/agileone/Agileone_1.2/")
    #     self.setcookie=conn.getresponse().getheader("Set-Cookie")
    #     self.sessionid=self.setcookie.split(";")[0]
    #     print(self.sessionid)
    #     # return self.sessionid
    #     # print(setcookie)
    #     # print(sessionid)
    #登录Agileone，因为添加需要用到cookie，则将登录测试写做构造方法
    def __init__(self):
        client = http.client.HTTPConnection("localhost", port=8081)
        header1 = {"Content-Type": "application/x-www-form-urlencoded"}
        body = "username=admin&password=admin&savelogin=true"
        client.request('POST', '/agileone/Agileone_1.2/index.php/common/login', headers=header1, body=body)
        #获取到cookie，前面加self设为全局变量方便下面的测试方法调用
        response=client.getresponse()
        self.setcookie=response.getheader("Set-Cookie")
        print(self.setcookie)
        # 因为得到的cookie有多个字段，所以切割取第一个PHPSESSID即可，也可将cookie全部传参
        self.sessionid=self.setcookie.split(";")[0]
        print(self.sessionid)
        res = response.read().decode()
        if res=="successful":
            print("登录成功")
        else:
            print("登录失败")
    #需求提案的添加，注意请求正文body若重复添加会提示proposal_exist
    def addrequstion(self):
        sequence=random.randint(100,200)
        conn = http.client.HTTPConnection("localhost", port=8081)
        body="type=Requirement&importance=Medium&headline=test%d&content=world%d&processresult=sss"%(sequence,sequence)
        #将构造方法的cookie调用写入header
        header={"Content-Type":"application/x-www-form-urlencoded","Cookie":self.sessionid}
        conn.request("POST","/agileone/Agileone_1.2/index.php/proposal/add",headers=header,body=body.encode())
        response=conn.getresponse()
        result_res=response.read().decode()
        #利用正则表达式断言
        if re.match("^\d{2,}$",result_res):
            print("新增成功")
        else:
            print("新增失败")
        print(re)

if __name__ == '__main__':
    aglieone=AgileoneInterTest()
    aglieone.addrequstion()