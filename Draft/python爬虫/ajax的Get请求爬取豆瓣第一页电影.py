import urllib.request
import urllib.parse

# 豆瓣电影第一页请求方式:GET
base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 请求对象制订
req = urllib.request.Request(url=base_url, headers=headers)

# 模拟电脑向网站发出请求获取数据
response = urllib.request.urlopen(req)

# 对内容解码
content = response.read().decode('utf-8')

# 存放到文件 open默认gbk编码格式 如果有中文就要指定编码格式 encoding='utf-8'
fp = open('douban.json', 'w', encoding='utf-8')
fp.write(content)
fp.close()

# 第二种保存文件的方法 无需关闭文件
with open('douban1.json', 'r', encoding='utf-8') as fp:
    fp.write(content)
