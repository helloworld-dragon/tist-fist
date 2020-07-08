from appium import webdriver
	# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
de# 实例化对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 解决输入中文问
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

while True:
    try:
        driver.find_element_by_xpath("//*[contains(@text,'关于平板电脑')]").click()
        break
    except Exception:
        driver.swipe(100,1000,100,200,1000)
eles = driver.find_elements_by_class_name("android.widget.TextView")
for i in eles:
     if i.text == "5.1.1":
          print("该手机android版本是5.1.1")
          break
else:
     print("该手机android版本不是5.1.1")