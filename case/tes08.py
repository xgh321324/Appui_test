# coding:utf-8
from appium import webdriver
import time,os
from common.My_swipe import swipe_down

'''
这章主要讲解几种xpath的用法，xpath是最牛逼的
'''

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '8.0',
                'deviceName': '740dc3d1',
                'appPackage': 'com.taobao.taobao',
                'appActivity': 'com.taobao.tao.welcome.Welcome',
                'automationName': 'Uiautomator2',
                # 'unicodeKeyboard': True,
                # 'resetKeyboard': True,
                'noReset': True,
                #'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
                }
driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
# 定位左上角扫一扫
# driver.find_element_by_xpath('//*[@text="扫一扫"]').click()
# time.sleep(3)\

# 如果元素id是唯一的，xpath也可以定位id属性
# driver.find_element_by_xpath('//*[@resource-id="com.taobao.taobao:id/tv_scan_text"]').click()
# time.sleep(3)

# 定位搜索框,xpath定位class属性
driver.find_element_by_xpath('//*[@class="android.widget.EditText"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@resource-id="com.taobao.taobao:id/searchEdit"]').send_keys('行车记录仪')
driver.find_element_by_xpath('//*[@resource-id="com.taobao.taobao:id/searchbtn"]').click()
time.sleep(2)

# contains模糊定位
# driver.find_element_by_xpath('//*[contains(@resource-id,"home_searchedit")]').click()
# time.sleep(2)
# driver.back()

# 若一个元素只有class属性 可用父亲定位儿子  搜索输入框,定位拍立淘
#loc = '//*[@resource-id="com.taobao.taobao:id/home_searchbar"]/android.widget.TextView'
#driver.find_elements_by_xpath(loc)[1].click()
#time.sleep(2)

# 如果一个父元素下，有多个相同class的儿子时候，可以通过xpath的索引去取对应第几个
# 取第二个
#loc = '//*[@resource-id="com.taobao.taobao:id/ll_navigation_tab_layout"]/android.widget.FrameLayout[2]'
#driver.find_element_by_xpath(loc).click()
#time.sleep(2)

# 儿子定位父亲
# 通过子元素定位父元素
# loc = '//*[@resource-id="com.taobao.taobao:id/tv_scan_text"]/..'
# x = driver.find_element_by_xpath(loc).tag_name
# print(x)


