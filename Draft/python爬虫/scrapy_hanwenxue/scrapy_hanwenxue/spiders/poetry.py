import scrapy
from ..items import poetryItem


class PoetrySpider(scrapy.Spider):
    name = "poetry"
    allowed_domains = ["www.gushiwen.cn"]
    start_urls = ["https://www.gushiwen.cn/shiwens/"]

    def parse(self, response):
        div_list = response.xpath('//div[@id="leftZhankai"]//div[@class="cont"]')
        for div in div_list:
            """获取标题"""
            title = div.xpath('.//b/text()').extract_first()
            # print(title)

            """获取作者 朝代"""
            author_infor = div.xpath('.//p[@class="source"]/a/text()').extract()
            i = 0
            while i < len(author_infor):
                if author_infor[i] == '\n':
                    author_infor.pop(i)
                else:
                    i += 1
            author = str(author_infor[0][1:])
            dynasty = str(author_infor[-1])
            # print(author, dynasty)

            """获取内容"""
            content = div.xpath('.//div[@class="contson"]/text()').extract()
            for i in range(len(content)):
                content[i] = content[i].strip('\n')
            if content[0] == '':
                content = div.xpath('.//div[@class="contson"]/p/text()').extract()
            # print(content)

            yield poetryItem(title=title, author=author, dynasty=dynasty, content=content)

        href = response.xpath('//form[@id="FromPage"]//a[@class="amore"]/@href').extract_first()
        if href:
            url = 'https://www.gushiwen.cn' + str(href)
            yield scrapy.Request(url=url, callback=self.parse)
