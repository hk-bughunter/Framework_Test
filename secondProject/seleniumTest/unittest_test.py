# baiduTest.setUp()
import unittest
class baiduTest(unittest.TestCase):
    def setUp(self):
        print('setup running')

    def tearDown(self):
        print('tearDown running')
    def testOpen(self):
        print('testOpen running')

    def testClose(self):
        print('testClose running')

if __name__ == '__main__':
    # unittest.main()
    ts=unittest.TestSuite()
    ts.addTests([baiduTest('testOpen'),baiduTest('testClose')])
    unittest.TextTestRunner().run(ts)