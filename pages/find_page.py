# coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Find(BasePage):

    # 发现按钮
    find_button = (By.ID, "com.mld.LanTin:id/iv_main_home_03")
    # 进入发现
    def click_find_button(self):
        self.find_element(*self.find_button).click()
    # 商城按钮
    mall_button = (By.ID, "com.mld.LanTin:id/rl_shop")

    # 进入商城
    def click_mall_button(self):
        self.find_element(*self.mall_button).click()

    # 立即购买按钮
    buy_now = (By.ID, "com.mld.LanTin:id/btn_buy_device")
    # 进入购买页（第一个商品）
    def click_buy_now(self):
        self.find_elements(*self.buy_now)[0].click()

    # 选择规格按钮
    goods_type = (By.ID, "com.mld.LanTin:id/tv_item_value")
    type_button = (By.ID, "com.mld.LanTin:id/tv_goods_spec")
    # 进入选择规格
    def click_goods_type(self):
        # 进入选择规格页
        self.find_element(*self.goods_type).click()
        # 选择第一个规格
        self.find_element(*self.type_button).click()

    # 商品-增加数量
    add_num = (By.ID, "com.mld.LanTin:id/btn_add")
    # 输入数量
    def goods_num(self,num):
        """如果只买一件则return出去，若买>1个则执行循环"""
        if num==1:
            return
        elif num > 1:
            i = 1
            while i < num:
                self.find_element(*self.add_num).click()
                i += 1

    # 确认购买
    buy_it = (By.ID, "com.mld.LanTin:id/btn_confirm_order")
    # 点击确认购买
    def click_buy_it(self):
        self.find_element(*self.buy_it).click()

    # 提交订单按钮
    submit_order = (By.ID, "com.mld.LanTin:id/btn_confirm_order")
    # 点击提交订单
    def click_submit_order(self):
        self.find_element(*self.submit_order).click()


    # 去支付按钮()
    pay_button = (By.ID, "com.mld.LanTin:id/btn_go_pay")
    # 点击去支付
    def click_pay_button(self, pay_way):
        if pay_way == "微信":
            self.find_element(*self.pay_button).click()
        else:

            alipay_button = (By.ID, "com.mld.LanTin:id/ll_alipay")
            # 选择支付宝支付
            self.find_element(*alipay_button).click()
            # 点击去支付
            self.find_element(*self.pay_button).click()










    # 我的医生
    doctor_button = (By.ID, "com.mld.LanTin:id/rl_me_doctor")
    # 进入我的医生
    def click_doctor_button(self):
        self.find_element(*self.doctor_button).click()
    # 我的科室
    department_button = (By.ID, "com.mld.LanTin:id/rl_dep")
    # 进入我的科室
    def click_department_button(self):
        self.find_element(*self.department_button).click()



