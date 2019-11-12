import os,threading
import subprocess

class CloudMonkey:
    def __init__(self):
        self.path=os.path.abspath(".")

    def get_devices(self):
        list=[]
        devices=subprocess.check_output("adb devices").decode().strip().split("\r\n")
        for i in range(1,len(devices)):
            udid=devices[i].split("\t")[0]
