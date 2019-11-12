import uiautomator2,os,threading

class CloudtestU2:
    def __init__(self):
        pass

    def get_devices(self):
        udid_list=[]
        devices_list=os.popen("adb devices").read().strip().split('\n')
        for i in range(1,len(devices_list)):
            udid=devices_list[i].split('\t')[0]
            udid_list.append(udid)
        return udid_list

    def test_app(self,udid,package):
        u2=uiautomator2.connect(udid)
        u2.app_start(pkg_name=package)
        s=u2.session(pkg_name=package,attach=True)
        s.implicitly_wait(20)

if __name__ == '__main__':
    cloudtest=CloudtestU2()
    udid_list=cloudtest.get_devices()
    print(udid_list)
    package = "io.dcloud.cinema"
    for udid in udid_list:
        threading.Thread(target=cloudtest.test_app,args=(udid,package)).start()
    # udid='127.0.0.1:62025'
