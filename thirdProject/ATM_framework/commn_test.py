from ATM_framework.commn_action import Action
class testSuite:
    def __init__(self):
        pass
    def do_login(self,user,pwd,button,username,password):
        act=Action()
        dr_user,dr_pwd,dr_click=act.get_login_username(user,pwd,button)
        dr_user.send_key(username)
        dr_pwd.send_key(password)
        dr_click.click()
