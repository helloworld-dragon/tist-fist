from appium import webdriver
	# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = '.activities.PeopleActivity'
# 解决输入中文问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 实例化对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)