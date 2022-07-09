# Author: by tunan
# Date: 2022/4/4 2:12 PM
# Function:

import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': 0,
        'limit': 20
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/100.0.4896.60 Safari/537.36'}

    response = requests.get(url=url, params=param,headers=header)

    list_data = response.json()

    f = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=f,ensure_ascii=False)
    f.close()
    print('finished')
