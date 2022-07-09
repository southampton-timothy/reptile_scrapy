# Author: by tunan
# Date: 2022/5/30 21:43
# Function:获取盗版天堂2022新片精品

# 1.定位到2022新片精品
# 2.从2022新片精品中提取到子页面到链接地址
# 3.请求子页面到链接地址，获取想要到下载地址

import re
import requests
import time

domain = "https://m.dytt8.net/index2.htm"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/100.0.4896.60 Safari/537.36"}

resp = requests.get(url=domain, headers=headers)
resp.encoding = "gbk"  # 指定字符集
page_content = resp.text

# 获取2022新片精品的下载链接和名称
# parse website domain
obj = re.compile(r"最新电影下载</a>]<a href='(?P<weblink>.*?)'>(?P<name>.*?)</a><br/>", re.S)
obj2 = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?<br /><br /><br /><a target="_blank" href="(?P<download>.*?)">'
                  r'<strong>', re.S)

#
result = obj.finditer(page_content)

list = []
for it in result:
    dic = it.groupdict()
    dic['weblink'] = "https://m.dytt8.net"+dic['weblink']
    list.append(dic)

for d in list:
    url = d['weblink']
    resp2 = requests.get(url=url, headers=headers)  # verify变量用于是否ssh验证
    resp2.encoding = "gbk"
    film_content = resp2.text
    result2 = obj2.search(film_content)
    print(result2.group("movie", "download"))



