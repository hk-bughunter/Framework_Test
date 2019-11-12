**我是本框架的自述文件, 为什么非要有这句话? 看其他项目都有个readme.md 不来个感觉不太好.**


**版本信息:**
Vol.0.2

**common:**
整个测试框架的基本结构所在路径

    1. captcha.py 验证码图片经过该文件操作返回验证码的字符串

    2.origin.py 框架的基本语法以及底层调用所在 要读代码建议从这里开始
    提供的方法: sleep click handle_click input chains verdict quit select captcha
    
    3.support.py origin.py的支持模块 包含各种错误处理, 辅助功能等
    
    4.yundamAPIx64.dll captcha.py支持文件
    
**data:**
整个框架传入的数据 

**imgs:**
存放包括错误截图, 验证码图片目录

**log:**    
存放错误日志以及断言日志

**result:**
html结果报告以及邮件发送

**case:**
通过对origin.py操作的基本封装 制作成单个模块的基本操作事件 请仿照LoginCase.py进行编写

**suite**
通过对case中模块的事件进行组成封装成的测试套件 请仿照Login.py进行编写

**注意事项:**
每个模块即每个页面之间除登陆外相互不关联; 编写case时尽量降低耦合性
脚本中难免还有会错误 会持续改进

**更新日志:**
添加pytest自动化测试构建, 优化脚本 完成html报告生成以及发送邮件

使用操作 运行send_email.py文件