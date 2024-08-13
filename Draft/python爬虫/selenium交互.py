import time

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://www.baidu.com'
browser = webdriver.Edge()
# 打开浏览器
browser.get(url)
# 睡眠2秒
time.sleep(2)
# 找到输入框
input = browser.find_element(by='id', value='kw')
# 输入周杰伦
input.send_keys('周杰伦')

time.sleep(2)
# 点击百度一下
button = browser.find_element(By.ID, value='su')
time.sleep(2)
# 下滑到底 固定写法
js_buttom = 'document.documentElement.scrollTop=1000000'
browser.execute_script(js_buttom)
time.sleep(3)
# 点击下一页
next = browser.find_element(By.XPATH, '//a[@class="n"]')
next.click()
time.sleep(2)

# 返回上一页
browser.back()
time.sleep(2)

# 向前
browser.forward()
time.sleep(2)

# 退出
browser.quit()
