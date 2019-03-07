# coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Study(BasePage):
    u'我的学习中心页面'
    # 我的按钮
    my_button = (By.XPATH, "//*[@resource-id='com.mld.LanTin:id/ly_main_home_tab04']")
    # 点击我的
    def click_my_button(self):
        self.find_element(*self.my_button).click()

    # 学习中心
    study_center = (By.ID, "com.mld.LanTin:id/rl_my_study")
    def click_study_center(self):
        self.find_element(*self.study_center).click()

    # 列表为空

    # 封装判断元素是否存在
    def is_element_exist(self):
        u'存在就返回True'
        try:
            loc = (By.ID, "com.mld.LanTin:id/tv_empty")
            WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_element_located(loc))
            return True
        except Exception as e:
            print(e)
            return False

    # 已购课程按钮
    buyed_lesson = (By.ID, "com.mld.LanTin:id/tv_right")
    def click_buyed_lesson(self):
        self.find_element(*self.buyed_lesson).click()

    # 点击澜渟测试专栏
    target_column=(By.XPATH, '//*[@text="免费测试版"]')
    def click_target_column(self):
        self.find_element(*self.target_column).click()

    # 加入学习按钮
    join_study = (By.ID, "com.mld.LanTin:id/bt_join_study")
    def click_join_study(self):
        self.find_element(*self.join_study).click()

    # 学习列表第一个
    the_first = (By.ID, "com.mld.LanTin:id/content")
    def get_size_of_first(self):
        s = self.find_elements(*self.the_first)[0].get_attribute("bounds")
        return s

    # 取消学习按钮
    cancle_study = (By.ID, "com.mld.LanTin:id/tv_delete")
    def click_cancle_study(self):
        self.find_element(*self.cancle_study).click()

    # 点击确定按钮
    def yes_or_no(self, choice):
        u'choice只可以输入确定或者取消'
        loc = (By.ID, "com.mld.LanTin:id/btn_ok")
        self.find_element(*loc).click()






