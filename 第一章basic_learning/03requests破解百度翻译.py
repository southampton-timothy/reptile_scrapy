# Author: by tunan
# Date: 2022/4/2 4:02 PM
# Function: POST请求（携带参数）
import json

import requests

if __name__ == '__main__':
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.进行UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
        ' Chrome/100.0.4896.60 Safari/537.36'}
    # 3.post请求参数处理（同get）
    word = input('enter a word:')
    data = {
        'kw': word
    }
    # 4.发送请求
    response = requests.post(url=post_url, data=data, headers=header)
    # 5.获取响应数据:确认返回json类型对象
    dic_obj = response.json()
    # 6.永久化存储
    filename = word + '.json'
    f = open(filename, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=f, ensure_ascii=False)
    f.close()
    print('finished')
