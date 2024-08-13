import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}

# 将字典用urlencode转化为Unicode编码
new_data = urllib.parse.urlencode(data)

# 请求对象制订
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 网页地址拼接
new_url = base_url + new_data
# print(new_url)

# 发送请求
req = urllib.request.Request(url=new_url, headers=headers)
response = urllib.request.urlopen(req)

# 获取内容
content = response.read().decode('utf-8')
print(content)

