import requests

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'spider'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

response = requests.post(url=url, data=data, headers=headers)
content = response.text
print(type(content))
print(content)

print(type(response.json()))
print(response.json())
