import scrapy
from ..items import ImgsproItem


class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        pic_list = response.xpath(
            '//*[@id="container"]/div/div/a/img/@src').extract()
        for pic in pic_list:
            # 注意：网页是否使用伪属性
            pic_url = 'https:' + pic
            item = ImgsproItem()
            item['src'] = pic_url
            yield item
