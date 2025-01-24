import json,requests,time
import pandas as pd
import re
# from bs4 import BeautifulSoup
import chardet
import datetime
import webbrowser

def search_video(search_name, pages):
    """
    search_name: str; 输入搜索关键词
    pages: int; 输入需要爬取的页数

    return:
    bvid_lst: list; 返回BV号列表
    up_lst: list; 返回up主名字列表；与BV号一一对应
    """
    bvid_lst = []
    up_lst = []
    for page in range(1, pages):
    #
        content = req.text
        print(content)
        print(req)
        pattern = re.compile('<a href="//www.bilibili.com/video/(.*?)\?from=search" title=')
        pattern_up = re.compile('<a href="//space.bilibili.com/.*?class="up-name">(.*?)</a></span>')
        lst_add = pattern.findall(content)
        up_lst_add = pattern_up.findall(content)
        tem = ['BV1GE411y7kE','BV1oW4y1B7re','BV1qq4y1472y','BV1db411v7jS','BV1us411S7jQ','BV1SE41167qy']
        while len(lst_add) == 0:
            # print(1)
            url = ('http://search.bilibili.com/all?keyword=' + search_name +
                   '&single_column=0&&order=dm&page=' + str(page))
            req = requests.get(url)
            content = req.text
            bvid_lst = tem
            # print(content)
            pattern = re.compile('<a href="//www.bilibili.com/video/(.*?)\?from=search" title=')
            # print(pattern)
            pattern_up = re.compile('<a href="//space.bilibili.com/.*?class="up-name">(.*?)</a></span>')
            # print(pattern_up)
            lst_add = pattern.findall(content)
            up_lst_add = pattern_up.findall(content)
            # print(lst_add)
        time.sleep(1)
        print('第{}页'.format(page), lst_add)
        up_lst.extend(up_lst_add)


    return bvid_lst, up_lst

