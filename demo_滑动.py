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
desired_caps['appPackage'] = 'com.hcloud.wocom'
# 界面名
desired_caps['appActivity'] = 'com.hcloud.pan.ui.activity.login.LoginNewActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.hcloud.wocom:id/tv_right").click()

driver.find_element_by_id("com.hcloud.wocom:id/tv_psw").click()

driver.find_element_by_id("com.hcloud.wocom:id/et_phone").send_keys("18000000310")

driver.find_element_by_id("com.hcloud.wocom:id/et_psw").send_keys("Abc1234@")

driver.find_element_by_id("com.hcloud.wocom:id/bt_next").click()
time.sleep(5)
driver.find_element_by_id("com.hcloud.wocom:id/tab_my").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@text,'应用')]").click()

driver.find_element_by_id("com.hcloud.wocom:id/gesture").click()

driver.quit()
