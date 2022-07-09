# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    """
    定义需要爬取的字段和类型
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    position = scrapy.Field(serializer=str)  # 招聘职位
    salary = scrapy.Field(serializer=str)  # 薪资
    addr = scrapy.Field(serializer=str)  # 工作地址
    years = scrapy.Field(serializer=str)  # 工作年限
    education = scrapy.Field(serializer=str)  # 学历
    company = scrapy.Field(serializer=str)  # 招聘公司
    industry = scrapy.Field(serializer=str)  # 行业
    nature = scrapy.Field(serializer=str)  # 性质：是否上市
    scale = scrapy.Field(serializer=str)  # 规模：人数
    publisher = scrapy.Field(serializer=str)  # 招牌者
    publisherPosition = scrapy.Field(serializer=str)  # 招聘者岗位
    publishDateDesc = scrapy.Field(serializer=str)  # 发布时间

