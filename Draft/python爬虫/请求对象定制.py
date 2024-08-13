import urllib.request

url = 'https://www.baidu.com'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}
# urlopen不能穿字典，只能用request传递
# request要把headers对应的传入，由于中间有个data，必须用关键字传参
request = urllib.request.Request(headers=headers, url=url)

# 使用了request伪装，就不再传url
response = urllib.request.urlopen(request)
content = response.read().decode('utf8')

print(type(content))
print(content)
