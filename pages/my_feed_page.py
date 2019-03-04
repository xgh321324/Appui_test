# coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MyFeed(BasePage):
    u'我的渟说页面'

    # 我的按钮
    my_button = (By.XPATH, "//*[@resource-id='com.mld.LanTin:id/ly_main_home_tab04']")
    # 点击我的
    def click_my_button(self):
        self.find_element(*self.my_button).click()

    # 进入渟说
    feed = (By.ID, "com.mld.LanTin:id/tv_publish")
    def click_feed(self):
        self.find_element(*self.feed).click()
    # 收藏按钮
    collect_btn = (By.ID, "com.mld.LanTin:id/iv_collect")
    def click_collect_btn(self):
        self.find_element(*self.collect_btn).click()

    # 点赞
    like_btn = (By.ID, "com.mld.LanTin:id/iv_like")
    def click_like_btn(self):
        self.find_element(*self.like_btn).click()
    # 点赞个数
    like_num = (By.ID, "com.mld.LanTin:id/tv_like")

    # 删除渟说
    del_feed_btn = (By.ID, "com.mld.LanTin:id/iv_delete")
    def click_del_feed_btn(self):
        self.find_element(*self.del_feed_btn).click()

    #渟说详情
    feed_info = (By.ID, "com.mld.LanTin:id/iv_comment")
    def click_feed_info(self):
        self.find_element(*self.feed_info).click()


    # 评论按钮
    comment_btn = (By.ID, "com.mld.LanTin:id/tv_bottom_comment")
    def click_comment_btn(self):
        self.find_element(*self.comment_btn).click()

    # 评论/回复评论 输入框
    input_comment = (By.ID, "com.mld.LanTin:id/et_comment")

    #发送 评论/回复评论 按钮
    send_comment = (By.XPATH, '//*[@resource-id="com.mld.LanTin:id/tv_send_comment"]')
    def click_send_comment(self):
        self.find_element(*self.send_comment).click()

    # 获取评论数量
    comment_text = (By.ID, "com.mld.LanTin:id/tv_comment")
    def get_comment_num(self):
        t = self.find_element(*self.comment_text).text
        # 分割得到评论数量
        result = int(t)
        return result

    # 回复评论按钮
    reply_comment = (By.ID, "com.mld.LanTin:id/iv_reply")
    def click_reply_comment(self):
        self.find_elements(*self.reply_comment)[0].click()

    # 删除评论按钮
    del_comment_btn = (By.ID, "com.mld.LanTin:id/iv_delete")
    def click_del_comment_btn(self):
        self.find_elements(*self.del_comment_btn)[0].click()

    # 确定按钮
    yes_btn = (By.ID, "com.mld.LanTin:id/operate_1")
    def click_yes_btn(self):
        self.find_element(*self.yes_btn).click()








