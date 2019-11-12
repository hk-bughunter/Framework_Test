import time, os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.common.captcha import query
from PIL import Image, ImageGrab


class Support:
    # 查找元素类型支持列表
    mode_list = ["xpath",
                 "link text",
                 "xpath",
                 "name",
                 "id",
                 "css selector",
                 ]

    # 获取driver实例初始化
    def __init__(self, driver):
        self.driver = driver

    # 检查元素是否存在
    def _checkele(self, mode):
        # 在五秒内每隔0.5s检查一次元素是否出现 超时则报timeout错误 跳转至被调用的except
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(mode))

    # 检查元素查询方式
    def _checkmode(self, method, position):
        # 将查询方式字符小写
        method = method.lower()

        # 判断查询方式是否存在于查询列表中
        if method in Support.mode_list:
            # 封装find_element对象为元组
            mode = (method, position)
            return mode
        else:
            return None

    # 未找到元素错误提示
    def _error_timeout(self, mode, action):
        logtime = time.strftime('%Y-%m-%d %H:%M:%S')
        imgtime = time.strftime('%Y%m%d%H%M%S')
        # 错误提示信息
        msg = f"页面未找到该元素:{mode} 操作类型:{action} 时间:{logtime} 截图已保存在{os.path.abspath('../imgs/')}下 文件名为:{imgtime}.png"
        print(msg)

        # 调用截图方法 将本次错误操作保存
        self._screen(imgtime)
        # 输出本次错误操作到错误日志
        with open("../log/error.log", "a+", encoding="GBK") as file:
            file.write(f"\n{msg}")


    # 查找方式不正确错误提示
    def _error_type(self,method , action):
        logtime = time.strftime('%Y-%m-%d %H:%M:%S')
        imgtime = time.strftime('%Y%m%d%H%M%S')

        msg = f"查找方式不正确:{(method,)} 操作类型:{action} 时间:{logtime} 查询方式请参阅:{os.path.abspath('.')}\\support.modelist 截图已保存在{os.path.abspath('../imgs/')}下 文件名为:{imgtime}.png"
        print(msg)

        self._screen(imgtime)

        with open("../log/error.log", "a+", encoding="GBK") as file:
            file.write(f"\n{msg}")

    # 下拉框选择不正确错误提示
    def _error_sele(self, action):
        logtime = time.strftime('%Y-%m-%d %H:%M:%S')
        imgtime = time.strftime('%Y%m%d%H%M%S')

        msg = f"操作类型:{action} 仅支持select_by_index;请传入选择项下标 时间:{logtime} 截图已保存在{os.path.abspath('../imgs/')}下 文件名为:{imgtime}.png"
        print(msg)

        self._screen(imgtime)

        with open("../log/error.log", "a+", encoding="GBK") as file:
            file.write(f"\n{msg}")

    def _js(self, mode):
        # 如果查询方式使用 id或者name 则将边框变色方便标识
        if mode[0] == "id":
            js = f'q=document.getElementById("{mode[1]}");q.style.border=\"1px solid #f0e\";'
            self.driver.execute_script(js)
        if mode[0] == "name":
            js = f'q=document.getElementsByName("{mode[1]}")[0];q.style.border=\"1px solid #f0e\";'
            self.driver.execute_script(js)

    # 截图
    def _screen(self, imgname="baseimg"):
        # 使用webdriver方法截图
        path = f"{os.path.abspath('../imgs/')}\\{imgname}.png"
        self.driver.get_screenshot_as_file(path)
        # ImageGrab.grab().save(path)

    # 获得验证码
    def _captcha(self, driver):
        # 先将底图截图
        self._screen()

        # 获得验证码图片的长宽, 相对位置
        size = driver.size
        location = driver.location

        # 组装验证码在底图中的位置
        captcha_location = (int(location['x']),
                            int(location['y']),
                            int(location['x'] + size['width']),
                            int(location['y'] + size['height']))

        # 保存验证码
        source_img = Image.open(f"{os.path.abspath('../imgs/')}\\baseimg.png")

        # 使用Image.crop方法在底图中匹配验证码
        captcha_img = source_img.crop(captcha_location)
        # 将得到的验证码图片保存
        captcha_img.save(f"{os.path.abspath('../imgs/')}\\captcha.png")

        # 使用自己封装的query方法返回验证码的字符串
        path = f"{os.path.abspath('../imgs/')}\\captcha.png"
        return query(path)






