import time,os
from PIL import Image, ImageGrab

class ImageMatch:
    # 获取RGB
    def get_pixel(self):
        small = Image.open('login.png')
        small_rgb = small.load()
        if small.mode == 'RGBA':
            big = ImageGrab.grab().convert('RGBA')
        else:
            big = ImageGrab.grab()
        big_rgb = big.load()

        for x in range(big.width - small.width):
            for y in range(big.height - small.height):
                print('-----------------------------------')
                if (big_rgb[x, y] == small_rgb[0, 0] and
                        big_rgb[x + small.width - 1, y] == small_rgb[small.width - 1, 0] and
                        big_rgb[small.width + x - 1, small.height + y - 1] == small_rgb[small.width - 1, small.height - 1] and
                        big_rgb[x, small.height + y - 1] == small_rgb[0, small.height - 1] and
                        big_rgb[x + int(small.width / 2), y + int(small.height / 2)] == small_rgb[int(small.width / 2), int(small.height / 2)]):

                    if self.check_match(small,big_rgb,x,y,small_rgb):
                        return (int(small.width / 2), int(small.height / 2))
        return -1, -1

    #先匹配五个点匹配
    # def match(self):
    #     small, big, small_rgb, big_rgb = self.get_pixel()
    #     for x in range(big.width - small.width):
    #         for y in range(big.height - small.height):
    #             if big_rgb[x, y] == small_rgb[0, 0] and big_rgb[x + small.width - 1, y] == small_rgb[small.width - 1, 0] \
    #                     and big_rgb[small.width + x - 1, small.height + y - 1] == small_rgb[small.width - 1, small.height - 1] \
    #                     and big_rgb[x, small.height + y - 1] == small_rgb[0, small.height - 1] \
    #                     and big_rgb[x + int(small.width / 2), y + int(small.height / 2)] == small_rgb[int(small.width / 2), int(small.height / 2)]:
    #
    #                 if self.check_match(x, y):
    #                     return small.width / 2, small.height / 2
    #     return -1, -1

    # def find_image(self):
    #     small, big, small_rgb, big_rgb = self.get_pixel()
    #     for x in range(big.width - small.width):
    #         for y in range(big.height - small.height):
    #             for i in range(small.width):
    #                 for j in range(small.height):
    #                     if big_rgb[x + i, y + j] != small_rgb[i, j]:
    #                         return False
    #             return (x + small.width) / 2, (y + small.height) / 2
    #             # if self.check_match(x, y):
                #     print("找到了")
                #     return (x + small.width) / 2, (y + small.height) / 2

    def check_match(self, small,big_rgb,x,y,small_rgb):
        # small, big, small_rgb, big_rgb = self.get_pixel()
        # print(small_rgb)
        for i in range(small.width):
            for j in range(small.height):
                if big_rgb[x + i, y + j] != small_rgb[i, j]:
                    return False
        return True

    def open(self):
        os.popen(r"C:\Users\Administrator.USER-20190305CL\AppData\Local\Google\Chrome\Application\chrome.exe http://localhost:8081/agileone/Agileone_1.2")

if __name__ == '__main__':
    match = ImageMatch()
    match.open()
    time.sleep(3)
    match.get_pixel()
    # match.get_pixel()