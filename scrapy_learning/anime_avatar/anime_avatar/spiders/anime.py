import scrapy


class AnimeSpider(scrapy.Spider):
    name = 'anime'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://mip.woyaogexing.com/touxiang/z/ktnan/']

    # 生成一个通用的url模版(不可变)
    url = 'https://mip.woyaogexing.com/touxiang/z/ktnan/index_%d.html'
    page_num = 2

    def parse(self, response):
        ul_list = response.xpath('/html/body/ul')
        for ul in ul_list:
            img_name = ul.xpath('./li/div/div[1]/a/div[2]/text()').extract()
            print(self.page_num, img_name)

        if self.page_num <= 17:
            new_url = format(self.url % self.page_num)
            # 手动请求发送, callback回调函数是专门用作于数据解析的
            yield scrapy.Request(url=new_url, callback=self.parse)
            self.page_num += 1


