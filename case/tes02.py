#coding:utf-8
from appium import webdriver
import time

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
time.sleep(5)

ac = driver.current_activity
print(ac)
driver.wait_activity(ac,30)
'''
driver.find_element_by_id('com.baidu.yuedu:id/cb_choose_book').click()
time.sleep(1)
driver.find_element_by_id('	com.baidu.yuedu:id/cb_choose_view').click()
time.sleep(1)
driver.find_element_by_id('	com.baidu.yuedu:id/tv_confirm_button').click()
time.sleep(2)
ab = driver.current_activity
print(ab)
driver.wait_activity(ab,30)
driver.f

# 点击搜索
driver.find_element_by_id('com.baidu.yuedu:id/tv_search').click()
time.sleep(2)
# 输入python
driver.find_element_by_id('com.baidu.yuedu:id/full_text_search_bar_input').send_keys('python接口')
time.sleep(2)
# 点击搜索按钮
driver.find_element_by_id('com.baidu.yuedu:id/full_text_search_bar_search').click()
time.sleep(2)
# 点击搜索结果第一个
results = driver.find_elements_by_class_name('android.widget.Image')[0].click()
'''
'''
#用xpath获取text值
t = driver.find_element_by_xpath("//*[@text='免费图书']").text
print(t)
'''
# 获取text
a = driver.find_element_by_id('com.baidu.yuedu:id/iv_yuedu_classify').text
print(a)
# 获取tagname
b = driver.find_element_by_id('com.baidu.yuedu:id/iv_yuedu_classify').tag_name
print(b)
# content-desc为空，获取的是text
c = driver.find_element_by_id('com.baidu.yuedu:id/iv_yuedu_classify').get_attribute('name')
print(c)
# 获取id
d = driver.find_element_by_id('com.baidu.yuedu:id/iv_yuedu_classify').get_attribute('resourceId')  # 这里要注意
print(d)
# 获取class
e = driver.find_element_by_id('com.baidu.yuedu:id/iv_yuedu_classify').get_attribute('className')
print(e)
# 获取text
f = driver.find_element_by_id('com.baidu.yuedu:id/iv_yuedu_classify').get_attribute('text')
print(f)
# 获取chekable
g = driver.find_element_by_id('com.baidu.yuedu:id/iv_yuedu_classify').get_attribute('checkable')
print(g)
# 获取size
h = driver.find_element_by_id('com.baidu.yuedu:id/iv_yuedu_classify').size
print(h)
# 获取location
i = driver.find_element_by_id('com.baidu.yuedu:id/iv_yuedu_classify').location
print(i)



