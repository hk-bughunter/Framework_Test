import re,os,time
import requests

class AppDownload:
    def __init__(self):
        pass
    def download(self):
        path='D:\\apk'
        con=requests.request(method="get",url="http://app.mi.com/topList")
        package_list=re.findall('<a href="/details\\?id=(.+?)">',con.text)
        package_set=set(package_list)
        package_list=list(package_set)
        # print(url_list)
        for package in package_list:
            print(package)
            response=requests.request(method='get',url="http://app.mi.com/details?id=%s"%package)
            down_list=re.findall('<a href="/download(.*)" class="download">',response.text)
            print(down_list)
            response=requests.get(' http://app.mi.com/download%s'%down_list[0])
            #以二进制的方式将下载好的apk放在文件下
            with open(path+'\%s.apk'%package,'wb') as file:
                file.write(response.content)


if __name__ == '__main__':
    appdown=AppDownload()
    appdown.download()