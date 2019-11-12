import time,os,pymysql

class DatabaseArchive:
    def __init__(self):
        self.conn = pymysql.connect(user='root', password='', host='localhost', db='report', charset='utf8')
        self.cursor = self.conn.cursor()
    #往数据库中写入数据
    def wirte_data_mysql(self,version,module,testtype,caseid,casetitle,result,error,screenshot):
        testtime=time.strftime("%Y-%m-%d %H:%M:%S")
        # sql="insert into woniucbt (version,module,testtype,caseid,casetitle,testtime," \
        #     "result,error,screenshot) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(version,module,testtype,caseid,casetitle,testtime,result,error,screenshot)
        self.cursor.execute(sql)
        self.conn.commit()
    #往数据库中读取数据
    def read_onedata_mysql(self,sql):
        # sql="select version from woniucbt where caseid='%s';"%caseid
        self.cursor.execute(sql)
        # version, module, testtype, case, casetitle, result, error, screenshot=self.cursor.fetchone()
        result=self.cursor.fetchone() #获取到的是元祖
        return result
    def read_alldata_mysql(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        return result
    def __del__(self):
        self.cursor.close()
        self.conn.close()
if __name__ == '__main__':
    write=DatabaseArchive()
    # version, module, testtype, caseid, casetitle, result, error, \
    # screenshot='1.1.0','注册','GUI测试','TC_02','注册失效','Pass','',''
    # version='1.1.0'
    # module='注册'
    # testtype='GUI测试'
    # caseid='TC_02'
    # casetitle='注册失效'
    # result='Fail'
    # error=''
    # screenshot=''
    # write.wirte_data_mysql(version,module,testtype,caseid,casetitle,result,error,screenshot)
    version='1.1.0'
    sql = "select * from woniucbt where version='%s'" % version
    result=write.read_alldata_mysql(sql)
    print(result)
