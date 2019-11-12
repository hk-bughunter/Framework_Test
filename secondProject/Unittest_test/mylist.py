import unittest
class mylist:
    def __init__(self,list):
        self.list = list
    #删除列表中最后一个元素

    def mypop(self):
        newlist = []
        for i in range(len(self.list)-1):
            newlist.append(self.list[i])
        self.list = newlist
        return self.list

    # @unittest.skip
    #删除列表中从index下标开始的count个元素
    def myremove(self,index,count):
        for i in range(index,len(self.list)-count):
            self.list[i] = self.list[i+count]
        for i in range(count):
            self.mypop()
        return self.list
    #从下标insert开始，插入一个元素value
    def myinsert(self,index,value):
        newlist = []
        for i in range(len(self.list)):
            if index == i:
                newlist.append(value)
            newlist.append(self.list[i])
        self.list = newlist
        return self.list
    #检查列表中是否全部是数字，是返回True，否返回False
    def myallnumber(self):
        isnumber = True
        for i in self.list:
            if not isinstance(i,(int)):
                isnumber = False
                break
        return isnumber
    #统计列表中元素value的次数
    def mycount(self,value):
        c = 0
        for i in self.list:
            if i == value:
                c = c + 1
        return c
    #判定类表中是否出现重复的元素值，如果有返回True，没有返回False。
    def myisdup(self):
        isdup = False
        for i in self.list:
            if self.mycount(i) > 1:
                isdup = True
                break
        return isdup
# if __name__ == '__main__':
#     suit=unittest.TestSuite()
#     suit.addTest([mylist('mypop')])
#     unittest.TextTestRunner().run(suit)