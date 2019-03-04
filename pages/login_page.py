#coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    u'登录页面'
    # 定位器，需要用到的元素

    # 进入登录页
    login_button = (By.ID, "")
    # 用户名
    username_loc = (By.ID,"com.mld.LanTin:id/et_telephone")
    # 密码
    password_loc = (By.ID,"com.mld.LanTin:id/et_checkcode")
    # 同意
    agree_loc = (By.ID,"com.mld.LanTin:id/cb_UserAgreement")
    # 登录
    submit_loc = (By.ID,"com.mld.LanTin:id/btn_tel_login")
    # 微信
    wechat = (By.ID,"com.mld.LanTin:id/btn_wx_login")
    # 成功后用户名
    real_name = (By.XPATH,"//*[@resource-id='com.mld.LanTin:id/tv_real_name']")




    '''
    以下所有发find_element方法均为继承父类使用父类的
    '''
    # 操作用户名输入框
    def input_usernam(self,user):
        return self.find_element(*self.username_loc).send_keys(user)

    # 操作验证码输入框
    def input_pass(self,psw):
        return self.find_element(*self.password_loc).send_keys(psw)

    # 点击登录
    def tap_login(self):
        return self.find_element(*self.submit_loc).click()

    # 微信登录
    def wechat_login(self):
        return self.find_element(*self.wechat).click()

    # 登录后用户名
    def show_name(self):
        return self.find_element(*self.real_name).text


