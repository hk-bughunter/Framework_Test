import os,time
from lxml import etree
class appXml:
    def __init__(self):
        self.path=os.path.abspath('.')+"\\data"

    #获取xml文件
    def get_xml(self):
        os.system("adb shell am start -n com.miui.calculator/com.miui.calculator.cal.CalculatorActivity")
        time.sleep(2)
        os.system("adb shell uiautomator dump")
        os.system("adb pull /storage/emulated/legacy/window_dump.xml %s"%self.path)

    #根据xpath定位
    def get_by_xpath(self,xpath):
        tree=etree.parse(self.path+"\\window_dump.xml")
        node_list=tree.xpath(xpath)
        print(node_list)
        bounds=node_list[0].get("bounds")
        print(bounds)
    def get_position(self,bounds):
        bounds=bounds.replace("[","",1)
        bounds=bounds.replace("][",",",1)
        bounds=bounds.replace("]","",)
        left_top_x=int()

if __name__ == '__main__':
    xmlFramework=appXml()
    # xmlFramework.get_xml()
    xmlFramework.get_by_xpath("//node")
