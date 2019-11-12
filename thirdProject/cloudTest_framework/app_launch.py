import glob
import subprocess,os,time

class AppLaunch:
    def __init__(self):
        self.apk_list=glob.glob(r"D:\apk\*.apk")
        self.pack_Act={'com.miui.calculator':'.cal.CalculatorActivity','com.tencent.qqmusic': 'com.tencent.qqmusic.activity.AppStarterActivity', 'com.tencent.mobileqq': 'com.tencent.mobileqq.activity.SplashActivity'}
        print(self.apk_list)

    #安装apk
    def install_apk(self):
        for apk in self.apk_list:
            print(apk)
            #利用aapt命令获取包名
            output_1=os.popen("aapt dump badging %s | findstr package"%apk).read()
            # output=subprocess.check_output("aapt dump badging %s | findstr package"%apk)
            package=str(output_1).split("'")[1] #获取包名
            output_2=os.popen("aapt dump badging %s | findstr launchable-activity"%apk).read()
            activity=str(output_2).split("'")[1] #获取activity
            self.pack_Act[package]=activity  #将包名和activity写入空的字典
            print(self.pack_Act)
            result=os.popen("adb install -r %s"%apk).read()
            if 'Failure' in result:
                print("安装%s失败"%apk)
            elif 'Success' in result:
                print("安装%s成功"%apk)
            else:
                print("无结果")

    #打开app
    def run_app(self):
        for package,activity in self.pack_Act.items():
            result=os.popen("adb shell am start -n %s/%s"%(package,activity)).read()
            print(result)
            time.sleep(2)
            print(package,activity)

    #卸载app
    def unistall_app(self,package):
        result=os.popen("adb uninstall %s"%package).read()
        if "Sucess" in result:
            print("卸载成功")
        else:
            print("卸载失败")

    #monkey测试app
    def monkey_app(self,package):
        # for package,activity in self.pack_Act.items():
        log_path='D:/monkey.log'
        os.popen("adb shell monkey -p %s -v -v --throttle 500 100 >%s"%(package,log_path))
        with open(log_path,encoding='utf-8') as file:
            content=file.read()
        if 'Crash' in content or 'crash' in content:
            print('运行%s时崩溃'%package)
        elif "ANR" in content or 'NOT RESPONDING' in content:
            print('运行%s时无响应'%package)
        elif 'Exception' in content or 'exception' in content or 'error' in content:
            print('运行%s时出现异常'%package)
        elif 'aborted' in content:
            print('%s未正常运行'%package)
        else:
            print('运行%s正常'%package)

if __name__ == '__main__':
    app=AppLaunch()
    # app.install_apk()
    # app.run_app()
    pack="com.miui.calculator"
    app.monkey_app(pack)
