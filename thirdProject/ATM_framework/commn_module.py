from selenium import webdriver
from ATM_framework.commn_test import testSuite
driver=webdriver.Chrome()
driver.get('http://localhost:8081/agileone/Agileone_1.2/')
test=testSuite()
testSuite.do_login('username','password','login','admin','admin')