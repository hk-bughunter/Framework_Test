import requests
class WoniusalesTest():
    #登录
    def testlogin(self):
        self.session=requests.session()
        url="http://192.168.3.180:8080/woniusales/user/login"
        data={"username":"admin","password":"Milor123","verifycode":"0000"}
        content=self.session.post(url=url,data=data).text
        # print(session)
        print(content)
        if content=="login-pass":
            print("登录成功")
        else:
            print("登录失败")
        #返回session
        return self.session
    def querybatch(self):
        url="http://192.168.3.180:8080/woniusales/sell/barcode"
        data={"barcode":"6955203636348"}
        content=requests.post(url=url,data=data).text
        print(content)
    def addmember(self):
        #调用登录成功的session
        sessio=self.testlogin()
        url="http://192.168.3.180:8080/woniusales/customer/add"
        data={"customername":"hk","customerphone":"11122203012","childsex":"男","childdate":"2019-09-09","creditkids":"0","creditcloth":"0"}
        # data={"customername":"hk","customerphone":"11122233388","childsex":"男","childdate":"2019-09-09","creditkids":"0","creditcloth":"0"}
        content=sessio.post(url=url,data=data).text
        print(content)
if __name__ == '__main__':
    woniusale=WoniusalesTest()
    # woniusale.testlogin()
    # woniusale.querybatch()
    woniusale.addmember()