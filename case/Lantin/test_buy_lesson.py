# coding:utf-8
from appium import webdriver
import time,unittest
from pages.classroom_page import Classroom

class BuyLesson(unittest.TestCase):
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
        cls.classroom_page = Classroom(cls.driver)

    def test_buy01(self):
        u'未购买直接播放'
        try:
            # 点击极致课堂
            self.classroom_page.click_best_classroom()
            # 点击课程
            self.classroom_page.click_lesson_button()
            # 点击某个课
            self.classroom_page.click_lesson_name()
            # 点击章节
            self.classroom_page.click_chapter_btn()
            # 点击播放（此章节未购买）
            self.classroom_page.click_first_chap()
            try:
                # 断言toast
                result = self.classroom_page.is_toast_exist(self.driver, '请先购买课程')
                self.assertTrue(result)
            except Exception as e:
                print('断言toast失败：%s' % e)
        except Exception as e:
            print('找元素有问题：%s' % e)
            raise

    def test_buy02(self):
        u'去购买课程'
        time.sleep(4)
        try:
            # 点击购买课程
            self.classroom_page.click_buy_lesson()
            # 点击提交订单
            self.classroom_page.click_submit_lesson_btn()
            # 点击去支付
            self.classroom_page.click_pay_button(pay_way='微信')
        except Exception as e:
            print(e)
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
