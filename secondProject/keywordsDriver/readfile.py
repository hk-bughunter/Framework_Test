import os
class parser():
    @classmethod
    def readAndAnalysis(cls):
        dt=[]
        # filepath=os.path()
        with open('data.txt','r',encoding='utf8') as f:
            # data=f.readline()
            while True:
                data = f.readline()
                if not data:
                    break
                else:
                    dt.append(data.strip('\n').split(','))
            # for testdata in dt:
            #     testdata.strip().split(',')[0]
            #     print(testdata)
            return dt

# if __name__ == '__main__':
#     a=parser.readAndAnalysis()
#     for data in a:
#         print(data[0])
#     # print(parser.readAndAnalysis())


