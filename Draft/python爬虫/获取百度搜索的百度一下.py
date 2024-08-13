import urllib.request
from lxml import etree


url = 'https://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟电脑发送请求
response = urllib.request.urlopen(request)

# 获取源码
content = response.read().decode('utf-8')

# 解析
tree = etree.HTML(content)

# 获取数据的路径
result = tree.xpath('//span/input[@id="su"]/@value')

# xpath 返回的是列表
print(result[0])
