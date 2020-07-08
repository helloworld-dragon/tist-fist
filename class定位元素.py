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
# # id 点击搜索按钮
# driver.find_element_by_id("com.android.settings:id/search").click()
# # class 点击输入框返回按钮
# driver.find_element_by_class_name('android.widget.ImageButton').click()
# driver.quit()
# xpath 点击WLAN按钮
driver.find_element_by_xpath("//*[contains(@text,'WLA')]").click()