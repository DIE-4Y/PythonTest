import urllib.parse
import urllib.request

"""GET请求爬取豆瓣任意页数 用封装函数正规实现"""

"""请求对象定制函数的封装"""
def get_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': 20*(page-1),
        'limit': 20
    }
    url = base_url + urllib.parse.urlencode(data)

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    request = urllib.request.Request(url=url, headers=headers)

    return request

"""发送请求获取数据函数的封装"""
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

"""爬取内容函数的封装"""
def get_file(content, page):
    with open('douban_'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)



if __name__ == '__main__':
    start_page = int(input('请输入起始页数>>:'))
    end_page = int(input('请输入结束页数>>:'))
    for page in range(start_page,end_page+1):
        # 请求对象定制
        request = get_request(page)
        # 模拟电脑发送请求 接受响应 获取内容
        content = get_content(request)
        # 下载数据
        get_file(content, page)
