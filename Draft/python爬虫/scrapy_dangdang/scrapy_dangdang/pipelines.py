# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDangdangPipeline:
    # 用这个方法只打开一次文件
    def open_spider(self, spider):
        self.file = open('book.json', 'w', encoding='utf-8')

    # item就是yield后边传过来的对象
    # 写入的对象必须转化成字符串才能用w写入
    def process_item(self, item, spider):
        self.file.write(str(item))
        return item

    # 写入完文件后需关闭文件
    def close_spider(self, spider):
        self.file.close()

import urllib.request

"""多条管道同时下载"""
# （1） 定义管道类 并添加到settings里
# （2） 重写prcesss_item()方法 使用别的方法要导包

class pictureDownloadPipeline:
    def process_item(self, item, spider):
        urllib.request.urlretrieve(url=item['src'], filename='./books/'+item['alt']+'.jpg')
        return item
