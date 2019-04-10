# coding:utf-8
import time,unittest
from pages.my_feed_page import MyFeed
from appium import webdriver
from common.My_swipe import swipe_up

class DOFeed(unittest.TestCase):

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
        cls.myfeed = MyFeed(cls.driver)

    def test_do_feed01(self):
        u'收藏渟说'
        try:
            # 进入我的
            self.myfeed.click_my_button()
            # 进入渟说
            self.myfeed.click_feed()
            # 点击收藏按钮
            self.myfeed.click_collect_btn()
            # 断言toast
            t = self.myfeed.is_toast_exist(self.driver, text='澜渟：已收藏')
            self.assertTrue(t)
        except Exception as e:
            print('收藏渟说出错：%s' % e)
            raise

    def test_do_feed02(self):
        u'取消收藏渟说'
        try:
            # 点击收藏按钮
            self.myfeed.click_collect_btn()
            # 点击确定取消收藏
            self.myfeed.click_yes_btn()
            # 断言toast
            t = self.myfeed.is_toast_exist(self.driver, text='澜渟：取消收藏成功')
            self.assertTrue(t)
        except Exception as e:
            print('取消收藏渟说出错：%s' % e)
            raise

    def test_do_feed03(self):
        u'点赞渟说'
        try:
            # 获取点赞数量
            n = self.myfeed.find_element(*self.myfeed.like_num).get_attribute('text')
            print('n：', n)
            # 点赞
            self.myfeed.click_like_btn()
            time.sleep(2)
            # 获取点赞后点赞数量
            n2 = self.myfeed.find_element(*self.myfeed.like_num).get_attribute('text')
            print('n2:', n2)
            self.assertEqual(int(n2), int(n)+1)
        except Exception as e:
            print('点赞出错：%s' % e)
            raise

    def test_do_feed04(self):
        u'取消点赞渟说'
        try:
            # 获取当前点赞数量
            n3 = self.myfeed.find_element(*self.myfeed.like_num).get_attribute('text')
            print('n3:', n3)
            # 取消点赞
            self.myfeed.click_like_btn()
            # 获取当前点赞数量
            n4 = self.myfeed.find_element(*self.myfeed.like_num).get_attribute('text')
            print('n4:', n4)
            self.assertEqual(int(n4), int(n3)-1)
        except Exception as e:
            print('取消点赞出错：%s' % e)
            raise

    def test_do_feed05(self):
        u'评论渟说'
        try:
            # 点击进入渟说详情
            self.myfeed.click_feed_info()

            # 获取评论数量
            #num = self.myfeed.get_comment_num()
            #print('num:', num)
            # 点击评论按钮
            self.myfeed.click_comment_btn()
            # 输入评论
            self.myfeed.send_keys(loc= self.myfeed.input_comment, value='这是我发表的评论')
            # 发送
            self.myfeed.click_send_comment()
            #num2 = self.myfeed.get_comment_num()
            #print('num2:', num2)
            #self.assertEqual(int(num)+1, int(num2))
        except Exception as e:
            print('发表评论出错：%s' % e)
            raise


    def test_do_feed06(self):
        u'回复评论'
        try:
            # 点击回复按钮
            self.myfeed.click_reply_comment()
            # 输入回复内容
            self.myfeed.send_keys(loc = self.myfeed.input_comment, value='回复评论回复评论')
            # 点击发送
            self.myfeed.click_send_comment()
            # 断言是否回复成功
            t = self.myfeed.is_toast_exist(self.driver, text='澜渟')
            self.assertTrue(t)
        except Exception as e:
            print('回复评论出错：%s' % e)
            raise


    def test_do_feed07(self):
        u'删除评论'
        try:
            # 获取评论数量
            #r = self.myfeed.get_comment_num()
            # 上滑显示删除按钮
            swipe_up(self.driver)
            # 点击删除
            self.myfeed.click_del_comment_btn()
            # 点击确定
            self.myfeed.click_yes_btn()
            # 获取品论数量
            #r2 = self.myfeed.get_comment_num()
            #self.assertEqual(int(r)-1, int(r2))
        except Exception as e:
            print('删除评论不成功：%s' % e )
            raise

    def test_do_feed08(self):
        u'删除渟说'
        try:
            # 返回
            self.driver.keyevent(keycode=4)
            # 点击删除渟说按钮
            self.myfeed.click_del_feed_btn()
            # 点击确定
            self.myfeed.click_yes_btn()
            # 断言toast
            t = self.myfeed.is_toast_exist(self.driver, text='删除成功')
            self.assertTrue(t)
        except Exception as e:
            print('删除渟说出错：%s' % e)
            raise



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()



