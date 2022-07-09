# Author: by tunan
# Date: 2022/5/29 14:36
# Function: 通过re提取页面源代码里的有效信息

import re
import requests
import csv

for i in range(0, 250, 25):
    url = "https://movie.douban.com/top250?start="+str(i)
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.60 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)
    page_content = resp.text
    # 解析数据
    obj = re.compile(
        r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;/&nbsp.*?'
        r'property="v:average">(?P<mark>.*?)</span>.*?<span>(?P<comments_num>.*?)人评价</span>', re.S)
    # 开始匹配
    result = obj.finditer(page_content)
    f = open("data.csv", mode="a+")
    csvwriter = csv.writer(f)
    for it in result:
        dic = it.groupdict()
        dic["year"] = dic["year"].strip()
        csvwriter.writerow(dic.values())
    f.close()
    resp.close()
