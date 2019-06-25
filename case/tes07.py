#coding:utf-8
from appium import webdriver
import time,os
#from common.My_swipe import swipe_down


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
# 向下滑动
s = driver.get_window_size()
driver.swipe(s['width']*0.5, s['height']*0.32, s['width']*0.5, s['height']*0.99,duration=1000)
time.sleep(3)

# 点击膜拜单车
driver.find_element_by_id('com.tencent.mm:id/jb').click()
time.sleep(8)
print(driver.contexts)

# tap触摸右下角那个人头坐标
driver.tap([(972, 1613), (1034, 1622)], 1000)  #tap的点必须是tuple类型,一个点是一个tuple
time.sleep(5)
print('进入我的页面')
# 点击我的钱包
driver.find_element_by_xpath('//*[@text="我的钱包"]').click()
time.sleep(4)
print('进入钱包')
# 点击余额
driver.find_element_by_xpath('//*[@text="余额"]').click()
time.sleep(4)

# 点击充值
driver.find_element_by_xpath('//*[@text="充值"]').click()
time.sleep(2)

time.sleep(2)
#接下来就是摩拜的充值页面了，由于我太穷充不起，所以就介绍到这里





