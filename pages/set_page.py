#coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SetPage(BasePage):
    u'设置页面'

    # 我的按钮
    my_button = (By.XPATH, "//*[@resource-id='com.mld.LanTin:id/ly_main_home_tab04']")
    # 点击我的
    def click_my_button(self):
        self.find_element(*self.my_button).click()

    # 设置按钮
    set_button = (By.ID, "com.mld.LanTin:id/rl_setting")

    # 账号安全

    # 我的设备

    # 收货地址
    adress_btn = (By.ID, "com.mld.LanTin:id/rl_delivery_address")
    def click_adress_btn(self):
        self.find_element(*self.adress_btn).click()

    # 新增按钮
    add_address = (By.ID, "com.mld.LanTin:id/btn_add_address")
    def click_add_address(self):
        self.find_element(*self.add_address).click()

    # 姓名输入框
    name_input = (By.ID, "com.mld.LanTin:id/et_name")
    # 手机号输入框
    phone_input = (By.ID, "com.mld.LanTin:id/et_tel")

    # 地区
    chose_area = (By.ID, "com.mld.LanTin:id/tv_area")
    def click_chose_area(self):
        self.find_element(*self.chose_area).click()
    # 选择省再选择市
    item = (By.ID, "com.mld.LanTin:id/tv_item_title")
    def chose_city(self):
        u'默认选择第一个省，第一个市'
        # 第一个省
        self.find_elements(*self.item)[0].click()
        time.sleep(1)
        # 第一个市
        self.find_elements(*self.item)[0].click()

    # 地址输入框
    address_input = (By.ID, "com.mld.LanTin:id/et_detail_address")

    # 保存按钮
    save_btn = (By.ID, "com.mld.LanTin:id/btn_save_address")
    def click_save_btn(self):
        self.find_element(*self.save_btn).click()

    # 管理列表中收货人姓名
    reciever_name = (By.ID, "com.mld.LanTin:id/tv_name")
    def get_reciever_name(self):
        u'获取列表中第一个人姓名'
        name = self.find_elements(*self.reciever_name)[0].get_attribute('text')
        return name

    # 管理列表中收获人号码
    reciever_phone = (By.ID, "com.mld.LanTin:id/tv_phone")
    def get_reciever_phone(self):
        u'获取列表中第一个人号码'
        num = self.find_elements(*self.reciever_phone)[0].get_attribute('text')
        return num

    # 编辑地址按钮
    update_address = (By.ID, "com.mld.LanTin:id/btn_update_address")
    def click_update(self):
        self.find_elements(*self.update_address)[0].click()

    # 删除地址按钮
    del_address = (By.ID, "com.mld.LanTin:id/btn_delete_address")
    def click_del_address(self):
        self.find_element(*self.del_address).click()

    # 确定删除/取消删除
    def yes_or_no(self, choice):
        loc = (By.ID, "com.mld.LanTin:id/btn_ok")
        loc2 = (By.ID, "com.mld.LanTin:id/btn_cancel")
        if choice == '确定':
            self.find_element(*loc).click()
        else:
            self.find_element(*loc2).click()



    # 发票抬头
    invoice_title = (By.ID, "com.mld.LanTin:id/rl_bill_title")
    def click_invoice_title(self):
        self.find_element(*self.invoice_title).click()

    # 新增发票按钮
    add_title = (By.ID, "com.mld.LanTin:id/btn_add_bill")
    def click_add_title(self):
        self.find_element(*self.add_title).click()

    # 新增个人抬头
    add_person_title = (By.ID, "com.mld.LanTin:id/radioPerson")
    def click_add_person_title(self):
        self.find_element(*self.add_person_title).click()
    # 新增单位抬头
    add_co_title = (By.ID, "com.mld.LanTin:id/radioCompany")
    def click_add_co_title(self):
        self.find_element(*self.add_co_title).click()
    # 抬头名称
    title_name = (By.ID, "com.mld.LanTin:id/et_bill_name")
    # 纳税识别号
    title_number = (By.ID, "com.mld.LanTin:id/et_bill_id")
    # 保存按钮
    save_invoice_title = (By.ID, "com.mld.LanTin:id/btn_save_bill_detail")
    def click_save_title(self):
        self.find_element(*self.save_invoice_title).click()

    # 设置默认按钮,设置第一个为默认
    default_btn = (By.ID, "com.mld.LanTin:id/cb_set_default")
    def click_default_btn(self):
        self.find_elements(*self.default_btn)[0].click()

    # 获取发票抬头列表中抬头数量
    def get_title_num(self):
        loc = (By.ID, "com.mld.LanTin:id/rl_content")
        n = self.find_elements(*loc)
        return len(n)

    # 获取第一个抬头坐标
    def get_location(self):
        loc = (By.ID, "com.mld.LanTin:id/rl_content")
        d1 = self.find_elements(*loc)[0].rect  # 打印坐标
        print(d1)
        return d1
    # 点击删除按钮
    del_title = (By.XPATH, '//*[@text="删除"]')
    def click_del_title(self):
        self.find_element(*self.del_title).click()




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

