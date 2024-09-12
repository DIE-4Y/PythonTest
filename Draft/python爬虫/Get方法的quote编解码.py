import urllib.request
import urllib.parse

# # 法1：直接使用ASCII码
# url = 'https://cn.bing.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6'

# 法2：用quote将汉语变为ASCII码
url = 'https://cn.bing.com/search?q='
original_name = '周杰伦'
changed_name = urllib.parse.quote(original_name)
url = url + changed_name

headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')
print(content)
