from selenium import webdriver

class Action:

    def __init__(self,dr):
        self.dr=dr
    def get_login(self,username,password,button):
        dr_user=self.dr.find_element_by_id(username)
        dr_pwd=self.dr.find_element_by_id(password)
        dr_click=self.dr.find_element_by_id(button)
        return dr_user,dr_pwd,dr_click
    def get_notice(self):
        pass

    # def get_login_pwd(self):
    #     return self.dr.find_element_by_id("password")

    # def get_driver(self):

