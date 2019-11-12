import requests
class KdyTest():
    def get_token(self):
        url="http://localhost:8081/kdy/index.php?user/loginSubmit&name=admin&salt=1&checkCode=undefined&password=C9ZRv52e3TS8xMZh2qYXzfAipqgL0aEqzpTfyIkY4oA_J9bCjWw&rememberPassword=1&isAjax=1"
        con=requests.get(url)
        print(con)
        dic=con.json()
        accesstoken=dic['data']
        print(accesstoken)
    def get_oenuser(self):
        pass

if __name__ == '__main__':
    kdy=KdyTest()
    kdy.get_token()
