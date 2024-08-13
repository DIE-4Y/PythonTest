import urllib.request

# url代表要访问的地址
url = 'http://www.baidu.com'

# 向浏览器发送请求
response = urllib.request.urlopen(url)

# content接受数据
"""read返回的是二进制数据，需要解码"""
# 每次读一个字节
content = response.read()
# # 每次只读一行
# content = response.readline()
# # 一行一行地读直到读完
# content = response.readlines()

"""获取状态码"""
# 如果得到的是200，则数据正确
# 返回的是500，则数据错误
# 返回的是404，则没找到网页
status = response.getcode()
newurl = response.geturl()
header = response.getheaders()

# 内容解码
content = content.decode('utf-8')

print(type(content))
print(content)