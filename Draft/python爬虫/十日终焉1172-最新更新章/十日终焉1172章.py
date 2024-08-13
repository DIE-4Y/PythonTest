import requests
from lxml import etree

# 网站 https://m.hafuklxt.cc
"""自动爬取给出地址到最后章节的内容"""

def get_tree(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    response = requests.get(url=url, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    return tree

def get_next_url(tree):
    next_url = 'https://m.hafuklxt.cc' + tree.xpath('//a[@id="pb_next"]/@href')[0]
    return next_url

def down_load(tree):
    chapter_1 = tree.xpath('//div[@id="chaptercontent"]/text()')
    changed_chapter_1 = chapter_1[2:-2]
    # 一行一行地写入

    page = '第(1/3)页'
    if chapter_1[1] == page:
        # 如果是第每章一页 那么需额外下载列表中第1个元素 即标题
        with open('1172-1199.txt', 'a', encoding='utf-8') as file:
            file.write('\n'+chapter_1[0][2:]+'\n')
            for i in range(len(changed_chapter_1)):
                file.write('    ' + changed_chapter_1[i] + '\n')
    else:
        # 只下载主体内容
        with open('1172-1199.txt', 'a', encoding='utf-8') as file:
            for i in range(len(changed_chapter_1)):
                file.write('    ' + changed_chapter_1[i] + '\n')


# （1）请求1172章1/3页
if __name__ == '__main__':
    book_url = 'https://m.hafuklxt.cc/book/24110052/'
    # 1171章1/3页url
    # https://m.hafuklxt.cc/chapter/24110052/66013622.html
    # 1199章3/3页url
    # https://m.hafuklxt.cc/chapter/24110052/64644756_3.html
    now_url = 'https://m.hafuklxt.cc/chapter/24110052/66013622.html'

    next_url = ''

    while next_url != book_url:
        # 获取网页元素 以tree返回
        tree = get_tree(now_url)
        # 获取下一页网址
        next_url = get_next_url(tree)
        # 下载章节和内容
        down_load(tree)
        # 循环的必要条件
        now_url = next_url
