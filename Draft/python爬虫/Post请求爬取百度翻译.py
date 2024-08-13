import urllib.request
import urllib.parse
import json


# 请求地址
base_url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'spider'
}

# Post请求参数必须进行编码
# Post请求参数不会在地址上进行拼接 可放到请求对象中
# Post请求参数必须为字节型 就必须进行再编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象制订
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

req = urllib.request.Request(url=base_url, data=data, headers=headers)

response = urllib.request.urlopen(req)

content = response.read().decode('utf-8')

# 返回的是字符串 str-->json对象
obj = json.loads(content)
print(obj)
# print(type(obj))
