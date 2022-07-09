# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class LearnPipeline(object):
    fp = None

    # 写父类的一个方法，该方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('开始爬虫......')
        self.fp = open('./company.txt', mode='w', encoding='utf-8')

    # 专门用来处理item类型对象，该方法可以接受爬虫文件提交过来的item对象，该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        name = item['name']
        price = item['price']
        title = item['title']
        location = item['location']
        self.fp.write(name + '-' + price + '-' + title + '-' + location + '\n')
        return item  # item会传递给下一个即将被执行的管道类

    def close_spider(self, spider):
        print('结束爬虫......')
        self.fp.close()


# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class MysqlPipeline(object):
    _coon = None
    cursor = None

    def open_spider(self, spider):
        self._coon = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='scrapy_learning')

    def process_item(self, item, spider):
        self.cursor = self._coon.cursor()
        try:
            self.cursor.execute(
                'insert into saas_company(name,price,title,location) values("%s","%d","%s","%s")' %
                (item["name"], int(
                    item["price"]), item["title"], item["location"]))
            self._coon.commit()
        except Exception as e:
            print(e)
            self._coon.rollback()
        return item  # 传递item到下一个管道类

    def close_spider(self, spider):
        self.cursor.close()
        self._coon.close()

# 爬虫文件提交的item类型的对象最终会提交给哪一个管道类？先执行优先级高的
