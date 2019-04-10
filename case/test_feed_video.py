# coding:utf-8
from appium import webdriver
import time
import unittest
from pages.friend_page import Friend


class Post_video(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'android',
            'deviceName': '740dc3d1',
            'platformVersion': '8.0.0',
            'appPackage': 'com.mld.LanTin',
            'appActivity': 'com.mld.LanTin.main.activity.SplashActivity',
            'automationName': 'Uiautomator2', # 想定位toast元素这里一定要注意automationName的参数必须是Uiautomator2才能定位到
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True
        }
        # 配置
        cls.driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(6)
        # 实例化
        cls.friend_page = Friend(cls.driver)

    def test_post_video01(self):
        u'发布视频+摘要渟说'
        # 进入盆友圈
        self.friend_page.click_friend()
        # 点击发布渟说按钮
        self.friend_page.click_feed()
        # 选择发布视频
        self.friend_page.click_video()
        # 点击开始录制
        self.friend_page.click_record_start()
        time.sleep(6)
        # 点击停止录制
        self.friend_page.click_record_end()
        # 点击完成录制
        self.friend_page.click_record_complete()
        # 输入视频描述
        self.friend_page.input_text('这是我拍的视频，虽然很渣，但是很用心！')
        # 发布此停说
        self.friend_page.click_send()
        # 断言是否发布成功
        try:
            result = self.friend_page.is_toast_exist(self.driver,text='发布成功')
            self.assertTrue(result)
        except Exception as e:
            print(e)
            raise

    def test_post_video02(self):
        u'发布视频无摘要渟说'
        # 进入盆友圈
        self.friend_page.click_friend()
        # 点击发布渟说按钮
        self.friend_page.click_feed()
        # 选择发布视频
        self.friend_page.click_video()
        # 点击开始录制
        self.friend_page.click_record_start()
        time.sleep(6)
        # 点击停止录制
        self.friend_page.click_record_end()
        # 点击完成录制
        self.friend_page.click_record_complete()
        # 录制完成直接发布此停说
        self.friend_page.click_send()
        # 断言是否发布成功
        try:
            result = self.friend_page.is_toast_exist(self.driver,text='发布成功')
            self.assertTrue(result)
        except Exception as e:
            print(e)
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main___':
    unittest.main()


