import os
file_path='C:\\Users\Administrator.USER-20190305CL\Desktop\woniusales'
svn_url='https://USER-20190305CL:8443/svn/woniusales/'
tomcat_path='D:\\apache-tomcat-8.5.11'
# os.system('svn update C:\\Users\\Administrator.USER-20190305CL\\Desktop\\woniusales')
# os.system('copy %s\\woniusales.war %s\\webapps'%(file_path,tomcat_path))
# os.system(f'svn checkout {svn_url} {file_path} --username hk --password 123456')
# os.system('%s\\bin\startup.bat'%tomcat_path)
listdir=os.listdir(file_path)
print(listdir)