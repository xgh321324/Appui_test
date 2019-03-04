# coding:utf-8
from appium import webdriver
import time,unittest
from pages.classroom_page import Classroom

class Live(unittest.TestCase):
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

    def test_live01(self):
        u'进入直播开始评论'
        try:
            # 进入极致课堂
            self.classroom_page.click_best_classroom()
            # 点击直播
            self.classroom_page.click_live()
            # 点击直播中
            self.classroom_page.click_living_btn()
            # 点击最后一个直播（）
            self.classroom_page.click_secondlive()
            # 点击进入课堂
            self.classroom_page.click_enter_live()
            # 点击查看评论
            self.classroom_page.click_check_comment()
            # 输入评论
            self.classroom_page.input_comment('我的评论不知道说什么')
            # 发送评论
            self.classroom_page.click_send_comment()
            time.sleep(4)
            # 获取评论内容
            comment_text = self.classroom_page.get_comment_text()
            # 断言评论
            self.assertEqual('我的评论不知道说什么', comment_text)
        except Exception as e:
            print('评论过程出错：%s' % e)
            raise

    def test_live02(self):
        u'评论后删除评论'
        try:
            # 操作评论
            self.classroom_page.click_do_comment()
            # 点击删除评论-确认
            self.classroom_page.click_del_comment()
            # 断言toast
            result = self.classroom_page.is_toast_exist(self.driver, text='删除成功')
            self.assertTrue(result, msg='删除成功的断言失败！')
        except Exception as e:
            print('删除评论用例出错')
            raise


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()




