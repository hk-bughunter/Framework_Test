import xlrd
class Parse:
    """获取测试用例"""
    @classmethod
    def get_data(cls):
        #打开文件
        data = "D:\蜗牛\测试软件\PyCharm Community Edition 2019.2\workspace\WoniuBoss接口测试框架\woniuboss接口测试用例.xlsx"
        book = xlrd.open_workbook(data)
        #获取焦点
        lie = book.sheets()[0]
        #创建一个空列表接收测试用例
        testcase=[]
        #遍历excel文件将文件内容添加到列表中
        for i in range(lie.nrows):
            li=lie.row_values(i)
            testcase.append(li)
        testcase=testcase[1:]    #处理首行
        #将excel中浮点型的状态码转换为int
        for k in testcase:
            if type(k[7]) is not str:
                # k[7] = str(k[7])[:3]
                k[7] = int(k[7])
        return testcase

if __name__ == '__main__':
    testcase=Parse.get_data()
    print(testcase)
    print(len(testcase))