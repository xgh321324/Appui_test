# coding:utf-8
from appium import webdriver
import time, unittest, os
from pages.my_page import MyPage
from pages.friend_page import Friend
from common.My_swipe import swipe_up

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
        cls.mypage = MyPage(cls.driver)
        cls.friendpage = Friend(cls.driver)

    def test_feedback01(self):
        u'标题为空'
        try:
            # 进入我的
            self.mypage.click_my_button()
            time.sleep(3)
            # 上滑
            swipe_up(self.driver)
            time.sleep(1)
            # 点击意见反馈
            self.mypage.click_feedback()

            # 输入反馈内容
            self.mypage.send_keys(loc=self.mypage.feedback_content, value='反馈内容内容！')
            # 点击提交反馈
            self.mypage.click_submit_feedback_btn()
            try:
                # 断言toast
                r = self.mypage.is_toast_exist(self.driver, text='澜渟：请输入标题')
                self.assertTrue(r)
            except Exception as e:
                print('断言出错', e)
        except Exception as e:
            print('意见反馈标题为空出错')
            raise

    def test_feedback02(self):
        u'标题和内容'
        try:
            # 输入标题
            self.mypage.send_keys(loc=self.mypage.feedback_title, value='反馈意见标题')
            # 点击提交反馈
            self.mypage.click_submit_feedback_btn()
            try:
                # 断言toast
                r = self.mypage.is_toast_exist(self.driver, text='澜渟：提交成功')
                self.assertTrue(r)
            except Exception as e:
                print('断言出错', e)
        except Exception as e:
            print('意见反馈 标题和内容出错')
            raise


    def test_feedback03(self):
        u'标题+内容+图片'
        try:
            # 上滑
            swipe_up(self.driver)
            # 点击意见反馈
            self.mypage.click_feedback()
            # 输入反馈内容
            self.mypage.send_keys(loc=self.mypage.feedback_content, value='反馈内容内容！')
            # 输入标题
            self.mypage.send_keys(loc=self.mypage.feedback_title, value='反馈意见标题')
            # 添加图片
            self.mypage.click_add_pic()
            # 调用friendpage的选择照片方法
            self.friendpage.chose_picture(pic_num=1)
            # 点击提交反馈
            self.mypage.click_submit_feedback_btn()
            try:
                # 断言toast
                r = self.mypage.is_toast_exist(self.driver, text='提交成功')
                self.assertTrue(r)
            except Exception as e:
                print('断言出错', e)
                raise
        except Exception as e:
            print('标题+内容+图片出错')
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
