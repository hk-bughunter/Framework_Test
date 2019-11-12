import unittest,requests,ddt,parameterized
import BSTestRunner

class Guesttest(unittest.TestCase):
    @parameterized.expand(
        ()
    )
    def testaddsign(self,eid,name,limit,address,start_time,time,sign,expected):
        data={"eid":eid,"name":name,"limit":limit,"address":address,
              "start_time":start_time,"time":time,"sign":sign}
        con=requests.request(method="POST",url="http://127.0.0.1:8000/api/sec_add_event/",data=data)
if __name__ == '__main__':
    unittest.main()