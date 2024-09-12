import urllib.request
from lxml import etree

base_url = 'https://wyw.hwxnet.com/article/'
start_url = 'https://wyw.hwxnet.com/article/24.html'


def get_response(page):
    headers = {
        'cookie': 'JSESSIONID=9772D8135E6F4128A8ABEF8E51282710',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }
    url = 'https://wyw.hwxnet.com/article/' + str(page) + '.html'
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    resposne = urllib.request.urlopen(request)
    content = resposne.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    p_list = tree.xpath('//div[@class="topics_con clearfix"]/p')[3:]
    for p in p_list:
        word = p.xpath('.//strong/text()')[0]
        mean = p.xpath('./span/text()')
        print(word, mean)

    # with open('hanwenxue.html', 'w', encoding='utf-8') as fp:
    #     fp.write(content)


if __name__ == '__main__':

    start_page = 24
    end_page = 24
    for page in range(start_page, end_page + 1):
        request = get_response(page)
        content = get_content(request)
        down_load(content)
