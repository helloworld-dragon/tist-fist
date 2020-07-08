import time

from appium import webdriver
	# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 时间戳
print(time.time())
# swipe通过driver来使用
# 需要传入起始位置的x和y 结束位置的x和y
# 时间参数，越长时间的滑动越精准
# 如何获取当前的时间戳
# 时间戳是从1970年到现在过了多少秒
driver.swipe(100,1500,100,200,3000)
print(time.time())