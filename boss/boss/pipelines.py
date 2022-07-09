# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import codecs
from scrapy.linkextractors import LinkExtractor
from scrapy import signals
import os


class BossPipeline(object):
    """
        导出CSV格式
    """
    def __init__(self):
        self.file = {}
        self.csvpath = os.path.dirname(__file__) + '/spiders/output'
        self.exporter = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        """
        当蜘蛛启动时自动执行
        :param spider:
        :return:
        """
        f = open('%s/%s_items.csv' % (self.csvpath, spider.name), 'a')  # r只读, w可写, a追加
        self.file[spider] = f
        self.exporter = LinkExtractor(f)
        self.exporter.fields_to_export = spider.settings['FIELDS_TO_EXPORT']
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        """
        蜘蛛每yield一个item,这个方法执行一次
        :param item:
        :param spider:
        :return:
        """
        self.exporter.export_item(item)
        return item

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        f = self.file.pop(spider)
        f.close()


class JSONPipeline(object):
    """
        导出JSON格式
    """
    def __init__(self):
        self.file = None
        self.csvpath = os.path.dirname(__file__) + '/spiders/output'

    def process_item(self, item, spider):
        self.file = codecs.open('%s/%s_items.json' % (self.csvpath, spider.name), 'a', encoding='utf-8')
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        # return item

    def spider_closed(self, spider):
        self.file.close()
