# coding:utf-8
from appium import webdriver


# desired_caps 就是你需要启动的app的一些参数
desired_caps = {
        'platformName': 'android',  # 平台系统
        'deviceName': 'GB8ZAH154R', # 设备名字，adb devices可获得
        'platformVersion': '5.1.1', # 安卓系统版本
        'appPackage': 'com.medlander.b40tablet', # 包名，通过命令：aapt dump badging +apk 可获得
        'appActivity': 'com.medlander.b40tablet.activity.LoadingActivity',  # apk的launcherActivity
        'noReset': True,  # app不重置
        'newCommandTimeout': '150000' # 超时设置，appium保持与设备连接
    }
# 启动app ,在运行此py脚本之前需要先打开并启动appium
# 127.0.0.1 就是本机地址  4723是appium默认使用的端口
driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
# 点击数据管理
driver.find_element_by_id('com.medlander.b40tablet:id/iv_data_manager').click()
# 点击数据统计
driver.find_element_by_id('com.medlander.b40tablet:id/btn_data_statistics').click()
# 点击全部数据
driver.find_element_by_id('com.medlander.b40tablet:id/rb_all').click()
# 点击开始统计
driver.find_element_by_id('com.medlander.b40tablet:id/btn_confirm').click()
# 获取人数
number = driver.find_element_by_id('com.medlander.b40tablet:id/tv_user_count').get_attribute('text')
# 断言查询出的人数(就是测试中的所谓的检查点/预期结果)
assert number == '4'


