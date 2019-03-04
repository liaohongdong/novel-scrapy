# coding=utf-8
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()  # 窗口最大化

browser.get('https://www.baidu.com')  # 在当前浏览器中访问百度
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[4]/h3/a").click()
time.sleep(3)
print(browser.current_window_handle)  # 输出当前窗口句柄
handles = browser.window_handles  # 获取当前窗口句柄集合（列表类型）
browser.switch_to.window(handles[1]) # 切换窗口
print(browser.find_element_by_xpath("/html/head/title").get_attribute("innerHTML"))
# 新开一个窗口，通过执行js来新开一个窗口
# js = 'window.open("https://www.sogou.com");'
# browser.execute_script(js)



# for handle in handles:  # 切换窗口（切换到搜狗）
#     if handle != browser.current_window_handle:
#         print('switch to ', handle)
#         browser.switch_to.window(handle)
#         print(browser.current_window_handle)  # 输出当前窗口句柄（搜狗）
#         break

# browser.close()  # 关闭当前窗口（搜狗）
# browser.switch_to.window(handles[0])  # 切换回百度窗口

# time.sleep(10)
