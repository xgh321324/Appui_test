# coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Friend(BasePage):
    u'盆友圈-推荐页'
    # 朋友圈按钮
    friend_button = (By.ID, "com.mld.LanTin:id/iv_main_home_02")
    # 点击朋友圈按钮
    def click_friend(self):
        self.find_element(*self.friend_button).click()

    # 发布按钮
    feed = (By.ID, "com.mld.LanTin:id/iv_issue_feed")
    # 点击发布按钮
    def click_feed(self):
        self.find_element(*self.feed).click()

    # 发布文字按钮
    feed_text = (By.ID, "com.mld.LanTin:id/publish_text")
    #点击发布文字按钮
    def click_text(self):
        self.find_element(*self.feed_text).click()

    # 文字输入框
    input_field = (By.XPATH, '//*[@resource-id="com.mld.LanTin:id/et_editor"]')
    # 输入文本内容
    def input_text(self,text):
        self.find_element(*self.input_field).send_keys(text)

    # 发送按钮
    send_button = (By.ID, "com.mld.LanTin:id/tv_publish")
    # 点击发送按钮
    def click_send(self):
        self.find_element(*self.send_button).click()
    # 发布图片按钮
    feed_pic = (By.ID, "com.mld.LanTin:id/publish_image")
    #  点击发布图片按钮
    def click_pic(self):
        self.find_element(*self.feed_pic).click()
    # 下一步调用chose_pic


    # 发布视频按钮
    feed_video = (By.ID, "com.mld.LanTin:id/publish_video")
    # 点击发布视频按钮
    def click_video(self):
        self.find_element(*self.feed_video).click()
    # 拍摄按钮（开始）
    record_start = (By.ID, "com.mld.LanTin:id/iv_start")
    # 点击开始
    def click_record_start(self):
        self.find_element(*self.record_start).click()

    # 拍摄按钮（停止）
    record_end = (By.XPATH, '//*[@resource-id="com.mld.LanTin:id/iv_stop"]')
    # 点击停止
    def click_record_end(self):
        self.find_element(*self.record_end).click()

    # 完成录制
    record_complete = (By.ID, "com.mld.LanTin:id/iv_complete")
    # 点击完成录制
    def click_record_complete(self):
        self.find_element(*self.record_complete).click()




    # 发布文章按钮
    feed_article = (By.ID, "com.mld.LanTin:id/publish_article")
    # 点击发布文章按钮
    def click_article(self):
        self.find_element(*self.feed_article).click()

    # 编辑文章-添加封面按钮
    add_cover = (By.ID, "com.mld.LanTin:id/rl_add_cover")
    def click_add_cover(self):
        self.find_element(*self.add_cover).click()
    # 点击默认封面按钮
    default_cover = (By.ID, "com.mld.LanTin:id/default_cover")
    def click_default_cover(self):
        self.find_element(*self.default_cover).click()
    # 选择默认封面第一张
    default_first_cover = (By.ID, "com.mld.LanTin:id/iv_default_cover")
    def chose_default_cover(self):
        self.find_elements(*self.default_first_cover)[0].click()
    # 文章标题按钮
    article_title = (By.ID, "com.mld.LanTin:id/article_title")

    # 文章添加文本按钮
    add_text = (By.ID, "com.mld.LanTin:id/add_text")
    def click_add_text(self):
        self.find_element(*self.add_text).click()
    # 文章中文本输入框
    text_input = (By.ID, "com.mld.LanTin:id/text_edit")
    # 文章添加图片按钮
    add_pic = (By.ID, "com.mld.LanTin:id/add_pic")
    def click_add_pic(self):
        self.find_element(*self.add_pic).click()

    # 文章完成编辑按钮
    done_article = (By.ID, "com.mld.LanTin:id/fl_right")
    def click_done_article(self):
        self.find_element(*self.done_article).click()

    # 确定完成编辑
    article_config_done = (By.ID, "com.mld.LanTin:id/operate_1")
    def click_article_config_done(self):
        self.find_element(*self.article_config_done).click()
    # 摘要框，摘要输入框同发布文字框




    # 关注按钮
    follow = (By.ID, "com.mld.LanTin:id/tv_attention")
    # 推荐按钮
    recommend = (By.ID, "com.mld.LanTin:id/tv_hot")

    # 圈子按钮
    group = (By.ID, "com.mld.LanTin:id/tv_circle")
    # 点击圈子按钮
    def click_group(self):
        self.find_element(*self.group).click()

    # 用户按钮
    user = (By.ID, "com.mld.LanTin:id/tv_user")
    # 点击用户按钮
    def click_user(self):
        self.find_element(*self.user).click()




##########################################
    # 点击选择相册第一张图片，此方法公用
    def chose_picture(self, pic_num=1):
        # 定位图片列表选择第一张
        locs = (By.ID, "com.mld.LanTin:id/check_view")
        time.sleep(1)
        for i in range(pic_num):
            self.find_elements(*locs)[i].click()
        time.sleep(2)
        # 点击确认
        config = (By.ID, "com.mld.LanTin:id/button_apply")
        self.find_element(*config).click()






if __name__ == '__main__':
    desired_caps = {
        'platformName': 'android',
        'deviceName': '740dc3d1',
        'platformVersion': '8.0.0',
        'appPackage': 'com.mld.LanTin',
        'appActivity': 'com.mld.LanTin.main.activity.SplashActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True
    }
    driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
    driv = Friend(driver)



