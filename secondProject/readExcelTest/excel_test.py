import xlrd
file=xlrd.open_workbook(r"C:\Users\Administrator.USER-20190305CL\Desktop\readtest.xlsx")
data=file.sheet_by_name("Sheet1")
row=data.nrows
print(row)
rowvalue=data.row_values(1,6,6)
print(rowvalue)
# for i in row:
#     print(data.col_values(i))

