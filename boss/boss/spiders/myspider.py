# Author: by tunan
# Date: 2022/3/31 1:43 PM
# Function:
import scrapy

from boss.boss.items import BossItem


class BossSpider(scrapy.Spider):
    name = "boss"

    # 设定域名
    allowed_domains = ["www.zhipin.com"]

    def start_requests(self):
        """
        设置第一个爬取的URL,即boss直聘第一页
        """
        urls = [
            'https://www.zhipin.com/c101210100/h_101210100/?page=1&ka=page-1',
        ]

        # 每次yield都会调用下载器中间件,即 mySpiderMiddleware.SeleniumMiddleware
        # 这里由selenium进行动态抓取招聘信息
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        初始化Item：Boss
        :param response:
        :return:
        """
        boss = BossItem()

        # 利用xpath筛选想要爬取的数据
        for box in response.xpath('//div[@class="job-primary"]'):
            boss['position'] = box.xpath('.//div[@class="job-title"]/text()').extract()[0]
            boss['salary'] = box.xpath('.//span[@class="red"]/text()').extract()[0]
            boss['addr'] = box.xpath('.//p[1]/text()').extract()[0]
            boss['years'] = box.xpath('.//p[1]/text()').extract()[1]
            boss['education'] = box.xpath('.//p[1]/text()').extract()[2]
            boss['company'] = box.xpath('.//div[@class="info-company"]//a/text()').extract()[0]
            boss['industry'] = box.xpath('.//p[1]//text()').extract()[3]
            boss['nature'] = box.xpath('.//p[1]//text()').extract()[4]
            boss['scale'] = box.xpath('.//p[1]//text()').extract()[5]
            boss['publisher'] = box.xpath('.//div[@class="info-publis"]//h3/text()').extract()[0]
            boss['publisherPosition'] = box.xpath('.//div[@class="info-publis"]//h3/text()').extract()[1]
            boss['publishDateDesc'] = box.xpath('.//div[@class="info-publis"]//p/text()').extract()[0]

            # 将Item：BossItem传递给Spider中间件,由它进行数据清洗（去空,去重）等操作
            # 每次yield都将调用SpiderMiddleware, 这里是 mySpiderMiddleware.MyFirstSpiderMiddleware
            yield boss

        # 分页
        url = response.xpath('//div[@class="page"]//a[@class="next"]/@href').extract()
        if url:
            page = 'https://www.zhipin.com' + url[0]
            yield scrapy.Request(page, callback=self.parse)


if __name__ == '__main__':
    scrapy.spiders.CrawlSpider


    process = CrawlerProcess(get_project_settings())
    process.crawl(mySpider)
    process.start()
