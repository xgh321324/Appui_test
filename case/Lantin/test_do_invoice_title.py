# coding:utf-8
import time, unittest, re, random
from pages.set_page import SetPage
from appium import webdriver
from common.My_swipe import *
import warnings

class Set(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)  # 用于过滤掉warning
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
        cls.InvoicePage = SetPage(cls.driver)

    def test_do_invoice01(self):
        u'新增个人发票抬头'
        try:
            # 点击我的
            self.InvoicePage.click_my_button()
            time.sleep(2)
            # 上滑
            swipe_up(self.driver)
            time.sleep(1)
            # 点击设置
            self.InvoicePage.click_set()
            # 点击发票抬头
            self.InvoicePage.click_invoice_title()
            # 新增抬头
            self.InvoicePage.click_add_title()
            # 新增个人抬头
            self.InvoicePage.click_add_person_title()
            # 输入抬头名称
            self.InvoicePage.send_keys(self.InvoicePage.title_name, value='许广会的发票'+ str(random.randint(0, 99)))
            # 保存
            self.InvoicePage.click_save_title()
            # 断言toast
            t = self.InvoicePage.is_toast_exist(self.driver, text='保存成功')
            self.assertTrue(t,msg='toast不是保存成功')
        except Exception as e:
            print(e)
            raise

    def test_do_invoice02(self):
        u'新增单位发票抬头'
        try:
            # 新增抬头
            self.InvoicePage.click_add_title()
            # 新增单位抬头
            self.InvoicePage.click_add_co_title()
            # 输入抬头名称
            self.InvoicePage.send_keys(self.InvoicePage.title_name, value='麦澜德公司发票'+ str(random.randint(0, 99)))
            # 输入识别号
            self.InvoicePage.send_keys(self.InvoicePage.title_number, value= 'NJ20180017')
            # 保存
            self.InvoicePage.click_save_title()
            # 断言toast
            t = self.InvoicePage.is_toast_exist(self.driver, text='保存成功')
            self.assertTrue(t,msg='toast不是保存成功')
        except Exception as e:
            print('新增单位发票出错:%s' % e)
            raise

    def test_do_invoice03(self):
        u'设置默认'
        try:
            # 设置第一个为默认
            self.InvoicePage.click_default_btn()
            # 断言toast
            r = self.InvoicePage.is_toast_exist(self.driver, text='设置默认发票抬头成功')
            self.assertTrue(r, msg='toast断言错误了')
        except Exception as e:
            print(e)
            raise

    def test_do_invoice04(self):
        u'删除第一个抬头'
        try:
            # 获取当前抬头数目
            num = self.InvoicePage.get_title_num()
            # 得到第一条的坐标信息
            location = self.InvoicePage.get_location()
            # 向左滑动显示出删除按钮
            # 用ele.rec来获取该元素坐标，然后用swipe方法左滑
            self.driver.swipe(location['width']*0.8, (location['y'] + location['height']/2), location['width']*0.4, (location['y'] + location['height']/2))
            # 点击删除
            self.InvoicePage.click_del_title()
            # 点击确定
            self.InvoicePage.yes_or_no(choice='确定')
            # 再次获取当前抬头数目
            num2 = self.InvoicePage.get_title_num()
            # 断言数目差来判断是否删除成功
            self.assertEqual(num-1, num2, msg='抬头数量没有减少')
        except Exception as e:
            print(e)
            raise


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()