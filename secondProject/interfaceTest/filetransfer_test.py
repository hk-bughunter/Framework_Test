import requests
def test_download_img():
    con=requests.get(url="http://pic27.nipic.com/20130330/8648390_164218404105_2.jpg")
    content=con.content
    with open("D:\pig.png","wb") as f:
        f.write(content)
    print(con.status_code)
def test_transfer_img():
    #先定义文件字典key为请求上传框的属性，如name、id，跟open（"路径","rb"）以二进制读取
    file={"fileToUpload":("test.png",open("D:\pig.png", "rb"))}#test.png为重命名上传文件名，可要可不要
    url="http://192.168.3.182:8081/agileone/Agileone_1.2/index.php/attach/upload/refertype/defect/referid/4"
    con=requests.post(url=url,files=file)
    test_re=con.text
    print(test_re)


if __name__ == '__main__':
    test_transfer_img()
