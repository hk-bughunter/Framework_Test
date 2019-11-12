import pymysql,os

# def read(caseid):
#     conn=pymysql.connect(user='root', password='', host='localhost', db='report', charset='utf8')
#     cur=conn.cursor()
#     sql="select result from woniucbt where caseid='%s';"%caseid
#
#     cur.execute(sql)
#     version=cur.fetchall()
#     print(version)
# if __name__ == '__main__':
#     caseid='TC_02'
#     read(caseid)

html_path=os.path.abspath('.')+'\\python_report.html'
with open(html_path, mode='r', encoding='utf-8') as file:
    content = file.read()
print(content)