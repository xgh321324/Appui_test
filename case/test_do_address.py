# coding:utf-8
import time, unittest, re
from pages.set_page import SetPage
from appium import webdriver
from common.My_swipe import *

class Set(unittest.TestCase):
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
        cls.AddressPage = SetPage(cls.driver)

    def test_do_address01(self):
        u'新增收货地址'
        try:
            # 点击我的
            self.AddressPage.click_my_button()
            time.sleep(1)
            # 上滑显示出设置按钮
            swipe_up(self.driver)
            time.sleep(2)
            # 点击设置
            self.AddressPage.click_set()
            # 点击收货地址
            self.AddressPage.click_adress_btn()
            # 点击增加地址
            self.AddressPage.click_add_address()
            # 输入姓名，手机号
            self.AddressPage.send_keys(self.AddressPage.name_input, value='姓名姓名')
            self.AddressPage.send_keys(self.AddressPage.phone_input, value=13605246389)
            # 点击选择地区
            self.AddressPage.click_chose_area()
            # 选择城市
            self.AddressPage.chose_city()
            # 输入详细地址
            self.AddressPage.send_keys(self.AddressPage.address_input, value='江苏省南京市江宁区乾德路1号')
            # 点击保存
            self.AddressPage.click_save_btn()
            # 断言是否新增成功
            name = self.AddressPage.get_reciever_name()
            self.assertEqual(name, '姓名姓名', msg='新增收货人姓名不一致')
        except Exception as e:
            print('估计元素定位出错：%s' % e)
            raise

    def test_do_address02(self):
        u'修改收货人信息'
        try:
            # 点击修改
            self.AddressPage.click_update()
            # 输入新名字，号码
            self.AddressPage.send_keys(self.AddressPage.name_input, value='修改')
            self.AddressPage.send_keys(self.AddressPage.phone_input, value=13813891234)
            # 保存
            self.AddressPage.click_save_btn()
            # 断言
            name = self.AddressPage.get_reciever_name()
            self.assertEqual(name, '修改', msg='修改后收货人姓名不一致')
            phone_num = self.AddressPage.get_reciever_phone()
            number = phone_num.split('****')
            print(type(number))
            print(type(number[-1]))
            self.assertEqual(number[-1], '1234', msg='号码不相等')
        except Exception as e:
            print(e)
            raise

    def test_do_address03(self):
        u'删除一条收货人'
        try:
            # 点击修改按钮
            self.AddressPage.click_update()
            # 点击删除地址
            self.AddressPage.click_del_address()
            # 点击确定
            self.AddressPage.yes_or_no(choice='确定')
            # 断言是否删除成功
            name = self.AddressPage.get_reciever_name()
        except Exception as e:
            print(e)
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
