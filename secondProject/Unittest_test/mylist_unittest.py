import unittest
from Unittest_test.mylist import mylist

import BSTestRunner
class tcmylist(unittest.TestCase):
    def setUp(self):
        self.lista=mylist([1,2,3,4,5])
    def tearDown(self):
        pass
    def testmypop(self):
        newlist=self.lista.mypop()
        self.assertListEqual([1,2,3,4],newlist)
    # @unittest.skip('强制跳过')
    # @unittest.expectedFailure
    def testmyinsert(self):
        newlist=self.lista.myinsert(2,9)
        self.assertEqual([1,2,9,3,4,5],newlist)
if __name__ == '__main__':
    #调用main直接运行
    # unittest.main()

    #用TestSuite构建后再调用TextTestRunner类实例化后调用run方法
    suit=unittest.TestSuite()
    suit.addTests([tcmylist('testmypop'),tcmylist('testmyinsert')])
    # unittest.TextTestRunner().run(suit)
    r = unittest.TestResult()
    # print(r.__dict__)
    suit.run(result=r)
    print(r)
    #用TestLoader来构建测试套件后调用TestResult方法保存运行结果，最后用实例化后的对象调用run方法
    # tc=unittest.TestLoader().loadTestsFromTestCase(tcmylist)
    # r=unittest.TestResult()
    # tc.run(result=r)

    #生成报告
    # tc=unittest.TestLoader().loadTestsFromTestCase(tcmylist)
    # outfile=open('mylist_report.html','w',encoding='utf8')
    # runner=BSTestRunner.BSTestRunner(stream=outfile,title='mylist测试',description='测试报告')
    # runner.run(tc)

    # suit=unittest.TestSuite()
    # suit.addTests([tcmylist('testmypop'),tcmylist('testmyinsert')])
    # r=unittest.TextTestRunner()
    # r.run(suit)