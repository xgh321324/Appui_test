#coding:utf-8
from appium import webdriver
import time,os
import uiautomator2 as u2
d = u2.connect_wifi('192.168.31.1')
#from common.My_swipe import swipe_down


desired_caps = {
                'platformName': 'Android',
                'platformVersion': '8.0',
                'deviceName': '740dc3d1',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
                 'newCommandTimeout': '150000'
                }
driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
# 向下滑动
s = driver.get_window_size()
driver.swipe(s['width']*0.5, s['height']*0.32, s['width']*0.5, s['height']*0.99,duration=1000)
time.sleep(4)

# 点击小小签到
driver.find_element_by_id('com.tencent.mm:id/yv').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@text="去签到"]').click()
time.sleep(3)
#loc = 'new UiSelector().text("点击签到")'
driver.find_element_by_xpath('//*[@class="android.webkit.WebView"]/	android.widget.Button[9]').click()
time.sleep(3)
#driver.find_element_by_xpath('//*[@class="android.webkit.WebView"]/ android.view.View[1]').clear()
driver.find_element_by_xpath('//*[@class="android.webkit.WebView"]/ android.view.View[1]').click()
time.sleep(3)

#js = 'document.getElementByXpath("//*[@class="android.webkit.WebView"]/ android.view.View[1]").removeAttribute("clickable")'
# driver.execute_async_script(js)
# 换行
driver.press_keycode(66)
# HELLO
driver.press_keycode(36)
driver.press_keycode(33)
driver.press_keycode(40)
driver.press_keycode(40)
driver.press_keycode(43)

time.sleep(2)
driver.find_element_by_xpath('//*[@text="完成"]').click()
#driver.press_keycode(23)
driver.find_element_by_xpath('//*[contains(@text,"确定")]').click()





