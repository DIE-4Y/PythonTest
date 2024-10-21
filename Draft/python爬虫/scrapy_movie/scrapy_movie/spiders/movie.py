import scrapy
from scrapy_movie.items import ScrapyMovieItem


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.dyttcn.com"]
    start_urls = ["https://www.dyttcn.com/kehuanpian/list_5_1.html"]

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//a[3]')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'https://www.dyttcn.com/' + str(href)

            # 对链接进行访问 用自定义的parse_2
            # 用meta向自创函数传递数据
            yield scrapy.Request(url=url, callback=self.parse_2, meta={'name': name})

    def parse_2(self, response):
        img_src = response.xpath('//div[@id="Zoom"]//img/@src[1]').extract_first()
        name = response.meta['name']
        movie = ScrapyMovieItem(name=name, url=img_src)
        yield movie