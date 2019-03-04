# coding:utf-8
import time,unittest
from pages.personal_info_page import Personal
from appium import webdriver
from common.Key_event import back

class Info(unittest.TestCase):

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
        cls.personal_page = Personal(cls.driver)

    def test_edit_info01(self):
        u'编辑昵称'
        try:
            # 进入我的
            self.personal_page.click_my_button()
            # 进入个人信息
            self.personal_page.click_personal_btn()
            # 点击昵称栏
            self.personal_page.click_nick_name()
            # 输入昵称
            self.personal_page.send_keys(self.personal_page.nick_name_input, value='这是我新改的昵称')
            # 点击提交
            self.personal_page.click_finish()
            # 点击返回
            self.driver.keyevent(keycode=4)  # keycode4是返回按键
            # 获取主页昵称，断言是否成功
            name = self.personal_page.find_element(*self.personal_page.real_nick_name).get_attribute('text')
            print(name)
            self.assertEqual(name, '这是我新改的昵称')
        except Exception as e:
            print('修改昵称出错：%s' % e)
            raise

    def test_edit_info02(self):
        u'编辑昵称'
        try:
            # 进入我的
            self.personal_page.click_my_button()
            # 进入个人信息
            self.personal_page.click_personal_btn()
            # 点击地区栏
            self.personal_page.click_address()
            # 选择省市
            self.personal_page.chose_city()
            r = self.personal_page.is_toast_exist(self.driver, text='澜渟：修改地区成功')
            self.assertTrue(r)
        except Exception as e:
            print('修改地区出错：%s' % e)
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()





