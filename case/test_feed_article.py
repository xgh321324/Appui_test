# coding:utf-8
from appium import webdriver
import time
import unittest
from pages.friend_page import Friend


class Post_article(unittest.TestCase):

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
        cls.friend_page = Friend(cls.driver)

    def test_post_article01(self):
        u'测试发布完整文章'
        # 进入盆友圈
        self.friend_page.click_friend()
        # 点击发布渟说按钮
        self.friend_page.click_feed()
        # 选择发布文章
        self.friend_page.click_article()
        # 添加封面
        self.friend_page.click_add_cover()
        # 添加默认封面
        self.friend_page.click_default_cover()
        # 选择默认的照片
        self.friend_page.chose_default_cover()
        # 输入标题
        self.friend_page.send_keys(self.friend_page.article_title, '这里是文章标题标题标题！' )
        # 点击添加文本
        self.friend_page.click_add_text()
        # 输入文本内容
        self.friend_page.send_keys(self.friend_page.text_input, '这里是文章的内容啊，我不知道写点什么内容比较好！')
        # 点击添加图片按钮
        self.friend_page.click_add_pic()
        # 选择照片（默认第一张）
        self.friend_page.chose_picture()
        # 确认完成编辑
        self.friend_page.click_done_article()
        # 确定
        self.friend_page.click_article_config_done()
        # 输入摘要
        self.friend_page.input_text('摘要我就不写了吧！直接发布！')
        # 发布渟说
        self.friend_page.click_send()
        # 断言是否发布成功
        try:
            result = self.friend_page.is_toast_exist(self.driver,text='发布成功')
            self.assertTrue(result)
        except Exception as e:
            print(e)
            raise

    def test_post_article02(self):
        u'测试标题<6字'
        # 进入盆友圈
        self.friend_page.click_friend()
        # 点击发布渟说按钮
        self.friend_page.click_feed()
        # 选择发布文章
        self.friend_page.click_article()
        # 添加封面
        self.friend_page.click_add_cover()
        # 添加默认封面
        self.friend_page.click_default_cover()
        # 选择默认的照片
        self.friend_page.chose_default_cover()
        # 输入标题
        self.friend_page.send_keys(self.friend_page.article_title, '两个字' )
        # 确认完成编辑
        self.friend_page.click_done_article()
        # 断言标题字数过少提示语
        try:
            result = self.friend_page.is_toast_exist(self.driver,text='文章标题为6-32个字')
            self.assertTrue(result)
        except Exception as e:
            print(e)
            raise
        finally:
            # 最终都会重输标题发布成功，保证其他用例正确执行
            self.friend_page.send_keys(self.friend_page.article_title, '现在补全标题！！！' )
            # 点击添加文本
            self.friend_page.click_add_text()
            # 输入文本内容
            self.friend_page.send_keys(self.friend_page.text_input, '这里是文章的内容啊，我不知道写点什么内容比较好！')
            # 确认完成编辑
            self.friend_page.click_done_article()
            # 确定
            self.friend_page.click_article_config_done()
            # 发布渟说
            self.friend_page.click_send()
            # 断言是否发布成功
            try:
                result = self.friend_page.is_toast_exist(self.driver,text='发布成功')
                self.assertTrue(result)
            except Exception as e:
                print(e)
                raise


    def test_post_article03(self):
        u'只发布文本和摘要的文章'
        # 进入盆友圈
        self.friend_page.click_friend()
        # 点击发布渟说按钮
        self.friend_page.click_feed()
        # 选择发布文章
        self.friend_page.click_article()
        # 添加封面
        self.friend_page.click_add_cover()
        # 添加默认封面
        self.friend_page.click_default_cover()
        # 选择默认的照片
        self.friend_page.chose_default_cover()
        # 输入标题
        self.friend_page.send_keys(self.friend_page.article_title, '这个文章只有文本和摘要' )
        # 点击添加文本
        self.friend_page.click_add_text()
        # 输入文本内容
        self.friend_page.send_keys(self.friend_page.text_input, '这里是文章的内容啊，我不知道写点什么内容比较好！')
        # 确认完成编辑
        self.friend_page.click_done_article()
        # 确定
        self.friend_page.click_article_config_done()
        # 输入摘要
        self.friend_page.input_text('这个文章只有标题和摘要')
        self.friend_page.click_send()
        # 断言是否发布成功
        try:
            result = self.friend_page.is_toast_exist(self.driver,text='发布成功')
            self.assertTrue(result)
        except Exception as e:
            print(e)
            raise

    def test_post_article04(self):
        u'只发布带图片和摘要的文章'
        # 进入盆友圈
        self.friend_page.click_friend()
        # 点击发布渟说按钮
        self.friend_page.click_feed()
        # 选择发布文章
        self.friend_page.click_article()
        # 添加封面
        self.friend_page.click_add_cover()
        # 添加默认封面
        self.friend_page.click_default_cover()
        # 选择默认的照片
        self.friend_page.chose_default_cover()
        # 输入标题
        self.friend_page.send_keys(self.friend_page.article_title, '这个文章只有图片和摘要' )
        # 点击添加图片按钮
        self.friend_page.click_add_pic()
        # 选择照片（默认第一张）
        self.friend_page.chose_picture()
        # 确认完成编辑
        self.friend_page.click_done_article()
        # 确定
        self.friend_page.click_article_config_done()
        # 输入摘要
        self.friend_page.input_text('这个文章只有图片和摘要')
        self.friend_page.click_send()
        # 断言是否发布成功
        try:
            result = self.friend_page.is_toast_exist(self.driver,text='发布成功')
            self.assertTrue(result)
        except Exception as e:
            print(e)
            raise


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=='__main__':
    unittest.main()




