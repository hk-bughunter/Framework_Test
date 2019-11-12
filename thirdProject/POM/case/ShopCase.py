from POM_GUI.common.origin import Base

class Shop(Base):
    URL = "http://192.168.3.111:8081/tinyshop3.0/index.php?con=simple&act=login"

    def __init__(self):
        super().__init__(url=self.URL)

    def username(self, content):
        self.input("id", "account", content)

    def password(self,content):
        self.input("name", "password", content)

    def login(self):
        self.click("xpath",'//*[@id="main"]/div/div/form/ul/li[4]/button')
        self.sleep()

    def time_limit_purchase(self):
        self.click("link text","限时抢购")
        self.sleep()

    def clothing(self):
        self.click('link text','服装')

    def commodity(self):
        self.click('xpath',"(.//*[normalize-space(text()) and normalize-space(.)='关注'])[1]/following::img[1]")

    def color(self):
        self.click('xpath',"(.//*[normalize-space(text()) and normalize-space(.)='S'])[1]/following::span[1]")

    def size(self):
        self.click('xpath',"//dl[2]/dd/ul/li[2]/span")


    def buy_immediately(self):
        self.click('xpath',"//a[@id='buy-now']/span")

    def close(self):
        self.quit()

    def assertion(self,method,position,text):
        self.verdict()

