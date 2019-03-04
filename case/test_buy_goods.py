# coding:utf-8
from appium import webdriver
import time
import unittest
from pages.find_page import Find


class Buy(unittest.TestCase):

    def setUp(self):
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
        self.driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(6)
        # 实例化
        self.find_page = Find(self.driver)

    def test_buy01(self):
        u'完整的购买商品流程'
        # 进入发现
        self.find_page.click_find_button()
        # 进入商城
        self.find_page.click_mall_button()
        # 立即购买第一个商品
        self.find_page.click_buy_now()
        # 选择规格
        self.find_page.click_goods_type()
        # 输入数量
        self.find_page.goods_num(3)
        # 购买
        self.find_page.click_buy_it()
        # 提交订单
        self.find_page.click_submit_order()
        time.sleep(5)
        # 去支付(微信)
        self.find_page.click_pay_button(pay_way='微信')

    def test_buy02(self):
        u'支付宝支付'
        # 进入发现
        self.find_page.click_find_button()
        # 进入商城
        self.find_page.click_mall_button()
        # 立即购买第一个商品
        self.find_page.click_buy_now()
        # 选择规格
        self.find_page.click_goods_type()
        # 输入数量
        self.find_page.goods_num(1)
        # 购买
        self.find_page.click_buy_it()
        # 提交订单
        self.find_page.click_submit_order()
        time.sleep(5)
        # 去支付(支付宝)
        self.find_page.click_pay_button(pay_way='支付宝')


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
