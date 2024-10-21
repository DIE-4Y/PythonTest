import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem

"""爬取当当网科幻小说指定页数的图片和小说名称"""


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.03.41.00.00.00.html"]

    base_url = 'https://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # 获取li标签
        li_list = response.xpath('//ul[@id="component_59"]/li')

        for li in li_list:

            # 获取图片
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            src = 'https:' + str(src)

            # 获取名称
            alt = li.xpath('.//img/@alt').extract_first()

            # 获取价格
            price = li.xpath('.//span[@class="search_now_price"]/text()').extract_first()

            # 用items里定义的对象保存 需要先把settings里解注释 并导入items里的对象
            book = ScrapyDangdangItem(src=src, alt=alt, price=price)

            # 获取一个对象就用yield保存一个到管道
            yield book


        if self.page < 3:
            self.page += 1
            url = self.base_url + str(self.page) + '-cp01.03.41.00.00.00.html'

            # yield 调用parse函数 scrapy.Request()就是yield的Get请求
            yield scrapy.Request(url=url, callback=self.parse)
