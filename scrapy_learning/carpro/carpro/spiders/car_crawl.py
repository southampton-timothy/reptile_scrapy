import scrapy
from ..items import CarproItem


class CarCrawlSpider(scrapy.Spider):
    name = 'car_crawl'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.dongchedi.com/auto/series/score/4258-x-x-x-x-x-x']

    url = 'https://www.dongchedi.com/auto/series/score/4258-x-S0-x-x-x-%d'
    page_num = 2

    def parse(self, response):
        table = response.xpath('//*[@id="__next"]/div[1]/div[2]/div[3]/section/section[1]/article')
        for car in table:
            name = car.xpath('.//section/header/h2/span[2]/text()')[0].extract()
            comment = car.xpath('.//section/p/text()')[0].extract()
            mark = car.xpath('.//section/header/a/span[1]/text()')[0].extract()
            item = CarproItem()
            item['name'] = name
            item['comment'] = comment
            item['mark'] = mark
            yield item

        if self.page_num <= 6:
            new_url = format(self.url % self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)
            self.page_num += 1




