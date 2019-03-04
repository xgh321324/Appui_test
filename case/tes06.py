#coding:utf-8
from appium import webdriver
import os,time
from appium.webdriver.common.touch_action import TouchAction

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
                }

driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

# 定位聊天记录列表，选择第一个长安
el = driver.find_elements_by_id('com.tencent.mm:id/azj')[0]

# 使用Touchaction类
TouchAction(driver).long_press(el).perform()
time.sleep(2)

# 定位选项框删除该聊天
driver.find_element_by_xpath('//*[@text="删除该聊天"]').click()
time.sleep(2)

# 定位选项框 取消
driver.find_element_by_id('com.tencent.mm:id/au_').click()
time.sleep(2)



