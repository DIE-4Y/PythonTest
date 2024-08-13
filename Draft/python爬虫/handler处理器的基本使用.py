import urllib.request

url = 'https://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

request = urllib.request.Request(url=url, headers=headers)

""" 使用handler一共三步>> """
""" （1）获取handler对象 """
handler = urllib.request.HTTPHandler()

""" （2）获取opener对象 """
opener = urllib.request.build_opener(handler)

""" （3）调用open方法 """
# open方法相当于urlopen
response = opener.open(request)
content = response.read().decode('utf-8')

print(content)
