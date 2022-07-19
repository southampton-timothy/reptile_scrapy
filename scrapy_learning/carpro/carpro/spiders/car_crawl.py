import scrapy
from ..items import CarproItem


class CarCrawlSpider(scrapy.Spider):

    name = 'car_crawl'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.dongchedi.com/auto/series/score/4258-x-S0-x-x-1-1']  # id4
    url = 'https://www.dongchedi.com/auto/series/score/4258-x-S0-x-x-1-%d'  # id4

    # start_urls = ['https://www.dongchedi.com/auto/series/score/352-x-S0-x-x-1-1']  # 昂科威
    # url = 'https://www.dongchedi.com/auto/series/score/352-x-S0-x-x-1-%d'  # 昂科威

    # start_urls = ['https://www.dongchedi.com/auto/series/score/4540-x-S0-x-x-1-1']  # 宋PLUS EV
    # url = 'https://www.dongchedi.com/auto/series/score/4540-x-S0-x-x-1-%d'  # 宋PLUS EV

    # start_urls = ['https://www.dongchedi.com/auto/series/score/4814-x-S0-x-x-1-1']  # AION Y
    # url = 'https://www.dongchedi.com/auto/series/score/4814-x-S0-x-x-1-%d'  # AION Y

    # start_urls = ['https://www.dongchedi.com/auto/series/score/4380-x-S0-x-x-1-1']  # 几何C
    # url = 'https://www.dongchedi.com/auto/series/score/4380-x-S0-x-x-1-%d'  # 几何C

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

        max_page = response.xpath('//*[@id="__next"]/div[1]/div[2]/div[3]/section/section[1]/div[2]/ul/li/a/span/text()')[4].extract()

        if self.page_num <= int(max_page):
            new_url = format(self.url % self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)
            self.page_num += 1




