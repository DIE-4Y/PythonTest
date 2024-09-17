import scrapy
from ..items import ScrapyHanwenxueItem

class HanSpider(scrapy.Spider):
    name = "han"
    allowed_domains = ["wyw.hwxnet.com"]
    start_urls = ["https://wyw.hwxnet.com/article/24.html"]

    base_url = "https://wyw.hwxnet.com/article/"
    page = 24
    def parse(self, response):
        p_list = response.xpath('//div[@class="topics_con clearfix"]/p')[3:]
        for p in p_list:
            word = str(p.xpath('.//strong/text()').extract_first())[-1:]
            # print(type(word), word)
            means = p.xpath('./span/text()')
            mean_list = []
            for mean in means:
                mean = mean.extract()[2:]
                mean_list.append(mean)
            # print(type(mean_list), mean_list)
            yield ScrapyHanwenxueItem(word=word, mean=mean_list)

        if self.page < 27:
            self.page += 1
            url = self.base_url + str(self.page) + ".html"
            yield scrapy.Request(url=url, callback=self.parse)
