from seleniumTest.calcuMethod import *
class hkcalculator():
    def __init__(self):
        pass
    def calculater(self):
        string= input('请输入你要计算的数据：')
        lista=['+','-','*','/']
        for i in string:
            if i in lista:
                num1=int(string.split(i)[0])
                num2=int(string.split(i)[1])
                return (num1,num2,i)
if __name__ == '__main__':
    cal=hkcalculator()
    (x,y,op)=cal.calculater()
    # print(cal.calculater())
    setattr(cal, '+', add)
    setattr(cal, '-', reduce)
    setattr(cal, '/', divid)
    setattr(cal, '*', mutiply)
    result = getattr(cal, op)(x, y)
    print(result)
    print(dir(cal))
    delattr(cal,'*')
    print(dir(cal))
    # dict_demo={'+':add,'-':reduce,'/': divid,'*':mutiply}
    # result=dict_demo[op](x,y)
    # print(result)




