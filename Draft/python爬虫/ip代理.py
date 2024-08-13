import urllib.request
import random

url = 'https://cn.bing.com/search?q=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)

# random实现请求池
proxiy_pool = [
    {'http': '202.101.213.218:20026'},
    {'http': '202.101.213.218:20026'},
    {'http': '202.101.213.218:20026'}
]

# ip代理
proxies = random.choice(proxiy_pool)

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

# 下载文件
with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
