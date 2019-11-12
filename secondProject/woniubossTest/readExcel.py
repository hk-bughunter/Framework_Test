import xlrd
def readExcel():
    file=xlrd.open_workbook(r"C:\Users\Administrator.USER-20190305CL\Desktop\inter.xlsx")
    file_conten=file.sheet_by_name("Sheet1")
    row=file_conten.nrows
    datalist=[]
    for i in range(row):
        #读取文件
        reqlist=file_conten.row_values(i,4,10)
        i = i + 1
        #将列表追加在空列表，构建二维列表
        datalist.append(reqlist)
    #删除读取到的第一个元素
    datalist.pop(0)
    # print(datalist)
    return datalist
readExcel()