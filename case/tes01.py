#coding:utf-8
from appium import webdriver
import time
from selenium.webdriver.common.by import By

desired_caps = {
    'platformName': 'android',
    'deviceName': '740dc3d1',
    'platformVersion': '8.0.0',
    'appPackage': 'com.mld.LanTin',
    'appActivity': 'com.mld.LanTin.main.activity.SplashActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True
}
driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)


time.sleep(5)
#点击朋友圈
loc = (By.ID,"com.mld.LanTin:id/iv_main_home_02")
driver.find_element(*loc).click()
driver.long_press_keycode()
time.sleep(4)

#查看页面环境
print(driver.contexts)
#driver.switch_to.context()
'''
for i in range(3):
    #点击发布
    driver.find_element_by_id("com.mld.LanTin:id/iv_issue_feed").click()
    time.sleep(2)
    #点击文字
    driver.find_element_by_name('文字').click()
    time.sleep(2)
    #输入内容
    driver.find_element_by_id("com.mld.LanTin:id/et_editor").send_keys('今天是圣诞节，祝大家圣诞节快乐！')
    time.sleep(2)
    #发布
    driver.find_element_by_id("com.mld.LanTin:id/tv_publish").click()
    time.sleep(2)
'''
driver.quit()




