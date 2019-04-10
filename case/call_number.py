# coding:utf-8
from appium import webdriver
import time, os

def test_call_number():
    # number是个列表，直接在这里天上你想要骚扰的号码即可
    number = [10086, 10010, 12580]
    # 直接一个for循环，循环号码
    for num in number:
        # 使用adb打电话
        call = os.popen('adb shell am start -a android.intent.action.CALL -d tel:%s' % num)
        # 这里的sleep时间基本就是你想让通话保持的时间了
        time.sleep(15)
        #挂断电话
        end = os.popen('adb shell input keyevent 6') # code6是挂断
        time.sleep(4)

if __name__ == '__main__':
    test_call_number()