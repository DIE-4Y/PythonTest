import requests

# requests可省略路径中的？
url = 'https://www.baidu.com/s?'

data = {
    'wd': '北京'
}


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# requests无需对数据进行编码 可直接传递
# 无需请求对象定制
response = requests.get(url, params=data, headers=headers)
content = response.text
print(content)
