# Author: by tunan
# Date: 2022/6/5 14:32
# Function: 1.拿到主页面的源代码，提取子页面链接地址，href 2.通过href找到图片的下载内容 3.下载图片

import requests
import os
from bs4 import BeautifulSoup

# 创建文件夹，保存所有的图片
if not os.path.exists("./imgurls"):
    os.mkdir("./imgurls")

url = "https://www.umei.cc/bizhitupian/xiaoqingxinbizhi/"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.60 Safari/537.36"
}

resp = requests.get(url=url, headers=headers)
resp.encoding = 'utf-8'
page_content = resp.text

# 把页面源代码交给beautifulsoup进行处理，生成bs对象
main_page = BeautifulSoup(page_content, "html.parser")  # 指定html解析器
# 从bs对象中查找数据 find(标签，属性=值) and find_all
table = main_page.find("div", class_="swiper-wrapper after")  # class是python的关键字，所以用下标区分，第一次缩小范围
picture_list = table.find_all("a")
for p in picture_list:
    part = p.get("href")  # 直接通过get就可以拿到属性的值
    pic_url = "https://www.umei.cc/" + part
    # 获得子页面的源代码
    result = requests.get(url=pic_url, headers=headers)
    result.encoding = 'utf-8'
    pic_page = BeautifulSoup(result.text, "html.parser")
    picture = pic_page.find('img')
    src = picture.get('src')
    # 下载图片
    img_resp = requests.get(src)
    #  img_resp.content  # 获取图片的字节形式(二进制)
    img_name = src.split("/")[-1]
    with open('./imgurls/'+img_name, mode='wb') as f:
        f.write(img_resp.content)  # 图片内容写入文件
    print(img_name, "下载成功!")
