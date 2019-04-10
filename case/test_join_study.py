# coding:utf-8
import time, unittest, re
from pages.study_center_page import Study
from appium import webdriver
from common.My_swipe import swipe_down

class My_Study(unittest.TestCase):
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
        cls.study_page = Study(cls.driver)

    def test_study01(self):
        u'测试加入学习'
        try:
            # 进入我的
            self.study_page.click_my_button()
            # 进入学习中心
            self.study_page.click_study_center()
            swipe_down(self.driver)
            # 判断学习列表
            r =self.study_page.is_element_exist()
            # r若为true则列表为空
            if r:
                # 点击已购课程
                self.study_page.click_buyed_lesson()
                # 点击目标专栏
                self.study_page.click_target_column()
                # 点击加入学习
                self.study_page.click_join_study()
                # 获取状态
                t = self.study_page.find_element(*self.study_page.join_study).get_attribute('text')
                # 断言状态已改变
                self.assertTrue(t, '已加入学习')
                # 返回
                self.driver.keyevent(keycode=4)
                # 返回
                self.driver.keyevent(keycode=4)
                swipe_down(self.driver)
                # 断言学习列表页
                r2 =self.study_page.is_element_exist()
                self.assertFalse(r2)
            else:
                print('学习列表不为空')
                pass
        except Exception as e:
            print(e)
            raise


    def test_study02(self):
        u'取消加入学习'
        try:

            # 滑动取消加入学习
            self.driver.swipe(start_x=900, start_y=500, end_x=500, end_y=500, duration=500)
            # 点击取消加入学习
            self.study_page.click_cancle_study()
            # 点击确定
            self.study_page.yes_or_no(choice="确定")
            # 下滑刷新
            swipe_down(self.driver)
            # 断言
            t = self.study_page.is_element_exist()
            self.assertTrue(t)
        except Exception as e:
            print(e)
            raise


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

