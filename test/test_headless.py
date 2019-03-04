from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# time.sleep(1)
# # 此行代码用来定位当前页面
# current = browser.current_window_handle
# browser.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[4]/h3/a").click()
# time.sleep(3)
# browser.quit()

chrome_options = Options()
chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://www.baidu.com')
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(1)
browser.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[4]/h3/a").click()
time.sleep(1)
html = browser.find_element_by_xpath("/html").get_attribute("outerHTML")
file = open('index.html', mode='w', encoding='utf-8')
file.write(html)
file.close()
browser.quit()
