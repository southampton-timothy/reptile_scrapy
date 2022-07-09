import scrapy
from ..items import LearnItem


class Learn1Spider(scrapy.Spider):
    # 爬虫文件名称：就是爬虫源文件的一个唯一标识
    name = 'learn1'
    # 允许的域名：用来限定start_urls列表中哪些url可以进行请求发送
    # allowed_domains = ['www.xxx.com'] # 通常不使用
    # 起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ['https://shanghai.zbj.com/saas/f.html?']

    # 用作于数据解析：response参数表示的就是请求成功之后对应的响应对象
    # def parse(self, response):
    #     # 解析：八戒网公司名称+位置
    #     table = response.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div[1]/div")
    #     inf_list = []
    #     for company in table:  # 每一个服务商信息
    #         # xpath返回的是列表，但列表元素一定是selector类型的对象
    #         # extract可以将selector对象中data参数存储的字符串提取出来
    #         name = company.xpath(".//div/div/div/p/a/text()")[0].extract()
    #         price = company.xpath("./div/div/div[2]/div[2]/div[1]/span[1]/text()")[0].extract().strip('¥')
    #         # 列表调用extract之后，表示将列表中每一个selector对象中data对应的字符串提取出来
    #         title = company.xpath("./div/div/div[2]/div[2]/div[2]/p/a/text()").extract()
    #         title = '/'.join(title)
    #         location = company.xpath('.//div[1]/div[1]/div/span/@title')[0].extract()
    #         dic = {
    #             'name':name,
    #             'price':price,
    #             'title':title,
    #             'location':location
    #         }
    #         inf_list.append(dic)
    #     return inf_list

    def parse(self, response):
        # 解析：八戒网公司名称+位置
        table = response.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div[1]/div")
        inf_list = []
        for company in table:  # 每一个服务商信息
            # xpath返回的是列表，但列表元素一定是selector类型的对象
            # extract可以将selector对象中data参数存储的字符串提取出来
            name = company.xpath(".//div/div/div/p/a/text()")[0].extract()
            price = company.xpath("./div/div/div[2]/div[2]/div[1]/span[1]/text()")[0].extract().strip('¥')
            # 列表调用extract之后，表示将列表中每一个selector对象中data对应的字符串提取出来
            title = company.xpath("./div/div/div[2]/div[2]/div[2]/p/a/text()").extract()
            title = '/'.join(title)
            location = company.xpath('.//div[1]/div[1]/div/span/@title')[0].extract()
            item = LearnItem()
            item['name'] = name
            item['price'] = price
            item['title'] = title
            item['location'] = location

            yield item  # 将item提交给管道



