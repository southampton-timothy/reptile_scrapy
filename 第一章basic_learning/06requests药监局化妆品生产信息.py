# Author: by tunan
# Date: 2022/4/7 3:46 PM
# Function:动态加载数据
import json

import requests

if __name__ == '__main__':
    # 批量获取不同企业的id
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []  # 存储企业的id
    all_data_list = []  # 存储企业的详情数据
    # 参数的封装
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/100.0.4896.60 Safari/537.36'}
    for page in range(1,388):
        data = {
            'on': 'true',
            'page': page,
            'pageSize': 15,
            'productName': '',
            'conditionType': 1,
            'applyname': '',
            'applysn': ''
        }
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/100.0.4896.60 Safari/537.36'}
        json_id = requests.post(url=url, data=data, headers=header).json()
        for dic in json_id['list']:
            id_list.append(dic['ID'])

    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=url, headers=header, data=data).json()
        all_data_list.append(detail_json)
    # 持久化存储
    f = open('./allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=f, ensure_ascii=False)
    f.close()
    print('finished!')
