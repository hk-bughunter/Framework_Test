import time,os

class CI:
    def __init__(self):
        self.file_path='C:\\Users\Administrator.USER-20190305CL\Desktop\woniusales'
        self.svn_url='https://USER-20190305CL:8443/svn/woniusales/'
        self.tomcat_path='D:\\apache-tomcat-8.5.11'
    #从svn的server端更新out
    def download_svn(self):
        try:
            os.system(f'svn update {self.file_path}')
        except:
            os.mkdir(self.file_path)
            os.system(f'svn checkout {self.file_path} {self.svn_url} --username hk --password 123456')
        print('完成源码的更新')
    #利用ant来编译源文件为war文件
    def ant_compile(self):
        os.system('ant -f %s\\build.xml'%self.file_path)
    #将war文件部署在tomcat服务器
    def deploy(self):
        os.system('copy %s\\woniusales.war %s\\webapps'%(self.file_path,self.tomcat_path))



if __name__ == '__main__':
    ci=CI()
    ci.ant_compile()
    ci.deploy()