class Parse:
    @classmethod
    def getdata(cls):
        """读取脚本文件"""
        with open(r'data.txt', 'r', encoding='utf8')as file:
            data = file.readlines()
            datalisi = []
            for i in data:
                result = i.strip('\n').split(',')
                datalisi.append(result)
        return datalisi



# if __name__ == '__main__':
