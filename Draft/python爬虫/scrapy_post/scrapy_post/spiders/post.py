import json

import scrapy


class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["fanyi.baidu.com"]
    start_urls = ["https://fanyi.baidu.com/sug"]

    def parse(self, response):
        pass

    """Post请求只能用start_url方法"""
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        data = {
            'kw': 'scrapy'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_2)

    # 调用parse_2获取Post访问内容
    def parse_2(self, response):
        content = response.text
        # ajax请求返回的是json数据
        obj = json.loads(content)
        print(obj)
