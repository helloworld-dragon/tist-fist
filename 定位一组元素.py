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
# 定位到一组元素
title = driver.find_elements_by_id("com.android.settings:id/title")
# 打印title类型，预期为list
print(type(title))
# 取title返回列表中的第一个定位对象，执行点击操作
title[0].click()