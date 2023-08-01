import requests

url='https://movie.douban.com/j/chart/top_list'

headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'}


def main():

        i=int(input("请输入你想查找的豆瓣喜剧排行名次: "))
        i = i - 1
        params={
             'type': '24',
            'interval_id': '100:90',
            'action': '',
            'start': f'{i}',
            'limit': '20'
        }


        resp=requests.get(url=url,headers=headers,params=params)
        print(resp)
        print(resp.json())
        resp.close()



if __name__ == '__main__':

  main()
