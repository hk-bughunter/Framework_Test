import requests,time
# data={"eid":"22","name":"摩托罗拉发布会","limit":"500","address":"beijing","start_time":"2016-09-11 12:00:00"}
# con=requests.request(method="POST",url="http://127.0.0.1:8000/api/add_event/",data=data)
# re=con.content
# print(re)
# time=time.time()
# print(time)
# #sign 计算公式:
# api_key = '&Guest-Bugmaster'
# key=(str(time)+api_key).encode()
# md5=hashlib.md5()
# md5.update(key)
# sign = md5.hexdigest()

data={"eid":110,"name":"帕拉梅拉发布会","limit":200,"address":"chengdu",
              "start_time":"2016-09-11 12:00:00","time":1567687144,"sign":"boss"}
con=requests.request(method="POST",url="http://127.0.0.1:8000/api/sec_add_event/",data=data)

re=con.content
print(re)
# import unittest
# import ddt
# @ddt.ddt
# class MyTestCase1(unittest.TestCase):
#     @ddt.data([2,3,6])
#     def test_normal(self, value):
#         print(value)
#
# if __name__ == '__main__':
#     unittest.main()