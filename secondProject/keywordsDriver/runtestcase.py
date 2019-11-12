from keywordsDriver.keywords import Keydriver
from keywordsDriver.readfile import parser
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
cmd=parser.readAndAnalysis()
print(cmd)
for data in cmd:
    method=data[0]
    print(method)
    # print(path)
    # func = getattr(Keydriver, method)
    # func(driver, data.strip())
    if method.startswith('#'):
       continue
    else:
        func=getattr(Keydriver,method)
        func(driver,data)

