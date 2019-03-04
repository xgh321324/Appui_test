# coding:utf-8
from appium import webdriver
import time
import unittest
from pages.friend_page import Friend
from pages.my_page import MyPage



class Post_text(unittest.TestCase):

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
        cls.my_page = MyPage(cls.driver)

    def test_post_text01(self):
        u'发布文字渟说'
        # 进入朋友圈
        self.friend_page.click_friend()
        # 点击发布渟说
        self.friend_page.click_feed()
        # 选择发布文字
        self.friend_page.click_text()
        # 输入文字内容
        self.friend_page.input_text('!!!!!!')
        # 点击发送
        self.friend_page.click_send()
        # 验证发布成功
        # 判断存在发布成功的toast则说明发布成功
        to = self.friend_page.is_toast_exist(self.driver, '发布成功')
        # 断言
        self.assertTrue(to)

    def test_post_text02(self):
        u'发布空内容渟说'
        # 进入朋友圈
        self.friend_page.click_friend()
        # 点击发布渟说
        self.friend_page.click_feed()
        # 选择发布文字
        self.friend_page.click_text()
        # 输入文字内容(内容为空)
        self.friend_page.input_text('')
        # 点击发送
        self.friend_page.click_send()
        # 验证发布失败
        # 判断提示是否准确
        to = self.friend_page.is_toast_exist(self.driver, '内容不能为空')
        # 断言
        self.assertTrue(to)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
