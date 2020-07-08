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
save_batton=driver.find_element_by_xpath("//*[contains(@text,'蓝牙')]")
more_batton=driver.find_element_by_xpath("//*[contains(@text,'显示')]")
battery_batton=driver.find_element_by_xpath("//*[contains(@text,'存储')]")
driver.drag_and_drop(battery_batton,save_batton)


# swipe和drag的区别：drag没有“惯性”
# 相同点：都是使用元素形式传参