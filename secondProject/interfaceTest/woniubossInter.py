import requests
class Woniuboss:
    # @classmethod
    # def __init__(cls):
    #     cls.session=requests.session()
    # # def login(self):
    # @classmethod
    # def req_get(cls,url):
    #     Response=cls.session.get(url)

    @classmethod
    def req_post(cls,url,data):
        response=requests.post(url,data)
        a=response.text
        print(a)
