import json, re, requests


class Operation:
    def __init__(self):
        self.page = None
        self.url = "https://www.ssyer.com/apis/20001"
        self.session = requests.session()
        self.headers= {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "UserCookie": "SESSION=41e79fff-f05e-4356-b1a9-cde99d13f75a;path=/;HttpOnly"
        }


    def main(self, end_index):
        for i in range(1, int(end_index)):
            data = {
                "cateId": "1",
                "page": {
                    "showCount": "20",
                    "currentPage": str(i)
                }             
            }
            # 链接json
            response = self.session.request(method="post", url=self.url, headers=self.headers, verify=True, data=json.dumps(data))
            text = str(response.json())
            # 图片地址
            re_img = re.compile("'showUrl': '(.*?)'")
            self.img = re_img.findall(text)
            # 标题地址
            re_title = re.compile("'title': '(.*?)'")
            self.title = re_title.findall(text)
            # 写入
            self.write()

    def write(self):
        # 写入
        for i in range(len(self.img)):
            title = "./imgs/"+self.title[i]+".jpg"
            print(self.img[i])
            print(title)
        # 防止title中含有非法字符
            try:
                with open(title, "wb") as img:
                    img.write(requests.get(url=self.img[i]).content)
            except Exception:
                continue

    def run(self, end_index):
        """
        end_index must be int and end_index >=2

        """
        self.main(end_index)


if __name__ == '__main__':
        Operation().run(50)