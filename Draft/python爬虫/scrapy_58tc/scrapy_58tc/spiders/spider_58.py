import scrapy


class Spider58Spider(scrapy.Spider):
    name = "spider_58"
    allowed_domains = ["cn.58.com"]
    start_urls = ["https://cn.58.com/quanzhizhaopin/"]

    def parse(self, response):
        # print("========================")
        # # 获取网页源码
        # content = response.text
        # print(content)
        #
        # # 二进制源码
        # byte_html = response.body
        # print(byte_html)
        #
        # # 无需导包直接使用
        # address_list = response.xpath('//ul[@id="list_con"]//span[@class="address"]')
        # print(address_list)
        #
        # # extract()提取selector对象的内容
        # span =  response.xpath('//ul[@id="list_con"]//span[@class="address"]')[0]
        # print(span.extract())
        #
        # # extract_first()提取列表的第一个内容
        # address = address_list.extract_first
        # print(address)
        pass