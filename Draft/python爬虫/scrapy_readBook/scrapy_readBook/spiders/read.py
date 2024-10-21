import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readBook.items import ScrapyReadbookItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/guoxue/1011_1.html"]

    # 修改allow的路径为正则表达式
    # follow会一直向后寻找 直到结束
    rules = (Rule(LinkExtractor(allow=r"/guoxue/1011_\d+\.html"),
                  callback="parse_item",
                  follow=False),)

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        a_list = response.xpath('//div[@class="book-info"]//a')
        for a in a_list:
            name = a.xpath("./text()").extract_first()
            src = a.xpath("./@href").extract_first()
            url = 'https://www.dushu.com' + str(src)
            book = ScrapyReadbookItem(name=name, url=url)

            yield book


        return item
