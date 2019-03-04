#coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MyPage(BasePage):
    u'我的页面'
    # 定位器，需要用到的元素
    # 我的按钮
    my_button = (By.XPATH, "//*[@resource-id='com.mld.LanTin:id/ly_main_home_tab04']")
    # 登录按钮
    login_button = (By.XPATH,'//*[@text="登录"]')
    # 用户名
    real_name = (By.ID, "com.mld.LanTin:id/tv_real_name")

    # 进入渟说
    feed = (By.ID, "com.mld.LanTin:id/tv_publish")
    def click_feed(self):
        self.find_element(self.feed).click()


    # 关注
    follow = (By.ID, "com.mld.LanTin:id/tv_attention")
    # 粉丝
    fans = (By.ID, "com.mld.LanTin:id/tv_fans")
    # 我的收藏
    collect = (By.ID, "com.mld.LanTin:id/ic_me_favorite")

    # 我的直播间
    my_chat_room = (By.ID, "com.mld.LanTin:id/rl_my_chatroom")
    def click_my_chat_room(self):
        self.find_element(*self.my_chat_room).click()

    # 关注按钮
    attention_btn = (By.ID, "com.mld.LanTin:id/tv_room_attention")
    def click_attention_btn(self):
        self.find_element(*self.attention_btn).click()

    # 确定按钮
    yes_btn = (By.XPATH, '//*[@text="确定"]')
    def click_yes_btn(self):
        self.find_element(*self.yes_btn).click()

    # 进入直播间
    room_name = (By.ID, "com.mld.LanTin:id/tv_room_name")
    def click_room_name(self):
        self.find_element(*self.room_name).click()

    # 直播间标题
    room_title = (By.ID, "com.mld.LanTin:id/tv_title")






    # 意见反馈
    feedback = (By.ID, "com.mld.LanTin:id/rl_feedback")
    # 进入意见反馈
    def click_feedback(self):
        self.find_element(*self.feedback).click()

    # 标题
    feedback_title = (By.ID, "com.mld.LanTin:id/et_feedback_title")
    # 反馈内容
    feedback_content = (By.ID, "com.mld.LanTin:id/et_feedback_content")

    # 添加图片
    add_pic = (By.ID, "com.mld.LanTin:id/fl_add")
    def click_add_pic(self):
        self.find_element(*self.add_pic).click()
    # 选择照片调用friendpage的 chose_pic方法

    # 提交按钮
    submit_feedback_btn = (By.ID, "com.mld.LanTin:id/btn_submit")
    def click_submit_feedback_btn(self):
        self.find_element(*self.submit_feedback_btn).click()




    # 设置
    set_button = (By.ID, "com.mld.LanTin:id/rl_setting")

    # 点击我的
    def click_my_button(self):
        self.find_element(*self.my_button).click()
    # 获取用户名text
    def get_username(self):
        return self.find_element(self.real_name).text
    # 点击设置
    def login_out(self):
        self.find_element(*self.set_button).click()
    # 点击登录按钮
    def click_login_button(self):
        self.find_element(*self.login_button).click()
        time.sleep(3)


