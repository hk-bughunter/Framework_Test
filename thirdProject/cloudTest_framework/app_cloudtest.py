import socket
import subprocess,time,os
class CloudTest:
    def __init__(self):
        pass

    def get_devices(self):
        list=[]
        port=5000
        bpport=8000
        devices=subprocess.check_output("adb devices").decode().strip().split("\r\n")
        for i in range(1,len(devices)):
            udid=devices[i].split("\t")[0]
            if udid!="":
                version=subprocess.check_output("adb -s "+udid+" shell getprop ro.build.version.release").decode().strip()
                port=self.find_port(port)
                bpport=self.find_port(bpport)
                list.append(udid+"##"+version+"##"+str(port)+"##"+str(bpport))
        return list

    def find_port(self,port):
        while True:
            if self.check_port(port):
                port+=1
            else:
                break
        return port

    def check_port(self,port):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect(("127.0.0.1",port))
            s.shutdown(2)
            return True
        except:
            return False



if __name__ == '__main__':
    cloud=CloudTest()
    list=cloud.get_devices()
    print(list)