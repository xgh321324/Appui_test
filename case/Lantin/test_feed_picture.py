# coding:utf-8
from appium import webdriver
import time
import unittest
from pages.friend_page import Friend


class Post_pic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'android',
            'deviceName': '740dc3d1',
            'platformVersion': '8.0.0',
            'appPackage': 'com.mld.LanTin',
            'appActivity': 'com.mld.LanTin.main.activity.SplashActivity',
            'automationName': 'Uiautomator2', # 想定位toast元素，这里一定要注意automationName的参数必须是Uiautomator2才能定位到
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True
        }
        # 配置
        cls.driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(6)
        # 实例化
        cls.friend_page = Friend(cls.driver)

    def test_post_pic01(self):
        u'发布图片渟说'
        # 进入朋友圈
        self.friend_page.click_friend()
        # 点击发布渟说
        self.friend_page.click_feed()
        # 选择发布图片
        self.friend_page.click_pic()
        # 选择第一张图片-确定
        self.friend_page.chose_picture()
        # 输入文字内容
        self.friend_page.input_text('大家一起扫五福啦！')
        # 点击发送
        self.friend_page.click_send()
        # 验证发布成功
        # 判断存在发布成功的toast则说明发布成功
        to = self.friend_page.is_toast_exist(self.driver, '发布成功')
        # 断言
        self.assertTrue(to)

    def test_post_pic02(self):
        u'发布多张图片渟说'
        # 进入朋友圈
        self.friend_page.click_friend()
        # 点击发布渟说
        self.friend_page.click_feed()
        # 选择发布图片
        self.friend_page.click_pic()
        # 选择第一张图片-确定
        self.friend_page.chose_picture(pic_num=3)
        # 输入文字内容
        self.friend_page.input_text('大家一起扫五福啦！')
        # 点击发送
        self.friend_page.click_send()
        # 验证发布成功
        # 判断存在发布成功的toast则说明发布成功
        to = self.friend_page.is_toast_exist(self.driver, '发布成功')
        # 断言
        self.assertTrue(to)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()
