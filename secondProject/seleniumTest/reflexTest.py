class persion():
    def __init__(self,name):
        self.name=name
    def singsong(self):
        print('{}正在唱歌'.format(self.name))
    def playbasketball(self):
        print('{}打篮球'.format(self.name))

if __name__ == '__main__':
    onepersion=persion('hk')
    choice=input('请输入属性名')
    # if hasattr(onepersion,choice):
    #     f=getattr(onepersion,choice)
    #     try:
    #         f()
    #     except TypeError:
    #         print(f)
    value=input('请输入要设置的属性值')
    setattr(onepersion,choice,value)
    if hasattr(onepersion,choice):
        f=getattr(onepersion,choice)
        f()