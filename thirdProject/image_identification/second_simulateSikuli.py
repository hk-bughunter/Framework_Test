import time,os
from PIL import Image, ImageGrab
class ImageMatch:
    # 获取RGB
    def get_pixel(self):
        # path = os.path.abspath('./')
        small = Image.open('./login.png')
        small_rgb = small.load()
        if small.mode == 'RGBA':
            big = ImageGrab.grab().convert('RGBA')
        else:
            big = ImageGrab.grab()
        big_rgb = big.load()
        # print(small.width,small.height)
        # return small, big, small_rgb, big_rgb

    def find_image(self):
        small, big, small_rgb, big_rgb = self.get_pixel()
        for x in range(big.width - small.width):
            for y in range(big.height - small.height):
                for i in range(small.width):
                    for j in range(small.height):
                        if big_rgb[x + i, y + j] != small_rgb[i, j]:
                            print("没有该图片")
                            return False
                return (x + small.width) / 2, (y + small.height) / 2

    def open(self):
        os.popen(r"C:\Users\Administrator.USER-20190305CL\AppData\Local\Google\Chrome\Application\chrome.exe http://localhost:8081/agileone/Agileone_1.2")

if __name__ == '__main__':
    match=ImageMatch()
    match.open()
    time.sleep(3)
    match.find_image()