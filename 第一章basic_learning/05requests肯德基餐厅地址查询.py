# Author: by tunan
# Date: 2022/4/5 3:39 PM
# Function:

import requests
import json

if __name__ == '__main__':
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    addr = input('enter an address:')
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/100.0.4896.60 Safari/537.36'}
    for i in range(1, 7):
        data = {
            'cname': '',
            'pid': '',
            'keyword': addr,
            'pageIndex': i,
            'pageSize': 10
        }
        response = requests.post(url=post_url, data=data, headers=header)
        text = response.text
        filename = addr + '.txt'
        f = open(filename, 'a+', encoding='utf-8')
        json.dump(text, fp=f, ensure_ascii=False)
        f.close()
    print('finished')