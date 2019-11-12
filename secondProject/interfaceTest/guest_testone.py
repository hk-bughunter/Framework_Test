import unittest,requests,ddt
import BSTestRunner
def get_testdata():
    testdata = [{"eid": "818", "name": "金立1", "limit": "5000", "address": "beijing", "start_time": "2016-09-11 12:00:00"}]
    return testdata
@ddt.ddt
class Guesttest(unittest.TestCase):
    def setUp(self):
        # data={"username":"admin","password":"admin123456"}
        # self.session=requests.Session().post(url="http://localhost:8000/login_action/",data=data)
        # self.session

        print(*get_testdata())

    @ddt.data(get_testdata())
    @ddt.unpack
    def testsign(self,data):
        con = requests.request(method="POST", url="http://127.0.0.1:8000/api/add_event/", data=data)
        re = con.content
        print(re)
    # print(get_testdata())
        # testdata=self.get_testdata()
        # for data in testdata:
        #     con=requests.request(method="POST",url="http://127.0.0.1:8000/api/add_event/",data=data)
        #     re=con.content
        #     print(re)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()