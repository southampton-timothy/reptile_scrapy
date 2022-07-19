# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas as pd


class CarproPipeline:
    fp = None
    inf_list = []

    def open_spider(self, spider):
        print('beginning>>>>>>>>>>>>')

    def process_item(self, item, spider):

        name = item['name']
        comment = item['comment']
        mark = item['mark']
        self.inf_list.append({'name':name, 'comment':comment,'mark':mark })
        # inf_df = pd.DataFrame(self.inf_list)
        # inf_df.to_excel('./id4_comment.xlsx')
        # inf_df.to_csv('./id4_comment.csv')
        return item

    def close_spider(self, spider):
        print('end>>>>>>>>>>>>>>>>')