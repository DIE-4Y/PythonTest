import urllib.request
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyMoviePipeline:
    def open_spider(self, spider):
        self.fp = open('movie.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()

class imgDownloadPipeline:
    def process_item(self, item, spider):
        urllib.request.urlretrieve(item['url'], filename='movie/'+item['name']+'.jpg')
        return item
