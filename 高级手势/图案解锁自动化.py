from appium import webdriver
	# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.ChooseLockPattern'
# 解决输入中文问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 实例化对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

TouchAction(driver)\
    .press(x=178,y=643)\
    .move_to(x=538,y=643)\
    .move_to(x=898,y=643)\
    .move_to(x=898,y=1003)\
    .move_to(x=898,y=1363)\
    .move_to(x=538,y=1363)\
    .move_to(x=178,y=1003)\
    .release()\
    .perform()
# press  按下
# tag    轻敲
# long_press  长按
# release  松手
# move_to  移动
# perform  执行
