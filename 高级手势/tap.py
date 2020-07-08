from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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
# 获取“更多”元素
more_button=driver.find_element_by_xpath("//*[contains(@text,'更多')]")
# 轻敲
TouchAction(driver).tap(more_button).perform()