# Author: by tunan
# Date: 2022/3/31 8:18 PM
# Function: 爬取搜狗首页的页面数据

import requests

if __name__ == '__main__':
    # 确定url
    url = 'https://www.sogou.com/'
    # 发起请求
    # get方法返回一个响应对象
    response = requests.get(url=url)
    # 获取响应数据
    page_text = response.text
    print(page_text)
    # 持久化存储
    with open('./sogou.html','w',encoding='utf-8') as f:
        f.write(page_text)
    print('爬取数据结束')