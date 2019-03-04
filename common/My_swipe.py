#coding:utf-8
from appium import webdriver
import time

# 向上滑动
def swipe_up(driver,t=500,n= 1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.75  # 起点y坐标
    y2 = s['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

# 向下滑动
def swipe_down(driver,t=500,n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.25  # 起点y坐标
    y2 = s['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

# 向左滑动
def swipe_left(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.75
    y1 = s['height'] * 0.5
    x2 = s['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

# 向右
def swipe_right(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

if __name__=='__main__':
    '''
    desired_caps = {
        'platformName': 'android',
        'deviceName': '740dc3d1',
        'platformVersion': '8.0.0',
        'appPackage': 'com.mld.LanTin',
        'appActivity': 'com.mld.LanTin.main.activity.SplashActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    '''
    desired_caps = {
                'platformName': 'Android',
                'platformVersion': '8.0',
                'deviceName': '740dc3d1',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                # 'unicodeKeyboard': True,
                # 'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
                }
    driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)

    time.sleep(3)
    swipe_up(driver)








