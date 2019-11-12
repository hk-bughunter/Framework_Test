import pymysql,os,time
from html_report.database_achieve import DatabaseArchive
class ArchiveHtml:
    def __init__(self):
        pass

    def replace_html(self,version):
        readData=DatabaseArchive() #实例化封装好的读取数据库类
        html_path=os.path.abspath('.')+'\python_report.html'
        with open(html_path,mode='r',encoding='utf-8') as file:
            content=file.read()
        testtime = time.strftime("%Y-%m-%d")
        content=content.replace("$test_date",testtime) #替换报告生成时间
        # sql="select version from woniucbt where id='1'"
        # version=readData.read_onedata_mysql(sql)[0]
        content = content.replace('$test_version', version)
        sql = "select count(*) from woniucbt where result ='Pass';"
        pass_count = readData.read_onedata_mysql(sql)[0]  # 调用读取数据库的方法获取用例通过数量
        content = content.replace('$pass_count', str(pass_count))
        sql== "select count(*) from woniucbt where result ='Fail';"
        fail_count=readData.read_onedata_mysql(sql)[0]  #读取用例失败的数量
        sql == "select count(*) from woniucbt where result ='错误';"
        content = content.replace('$fail_count', str(fail_count))
        error_count=readData.read_onedata_mysql(sql)[0]   #读取用例错误的数量
        content=content.replace('%error_count',str(error_count))
        lasttime = time.strftime("%Y-%m-%d %H:%M:%S")
        content=content.replace('$last_time',lasttime)

        test_result=''
        sql='select * from woniucbt where version="%s"'%version
        results=readData.read_alldata_mysql(sql)
        print(results)
        for record in results:
            test_result+="<tr height='40'>"
            test_result+=f'<td width="7%">{record[0]}</td>'
            test_result +=f'<td width="9%">{record[2]}</td>'
            test_result+=f'<td width="9%">{record[3]}</td>'
            test_result += f'<td width="7%">{record[4]}</td>'
            test_result += f'<td width="20%">{record[5]}</td>'
            if record[6]=='Pass':
                test_result += f'<td width="7%" bgcolor="lightgreen">{record[6]}</td>'
            else:
                test_result += f'<td width="7%" bgcolor="red">{record[6]}</td>'
            test_result += f'<td width="16%">{record[7]}</td>'
            test_result += f'<td width="15%">{record[8]}</td>'
            if record[9]=='':
                test_result += f'<td width="10%">{record[9]}</td>'
            else:
                test_result += f'<td width="10%"><a href={record[9]}</a></td>'
        content=content.replace("$test_result",test_result)
        newhtml_path=os.path.abspath('.')+'\\new.html'
        with open(newhtml_path,'w',encoding='utf-8') as file:
            file.write(content)
        # print(content)
if __name__ == '__main__':
    aa=ArchiveHtml()
    version = '1.1.0'
    # result="Fail"
    # sql="select count(*) from woniucbt where result ='%s'"%result
    # sql = "select version,module,testtype,caseid,casetitle,result,error," \
    #       "screenshot from woniucbt where version='%s'" % version

    aa.replace_html(version)