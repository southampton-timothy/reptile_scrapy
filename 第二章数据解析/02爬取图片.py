# Author: by tunan
# Date: 2022/4/14 21:36
# Function: 爬取贴吧中糗图板块下所有的糗图
import re
import os
import requests

if __name__ == '__main__':
    # 创建文件夹，保存所有的图片
    if not os.path.exists('./imglibs'):
        os.mkdir('./imglibs')

    url = 'https://tieba.baidu.com/p/4222916093'

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/100.0.4896.60 Safari/537.36'
    }

    # 使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url, headers=header).text
    print(page_text)

    # 使用聚焦爬虫将页面中所有的糗图进行解析/提取
    ex = '<img class="BDE_Image" (.*?) src="(.*?)" size=(.*?)>'
    img_src_list = re.findall(ex, page_text, re.S)
    print(len(img_src_list))
    for src in img_src_list:
        # 请求图片的二进制数据
        img_data = requests.get(url=src[1], headers=header).content
        # 生成图片名称
        img_name = src[1].split('/')[-1]
        imgPath = './imglibs/'+img_name
        with open (imgPath, 'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！')

































    # # 如何爬取图片数据
    # url = 'https://pic.baike.soso.com/p/20140505/20140505164016-1669171701.jpg'
    # # content返回的是二进制形式的图片数据 text(字符串) json() 对象形式
    # img_data = requests.get(url=url).content
    # with open('./jiongtu.jpg','wb') as fp:
    #     fp.write(img_data)
    
