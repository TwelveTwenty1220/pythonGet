
#爬取一页的代码，利用线程池，同时爬取多页的数据
#一页代码
#线程池
#数据写入
import requests
import csv
import re
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

url='http://www.xinfadi.com.cn/getPriceData.html' #都是固定的，只不过参数不一样


file=open('data.csv','w',newline='',encoding='utf-8')
csv_writer=csv.writer(file)
obj=re.compile(r'.*京.*')

def download(i):
    params = {
        'limit': '20',
        'current': f'{i}',
        'pubDateStartTime': '',
        'pubDateEndTime': '',
        'prodPcatid': '',
        'prodCatid': '',
        'prodName': ''
    }
    resp=requests.post(url=url,params=params)
    dic=resp.json()
    for i in range(0,20):
        proName = dic['list'][i]['prodName']
        lowPrice= dic['list'][i]['lowPrice']
        highPrice=dic['list'][i]['highPrice']
        avgPrice=dic['list'][i]['avgPrice']
        pubDate= dic['list'][i]['pubDate']
        location=dic['list'][i]['place']

        list=[proName,lowPrice,highPrice,avgPrice,pubDate,location]
        csv_writer.writerow(list)
    resp.close()

if __name__ == '__main__':
    print('开始爬取')
    with ThreadPoolExecutor(100) as t:
        for i in tqdm(range(1,25258+1),desc='爬取蔬菜价格中'):
            t.submit(download,i)

    print('爬取完毕')






