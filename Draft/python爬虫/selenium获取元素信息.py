from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'Https://www.baidu.com'
browser = webdriver.Edge()
browser.get(url)

element = browser.find_element(By.ID, 'su')
# 获取元素属性
print(element.get_attribute('class'))
# 获取标签名字
print(element.tag_name)
# 获取元素文本
link = browser.find_element(By.LINK_TEXT, '新闻')
print(link.text)

