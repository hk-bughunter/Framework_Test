from GUI_keywordDriven.gui_parse_testdata import Parse
from GUI_keywordDriven.gui_keywords import Keywords
from selenium import webdriver
driver = webdriver.Chrome()     #实例化对象
driver.implicitly_wait(3)   #隐式等待
TEST_data = Parse.getdata()     #获取测试数据
with open("gui_testlog.txt", "w", encoding="utf-8") as f: #处理日志文件
    f.write("")
print("WoniuBoss GUI自动化测试 开始ing>>>>>>")
for par in TEST_data:           #遍历执行测试数据
    if par[0].startswith('#'):
        title = par[0][1:]
        print(title)
    else:
        try:
            if par[0].startswith("check"):
                getattr(Keywords,par[0])(driver,par,title)
            else:
                getattr(Keywords, par[0])(driver,par)
        except:
            print("该条脚本数据有问题，执行错误")
            with open("gui_testlog.txt", "r+", encoding="utf-8") as fi:  # 将错误用例写入脚本
                con = fi.readlines()
                logmsg = f"测试失败：>>>异常>>>{title}"
                loglist=[]
                for i in con:                #处理重复的输入
                    k=i.strip("\n")
                    loglist.append(k)
                if logmsg not in loglist:
                    fi.write(logmsg+"\n")
            continue


