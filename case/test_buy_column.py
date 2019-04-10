# coding:utf-8
from appium import webdriver
import time,unittest
from pages.classroom_page import Classroom

class BuyColumn(unittest.TestCase):
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
        u'进入专栏'
        self.classroom_page.click_best_classroom()
        self.classroom_page.click_column()
        nums = self.classroom_page.find_elements("xpath", '//*[@resource-id="com.mld.LanTin:id/single_iv"]')
        print(nums)
        try:
            self.assertEqual(4, len(nums))
        except Exception as e:
            print('专栏条目不是4')
            raise


    def test_buy02(self):
        u'购买专栏'
        try:
            # 进入产后更美专栏
            self.classroom_page.click_last_column()
            # 点击购买专栏
            self.classroom_page.click_buy_column()
            # 点击提交订单
            self.classroom_page.click_submit_column_btn()
            # 点击去支付（支付宝）
            self.classroom_page.click_pay_button(pay_way='支付宝')
        except Exception as e:
            print('购买专栏过程出错！')
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()







