# coding:utf-8
from appium import webdriver
import time
import unittest


desired_caps = {
    "platformName": "android",
    "deviceName": "GB8ZA1QBH3",
    "platformVersion": "5.1.1",
    "appPackage": "com.medlander.b40tablet",
    "appActivity": "com.medlander.b40tablet.activity.LoadingActivity",
    "noReset": True,
    'resetKeyboard': True,
}
# 启动app
driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
# 点击筛查
driver.find_element_by_id('com.medlander.b40tablet:id/iv_standard_screening').click()
time.sleep(2)
# 选择第一个病员开始筛查
driver.find_element_by_xpath('//*[@text="测试"]').click()
# 断言页面

