import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class Mail:
    def __init__(self, recv=['703870955@qq.com', '1321683164@qq.com']):
        self.sender = 'student@woniuxy.com'
        self.recevices = recv
        self.message = None

    def content(self, sender, recver, title, content, path):
        message = MIMEMultipart()
        message['From'] = Header(sender)
        message['To'] = Header(recver)
        message['Subject'] = Header(title)

        message.attach(MIMEText(content, 'plain', 'utf-8'))

        attr2 = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
        attr2["Content_Type"] = 'application/octet-stream'
        attr2['Content-Disposition'] = 'attachment; filename="report'
        message.attach(attr2)
        return message

    def run(self, sender='Epip', recver="BugHunter", title='TinySoup测试报告', content='TinySoup自动化测试完成 请查收报告!', path='./report.html'):
        message = self.content(sender, recver, title, content, path)

        smtpObj = smtplib.SMTP()
        smtpObj.connect('mail.woniuxy.com', 25)
        smtpObj.login(user='student@woniuxy.com', password='Student123')
        smtpObj.sendmail(self.sender, self.recevices, message.as_string())
        smtpObj.quit()

if __name__ == '__main__':
    Mail().run()