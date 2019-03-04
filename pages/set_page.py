#coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SetPage(BasePage):
    u'设置页面'
    # 定位器，需要用到的元素
    # 设置按钮
    set_button = (By.ID, "com.mld.LanTin:id/rl_setting")
    # 账号安全
    # 我的设备
    # 收货地址
    # 发票抬头
    # 关于我们
    # 退出登录按钮
    out_button = (By.ID, "com.mld.LanTin:id/btn_login_out")
    # 确定退出
    config_logout = (By.ID, "com.mld.LanTin:id/btn_ok")

    #点击设置按钮
    def click_set(self):
        self.find_element(*self.set_button).click()
        time.sleep(1)

    # 确认退出登录
    def logout(self):
        # 点击设置
        self.find_element(*self.set_button).click()
        time.sleep(1)
        # 点击退出登录
        self.find_element(*self.out_button).click()
        time.sleep(1)
        # 点击确定退出
        self.find_element(*self.config_logout).click()

