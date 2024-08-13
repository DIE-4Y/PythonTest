import urllib.request
from lxml import etree


def get_request(page):
    url = ''
    headers = {
        'cookie': 'ASP.NET_SessionId = zmbs1rsyvyipbca35elw0ctt',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/xingkongtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/xingkongtupian_' + str(page) + '.html'
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    # 网页上显示的数据不一定是爬取到的数据 需要根据爬取到的网页源码进行解析
    name_list = tree.xpath('//div[@class="item"]/img/@alt')
    src_list = tree.xpath('//div[@class="item"]/img/@data-original')

    # 先创建一个站长之家图片文件夹 以存放图片
    for i in range(len(name_list)):
        file_name = './站长之家图片/'+name_list[i] + '.jpg'
        url = 'http:' + src_list[i]
        urllib.request.urlretrieve(url, file_name)


# # 初始url
# url1 = 'https://sc.chinaz.com/tupian/xingkongtupian.html'
# # 第二页url
# url2 = 'https://sc.chinaz.com/tupian/xingkongtupian_2.html'

if __name__ == '__main__':

    start_page = int(input("请输入起始页数"))
    end_page = int(input("请输入结束页数"))
    for page in range(start_page, end_page + 1):
        # 请求对象定制
        request = get_request(page)
        # 模拟发送请求获取源码
        content = get_content(request)
        # 解析并下载下载
        down_load(content)
