import scrapy


class CarhomeSpider(scrapy.Spider):
    name = "carhome"
    allowed_domains = ["car.autohome.com.cn"]
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        print('==========')
        bmw_list = response.xpath('//div[@class="list-cont-main"]/div/a/text()')
        price_list = response.xpath('//span[@class="font-arial"]/text()')
        # print(type(bmw_list))
        # print(type(price_list.extract()))
        for i in range(len(bmw_list)):
            print(bmw_list[i].extract(), price_list[i].extract())
