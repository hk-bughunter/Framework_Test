import time,os,subprocess
from pom_framwork.object_action import action
from configparser import ConfigParser
from common.option_config import ConfigOpetion
class CI:
    def __init__(self):
        self.config=ConfigParser()
        # self.file_path='C:\\Users\Administrator.USER-20190305CL\Desktop\woniusales'
        # self.svn_url='https://USER-20190305CL:8443/svn/woniusales/'
        # self.tomcat_path='D:\\apache-tomcat-8.5.11'
        self.config.read('./ci.conf')
        self.file_path=self.config.get('ci','file_path')
        self.svn_url = self.config.get('ci', 'svn_url')
        self.tomcat_path = self.config.get('ci', 'tomcat_path')
        print(self.file_path,self.svn_url,self.tomcat_path)
    #从svn的server端更新out
    def download_svn(self):
        if os.path.exists(self.file_path):
            os.system(f'svn update {self.file_path}')
        else:
            #如果没有该文件则建立连接
            os.mkdir(self.file_path)
            os.system(f'svn checkout {self.svn_url} {self.file_path} --username hk --password 123456')
        print('完成源码的更新')
    #利用ant来编译源文件为war文件
    def ant_compile(self):
        os.system('ant -f %s\\build.xml'%self.file_path)
    #将war文件部署在tomcat服务器
    def deploy(self):
        os.system('%s\\bin\shutdown.bat'%self.tomcat_path)    #部署前先关闭tomcat
        os.system('copy /Y %s\\woniusales.war %s\\webapps'%(self.file_path,self.tomcat_path)) #将war包复制到tomcat服务器
        listdir=os.listdir('%s\\webapps'%self.tomcat_path)
        print(listdir)

        if 'woniusales' in listdir:    #判断如果woniusales文件在webapps下则替换db_propeties
            os.system('rd /S /Q %s\\webapps\\woniusales'%self.tomcat_path)
            os.system('%s\\bin\startup.bat' % self.tomcat_path)  # 重新打开tomcat服务器
            time.sleep(3)
            with open('%s\\webapps\woniusales\WEB-INF\classes\db.properties'%self.tomcat_path , 'w') as file:
                db_propeties = 'db_url=jdbc:mysql://localhost:3306/woniusales?useUnicode=true&characterEncoding=utf8\ndb_username=root\ndb_password=\ndb_driver=com.mysql.jdbc.Driver'
                file.write(db_propeties)
            time.sleep(30)
        elif 'woniusales' not in listdir:
            os.system('%s\\bin\startup.bat' % self.tomcat_path)
            time.sleep(40)
            with open(self.tomcat_path + '\\webapps\woniusales\WEB-INF\classes\db.properties', 'w') as file:
                db_propeties = 'db_url=jdbc:mysql://localhost:3306/woniusales?useUnicode=true&characterEncoding=utf8\ndb_username=root\ndb_password=\ndb_driver=com.mysql.jdbc.Driver'
                file.write(db_propeties)
        else:
            pass

    def start_GUItest(self):
        uiaction=action()
        uiaction.start_test()

    # def

if __name__ == '__main__':
    ci=CI()
    ci.download_svn()
    # ci.ant_compile()
    ci.deploy()
    ci.start_GUItest()
