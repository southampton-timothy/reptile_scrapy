# Author: by tunan
# Date: 2022/3/31 8:36 PM
# Function: 认识UA伪装


# UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import requests

if __name__ == '__main__':
    # UA伪装：将对应的User-Agent伪装到一个字典中
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                     ' Chrome/100.0.4896.60 Safari/537.36'
    }
    url = 'https://www.sogou.com/web?'
    # 处理url携带的参数封装到字段中
    kw = input('enter a keyword:')
    param = {
        'query': kw
    }
    # 对制定对url发起的请求对应的url是携带参数的，并且请求过程中处理参数
    response = requests.get(url=url,params=param,headers=header)
    page_text = response.text
    filename = kw+'.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_text)
    print(filename,'保存完成')

    