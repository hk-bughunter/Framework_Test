import http.client
import requests,re
class WoniusalesTest():
    def __init__(self):
        testdata={"username":"admin","password":"Milor123","verifycode":"0000"}
        con=requests.request(method='POST',url='http://192.168.3.180:8080/woniusales/user/login',data=testdata)
        re=con.text
        self.cookie=con.cookies
        # print(re)
    def testBatch(self):
        data={"customerphone":"123234233"}
        con=requests.request(method="POST",url="http://192.168.3.180:8080/woniusales/customer/query",data=data)
        content1=con.content.decode()
        history=con.history
        statucode=con.status_code
        print(statucode)
        print(history)
        print(content1)
    def test_addmember(self):
        data={"customername":"未和","customerphone":"13322088309","childsex":"男","childdate":"2019-09-05","creditkids":"0","creditcloth":"0"}
        con=requests.request(method="POST",url="http://192.168.3.180:8080/woniusales/customer/add",data=data,cookies=self.cookie)
        statucode=con.status_code
        print(statucode)
    def test_transimg(self):
        # con=requests.get(url="http://pic27.nipic.com/20130330/8648390_164218404105_2.jpg")
        # content=con.content
        # with open("D:\pig.png","wb") as f:
        #     f.write(content)
        # print(con.status_code)
        file={""}
if __name__ == '__main__':
    woniu=WoniusalesTest()
    # woniu.testBatch()
    # woniu.test_addmember()
    woniu.test_transimg()