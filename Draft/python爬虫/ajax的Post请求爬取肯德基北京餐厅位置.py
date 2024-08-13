import urllib.request
import urllib.parse

"""请求标头中含有 x-requested-with:XMLHttpRequest 的就表示是ajax请求"""

"""第一页"""
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
#
# data = {
# 'cname': '北京',
# 'pid': ,
# 'pageIndex': 1,
# 'pageSize': 10
# }

"""第二页"""


# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10


def get_request(page):
    base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    request = urllib.request.Request(url=base_url, data=data, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content, page):
    with open('KFC_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':

    start_page = int(input("请输入起始页数:>>"))
    end_page = int(input("请输入结束页数:>>"))

    for page in range(start_page, end_page + 1):
        # 请求对象定制
        request = get_request(page)
        # 模拟电脑发送请求 获取响应
        content = get_content(request)
        # 下载
        down_load(content, page)
        print(content)
