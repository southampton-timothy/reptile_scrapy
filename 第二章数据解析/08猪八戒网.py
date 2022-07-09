# Author: by tunan
# Date: 2022/6/7 10:20
# Function:1.提取页面源代码 2.提取和解析数据
import csv

import requests
from lxml import etree
import pandas as pd

url = "https://shanghai.zbj.com/saas/f.html?"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.60 Safari/537.36"
}

resp = requests.get(url=url, headers=headers)
# 解析网页
html = etree.HTML(resp.text)

name_list = html.xpath(".//div[1]/div[1]/p/a/text()")
location_list = html.xpath(".//div[1]/div[1]/div/span/text()")
price_list = html.xpath(".//div[2]/div[2]/div[1]/span[1]/text()")
product_list = html.xpath(".//div[2]/div[2]/div[2]/p/a/text()")[1]
print(len(product_list))

print(product_list)


#  #  范围从大到小缩小至每个服务商
# table = html.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div[1]/div")
# inf_list = []
# for item in table:  # 每一个服务商信息
#     name = item.xpath(".//div/div/div/p/a/text()")
#     name = name[0]
#     price = item.xpath("./div/div/div[2]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
#     title = item.xpath("./div/div/div[2]/div[2]/div[2]/p/a/text()")
#     title = '/'.join(title)
#     location = item.xpath('.//div[1]/div[1]/div/span/@title')[0]
#     inf_list.append([name, price, title, location])



