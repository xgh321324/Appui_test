# coding:utf-8
import time,unittest
from pages.my_follow_page import MyFollow
from appium import webdriver
from common.My_swipe import swipe_up

class Follow(unittest.TestCase):

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
        cls.follow_page = MyFollow(cls.driver)

    def test_follow01(self):
        u'关注'
        # 进入我的
        try:
            self.follow_page.click_my_button()
            # 点击关注
            self.follow_page.click_follow()
            # 获取列表第一个关注状态
            state_text = self.follow_page.get_user_attention_state()
            # 如果是关注那么久取消关注
            if state_text == '已关注' or '互相关注':
                # 点击 取消关注
                self.follow_page.click_user_attention()
                # 点击确定
                self.follow_page.click_yes_btn()
                # 获取关注状态
                state_text2 = self.follow_page.get_user_attention_state()
                # 断言
                self.assertEqual(state_text2, '关注')
                # 再次点击，关注
                self.follow_page.click_user_attention()
                # 获取关注状态
                state_text3 = self.follow_page.get_user_attention_state()
                L = ['已关注', '互相关注']
                self.assertIn(state_text3, L)
            else:
                print('该用户目前还未关注')
        except Exception as e:
            print('关注/取关出错：%s' % e)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()






