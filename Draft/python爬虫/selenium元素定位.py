from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://baidu.com'
browser = webdriver.Edge()
browser.get(url)
# 获取网页源码
print(browser.page_source)
# 元素定位 根据id寻找对象
print(browser.find_element('id', value='su'))
# 根据xpath 获取对象
button = browser.find_element(by='xpath', value='//input[@id="su"]')
print(button)
# 根据标签名获取对象
button = browser.find_elements(By.TAG_NAME, 'input')
print(button)

