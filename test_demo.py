import time

from appium import webdriver

desired_caps = dict()
# 平台名称，大小写无所谓
desired_caps['platformName'] = 'Android'
# 平台版本（5.4.3 可以写5.4.3,5.4,5）
desired_caps['platformVersion'] = '7.1'
# 设备名称，可以随便写，但是不能乱写
desired_caps['deviceName'] = 'VOG-AL00'
# 包名
desired_caps['appPackage'] = 'com.android.settings'
# 界面名
desired_caps['appActivity'] = '.Settings'

# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# #--------定位一个元素
# #通过id，点击放大镜
# driver.find_element_by_id('com.android.settings:id/search').click()
# #通过class 定位输入框，输入hello
# driver.find_element_by_class_name('android.widget.EditText').send_keys('hello')
# #通过xpath 定位返回 ，点击
# driver.find_element_by_xpath("//*[@content-desc='收起']").click()

# #----------定位一组元素，通过id，并打印文字内容
# titles = driver.find_elements_by_id('android:id/title')
# print(len(titles))
# # print(titles)
# for title in titles:
#     print(title.text)
# titles[1].click()

# 通过xpath,获取包含‘设’的元素，并打印
# eles =driver.find_elements_by_xpath('//*[contains(@text,"设")]')
# print(eles)
# for ele in eles:
#     print(ele.text)

# ——————————注意点——————


time.sleep(3)

driver.quit()
