# coding:utf-8
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Classroom(BasePage):

    # 极致课堂按钮
    best_classroom = (By.ID, "com.mld.LanTin:id/ly_main_home_news")
    # 进入极致课堂
    def click_best_classroom(self):
        self.find_element(*self.best_classroom).click()


    # 专栏按钮
    column_button = (By.ID, "com.mld.LanTin:id/ll_to_column")
    def click_column(self):
        self.find_element(*self.column_button).click()

    # 产后更美专栏
    last_column = (By.XPATH, '//*[@text="产后更美 - 10位专家说"]')
    def click_last_column(self):
        self.find_element(*self.last_column).click()

    # 购买专栏按钮
    buy_column = (By.ID, "com.mld.LanTin:id/btn_buy_column")
    def click_buy_column(self):
        self.find_element(*self.buy_column).click()

    # 提交订单按钮
    submit_column_btn = (By.ID, 'com.mld.LanTin:id/btn_submit_column_order')
    def click_submit_column_btn(self):
        self.find_element(*self.submit_column_btn).click()

    # 去支付按钮()
    pay_button = (By.XPATH, '//*[@text="去支付"]')
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




    # 课程按钮
    lesson_button = (By.ID, "com.mld.LanTin:id/ll_to_course")
    def click_lesson_button(self):
        self.find_element(*self.lesson_button).click()

    # 课程名称
    lesson_name = (By.XPATH, '//*[@text="1.母乳如何储存"]')
    def click_lesson_name(self):
        self.find_element(*self.lesson_name).click()

    # 章节按钮
    chapter_btn = (By.ID, "com.mld.LanTin:id/rl_detail_chapter")
    def click_chapter_btn(self):
        self.find_element(*self.chapter_btn).click()

    # 点击章节名称播放
    first_chapter = (By.ID, "com.mld.LanTin:id/rl_root")
    def click_first_chap(self):
        self.find_element(*self.first_chapter).click()

    # 购买课程按钮
    buy_lesson = (By.ID, "com.mld.LanTin:id/bt_join_study")
    def click_buy_lesson(self):
        self.find_element(*self.buy_lesson).click()

    # 课程提交订单
    submit_lesson_btn = (By.ID, "com.mld.LanTin:id/btn_submit_column_order")
    def click_submit_lesson_btn(self):
        self.find_element(*self.submit_lesson_btn).click()
    # 去支付调用专栏去支付方法





    # 直播按钮
    live_button = (By.ID, "com.mld.LanTin:id/ll_to_live")
    def click_live(self):
        self.find_element(*self.live_button).click()

    # 直播中按钮
    living_btn = (By.ID, "com.mld.LanTin:id/rl_living")
    def click_living_btn(self):
        self.find_element(*self.living_btn).click()

    # 排序最后一个直播
    secondlive_loc = (By.ID, "com.mld.LanTin:id/rl_live_item")
    # 点击第二个直播（ceshi）
    def click_secondlive(self):
        self.find_elements(*self.secondlive_loc)[1].click()

    # 进入课堂按钮
    enter_live_btn = (By.ID, "com.mld.LanTin:id/tv_enter_live")
    def click_enter_live(self):
        self.find_element(*self.enter_live_btn).click()

    # 查看评论按钮
    check_comment = (By.ID, "com.mld.LanTin:id/tv_chat_count")
    def click_check_comment(self):
        self.find_element(*self.check_comment).click()

    # 输入框输入评论
    input_btn = (By.XPATH, '//*[@text="点击这里开始互动..."]')
    def input_comment(self, text):
        self.send_keys(loc=self.input_btn, vaule=text)

    # 发送评论按钮
    send_comment = (By.ID, "com.mld.LanTin:id/bt_text_send")
    def click_send_comment(self):
        self.find_element(*self.send_comment).click()

    # 评论列表第一条
    fist_comment_loc = (By.ID, "com.mld.LanTin:id/tv_info")
    def get_comment_text(self):
        t = self.find_elements(*self.fist_comment_loc)[0].text
        return t

    # 操作评论按钮
    do_comment = (By.ID, "com.mld.LanTin:id/tv_doto")
    def click_do_comment(self):
        self.find_elements(*self.do_comment)[0].click()

    # 删除评论
    del_comment = (By.ID, "com.mld.LanTin:id/tv_item")
    btn_ok = (By.ID, "com.mld.LanTin:id/btn_ok")
    def click_del_comment(self):
        self.find_element(*self.del_comment).click()
        self.find_element(*self.btn_ok).click()




