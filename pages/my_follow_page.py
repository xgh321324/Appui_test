# coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MyFollow(BasePage):
    u'我的渟说页面'

    # 我的按钮
    my_button = (By.XPATH, "//*[@resource-id='com.mld.LanTin:id/ly_main_home_tab04']")
    # 点击我的
    def click_my_button(self):
        self.find_element(*self.my_button).click()
    # 关注
    follow = (By.ID, "com.mld.LanTin:id/tv_attention")
    def click_follow(self):
        self.find_elements(*self.follow)[0].click()

    # 关注状态按钮
    user_attention = (By.ID, "com.mld.LanTin:id/tv_user_attention")
    def click_user_attention(self):
        self.find_elements(*self.user_attention)[0].click()
    # 获取关注状态
    def get_user_attention_state(self):
        t = self.find_elements(*self.user_attention)[0].text
        return t

    # 确定按钮
    yes_btn = (By.ID, "com.mld.LanTin:id/operate_1")
    def click_yes_btn(self):
        self.find_element(*self.yes_btn).click()
