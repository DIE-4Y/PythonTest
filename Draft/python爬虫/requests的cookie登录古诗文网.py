import requests
from lxml import etree

login_url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# (1) 获取可变数据
login_response = requests.get(url=login_url, headers=headers)
login_content = login_response.text
tree = etree.HTML(login_content)

view_state = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
view_state_generator = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]

# (2) 获取验证码图片
src = tree.xpath('//img[@id="imgCode"]/@src')[0]
code_url = 'http://www.gushiwen.cn' + src

"""由于进行了两次访问 第一次访问和第二次访问给出的验证码不同 所以会导致错误 用requests.session解决"""
"""session能让请求都视为一次 不能直接打印code_url 这样进去相当于另外访问了一次 会导致验证码出错"""

session = requests.session()
reseponse_code = session.get(url=code_url, headers=headers)
# 由于下载的是图片 只能用content 且保存文件时要用 wb 以字节写入
content_code = reseponse_code.content
with open('code.jpg', 'wb')as fp:
    fp.write(content_code)
code = input("请输入验证码:>>")


# (3) 登录
data = {
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
    'email': '18975238480',
    'pwd': 'chenshanquan8772',
    'code': code,
    'denglu': '登录',
}
response = session.post(login_url, data=data, headers=headers)
content = response.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
