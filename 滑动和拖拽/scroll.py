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
time.sleep(3)
save_batton=driver.find_element_by_xpath("//*[contains(@text,'显示')]")
more_batton=driver.find_element_by_xpath("//*[contains(@text,'存储')]")
driver.scroll(more_batton,save_batton)
# 和swipe相比，都存在一定的惯性，
# 和swipe相比，参数不同，一个是坐标（swipe），一个是元素（scroll）
