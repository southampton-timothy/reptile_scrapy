import scrapy


class HouseSpider(scrapy.Spider):
    name = 'house'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sh.58.com/songnansh/ershoufang/e10y3/?PGTID=0d200001-0000-2be4-7e6b-2d4ce08819ce&ClickID=1']

    def parse(self, response):
        house_list = response.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]')
        print(house_list)
        for house in house_list:
            house_name = house.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/'
                                     'div[1]/a/div[2]/div[1]/div[1]/h3/text()').extract()
            print(house_name)


