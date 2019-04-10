#coding:utf-8
from appium import webdriver
import time
'''
这篇介绍安卓的uiautomator定位
用法：new UiSelector（）
'''
desired_caps = {
    'platformName': 'android',
    'deviceName': '740dc3d1',
    'platformVersion': '8.0.0',
    'appPackage': 'com.baidu.yuedu',
    'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True
}

driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
#等待主页activity
driver.wait_activity('.base.ui.MainActivity',30)


#通过text定位
loc = 'new UiSelector().text("图书")'
driver.find_element_by_android_uiautomator(loc).click()

#textContains()
#loc1 = 'new UiSelector().textContains("图")'
#driver.find_element_by_android_uiautomator(loc1).click()
#textStartWith
#loc2 = 'new UiSelector().textStartsWith("图")'
#driver.find_element_by_android_uiautomator(loc2).click()


#id
time.sleep(1)
loc_id = 'new UiSelector().resourceId("com.baidu.yuedu:id/iv_yuedu_classify")'
driver.find_element_by_android_uiautomator(loc_id).click()

#className
time.sleep(1)
loc_class = 'new UiSelector().className("android.widget.Image")'
L= driver.find_elements_by_android_uiautomator(loc_class)  #注意：elements
print(L)
driver.find_elements_by_android_uiautomator(loc_class)[1].click()



