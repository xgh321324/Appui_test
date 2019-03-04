#coding:utf-8
import os

class Event():
    '''常用keyevent事件'''
    KEYCODE_HOME = 3         # home键
    KEYCODE_MENU = 82        # menu键
    KEYCODE_BACK = 4         # back键
    KEYCODE_POWER = 26       # power键
    KEYCODE_DPAD_UP = 19     # 向上
    KEYCODE_DPAD_DOWN = 20   # 向下
    KEYCODE_DPAD_LEFT = 21   # 向左
    KEYCODE_DPAD_RIGHT = 22  # 向右
    KEYCODE_NOTIFICATION = 83  # 解锁
    KEYCODE_VOLUME_UP = 24  # 音量+
    KEYCODE_VOLUME_DOWN = 25  # 音量-

# 点击返回键
def back(keyname=Event.KEYCODE_BACK):
    ' 执行adb keyevent事件 参数从Event类里面关联'
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)

# 点击home键
def home(keyname = Event.KEYCODE_HOME):
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)

# 点击菜单键
def menu(keyname= Event.KEYCODE_MENU):
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)

# 按一下电源键
def power(keyname=Event.KEYCODE_POWER):
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)

# 增加音量
def volume_up(keyname=Event.KEYCODE_VOLUME_UP):
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)
    os.system(adb)

# 增加音量
def volume_down(keyname=Event.KEYCODE_VOLUME_DOWN):
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)
    os.system(adb)


# 向上滑动
def up(keyname = Event.KEYCODE_DPAD_UP):
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)

# 向下滑动
def down(keyname = Event.KEYCODE_DPAD_DOWN):
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)

# 向左滑动
def left(keyname= Event.KEYCODE_DPAD_LEFT):
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)

# 向右滑动
def right(keyname= Event.KEYCODE_DPAD_RIGHT):
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)

# adb也可以输入文本
def input_text(text):
    u'adb输入是text文本，不支持中文'
    adb = 'adb shell input text %s' % text
    os.system(adb)

if __name__=='__main__':
    back()
    back()
    volume_up()






