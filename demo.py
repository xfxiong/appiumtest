import os
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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
desired_caps['appActivity'] = 'com.android.settings.ChooseLockPattern'

# 包名
# desired_caps['appPackage']='com.ss.android.ugc.aweme'
# #界面名
# desired_caps['appActivity']='com.ss.android.ugc.aweme.splash.SplashActivity'

# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 轻敲
# wlan_button =driver.find_element_by_xpath("//*[@text='WLAN']")
# 创建TouchAction对象,调用方法，perform执行
# TouchAction(driver).tap(wlan_button).perform()

# #按下，2秒后，按下 ，无法进入
# TouchAction(driver).press(x=650,y=650).perform()
# time.sleep(2)
# TouchAction(driver).press(x=650,y=650).perform()
#
# #按下，2秒后，按下抬起 可以进入
# TouchAction(driver).press(x=650,y=650).perform()
# time.sleep(2)
# TouchAction(driver).press(x=650,y=650).release().perform()


# 等待
# TouchAction(driver).tap(x=250,y=258).perform()
# TouchAction(driver).press(x=250,y=258).wait(2000).release().perform() #长按


# TouchAction(driver).tap(x=250,y=258).perform()
# TouchAction(driver).long_press(x=250,y=258,duration=2000).perform()

# 获取手机分辨率
print(driver.get_window_size())

# driver.get_screenshot_as_file(os.getcwd()+os.sep+'./screen.png')

# 获取手机网络
print(driver.network_connection)

# 设置当前网络
driver.set_network_connection(6)

# 手势
# TouchAction(driver).press(x=345,y=982).move_to(x=540,y=982).move_to(x=739,y=982).move_to(x=540,y=1173).release().perform()


# print("准备进入后台————————")
# #进入后台5秒在回到前台
# driver.background_app(5)
# print("回到前台——————————")
# time.sleep(3)

# #判断是否安装
# if driver.is_app_installed('com.microvirt.market'):
#     #如果已安装，卸载
#     driver.remove_app('com.microvirt.market')
# 未安装，要安装
# driver.install_app('apk路径')

# 跳转其他的应用
# driver.start_activity('com.ddnapalon.calculator.gp','com.ddnapalon.calculator.gp.ScienceFragment')

# 获取包名、界面名
# print(driver.current_package)
# print(driver.current_activity)

# 关闭当前操作的App
# driver.close_app()

time.sleep(3)
# 关闭驱动对象
driver.quit()
