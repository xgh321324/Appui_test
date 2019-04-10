#coding:utf-8
from appium import webdriver
import time
import os

#执行第一个adb command
adb1 = 'adb shell input tap 150 1350'  # 这里的坐标根据你的桌面app布局，我的是百度阅读
os.system(adb1)

time.sleep(5)
#执行第二个adb comman
adb2 = 'adb shell input tap 980 1810'  # 进入”我的“页面
os.system(adb2)

