from 关键字框架.parse_testdata import Parse
from 关键字框架.keywords import Keywords
from selenium import webdriver
driver = webdriver.Chrome()
# driver.implicitly_wait(5)
TEST_data = Parse.getdata()
for par in TEST_data:
    if par[0].startswith('#'):
        print(par[0])
        # pass
    else:
        getattr(Keywords,par[0])(driver,par)
# driver.switch_to.default_content()