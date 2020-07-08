from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType

	# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 解决输入中文问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 实例化对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 获取手机时间
print(driver.device_time)
# 获取手机的宽和高
print(driver.get_window_size())
# 控制音量键
# 音量加
# for i in range(3):
#     driver.keyevent(24)
# # 音量减
# time.sleep(3)
#
# for i in range(3):
#     driver.keyevent(25)
# 打开通知栏
driver.open_notifications()
# 获取当前网络
print(driver.network_connection)
# 设置当前网络
driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
# 获取屏幕截图
driver.get_screenshot_as_file("./手机屏幕截图.png")