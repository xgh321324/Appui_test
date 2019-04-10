# coding:utf-8
from appium import webdriver
import time,unittest
from pages.my_page import MyPage

class Living(unittest.TestCase):
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
        cls.mypage = MyPage(cls.driver)

    def test_living01(self):
        u'测试直播间关注/取消关注'
        try:
            # 进入我的
            self.mypage.click_my_button()
            # 点击直播间
            self.mypage.click_my_chat_room()
            # 点击关注按钮去取消关注
            self.mypage.click_attention_btn()
            now = self.driver.current_context
            self.driver.switch_to.context(now)
            # 确定
            self.mypage.click_yes_btn()
            # 断言取消关注后toast
            r = self.mypage.is_toast_exist(self.driver, text='取消关注成功')
            self.assertTrue(r)
            time.sleep(2)
            # 再次点击关注
            self.mypage.click_attention_btn()
            # 断言关注后toast
            r2 = self.mypage.is_toast_exist(self.driver, text='关注成功')
            self.assertTrue(r2)
        except Exception as e:
            print('关注直播间出错：%s' % e)
            raise

    def test_living02(self):
        u'直播间直播课列表'
        self.mypage.click_room_name()
        t = self.mypage.find_element(*self.mypage.room_title).get_attribute('text')
        print(t)
        self.assertEqual(t, '随心所欲直播间')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()



