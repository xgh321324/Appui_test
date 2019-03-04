#coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Personal(BasePage):
    # 进入我的
    my_button = (By.XPATH, "//*[@resource-id='com.mld.LanTin:id/ly_main_home_tab04']")
    # 点击我的
    def click_my_button(self):
        self.find_element(*self.my_button).click()

    # 进入个人信息
    personal_btn = (By.ID, "com.mld.LanTin:id/rl_person_info")
    def click_personal_btn(self):
        self.find_element(*self.personal_btn).click()

    # 进入昵称栏
    nick_name = (By.ID, "com.mld.LanTin:id/rl_person_nickname")
    def click_nick_name(self):
        self.find_element(*self.nick_name).click()

    # 昵称输入框
    nick_name_input = (By.ID, "com.mld.LanTin:id/et_input_text1")

    # 提交昵称
    finish_btn = (By.ID, "com.mld.LanTin:id/btn_finish")
    def click_finish(self):
        self.find_element(*self.finish_btn).click()

    # 我的页面显示的真实昵称
    real_nick_name = (By.ID, "com.mld.LanTin:id/tv_real_name")

    #进入地区栏
    address = (By.ID, "com.mld.LanTin:id/rl_person_address")
    def click_address(self):
        self.find_element(*self.address).click()

    # 选择省再选择市
    item = (By.ID, "com.mld.LanTin:id/tv_item_title")
    def chose_city(self):
        u'默认选择第一个省，第一个市'
        # 第一个省
        self.find_elements(*self.item)[0].click()
        time.sleep(1)
        # 第一个市
        self.find_elements(*self.item)[0].click()



