import requests  #请求访问页面
import re   #正则表达
import csv

headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'}


def extract_data(url,index):

    resp=requests.get(url=url,headers=headers)
    html_content=resp.text

#解析数据
    obj=re.compile(r'</li>.*?<span class="title">(?P<name>.*?)</span>'
               r'.*?<p class="">.*?:(?P<director>.*?)&nbsp?.*?'
               r'<br>(?P<year>.*?)&nbsp.*?average">(?P<score>.*?)</span>'
               r'.*?content="10.0"></span>.*?<span>(?P<number>.*?)人评价</span>',re.S)

    result=obj.finditer(html_content)

    csv_writer=csv.writer(f)

    for i in result:
      list1=i.group('director').split()
      dic=i.groupdict()
      if len(list1)==3:
        dic['director']=f'{list1[0]} {list1[1]+list1[2]}'
      else :
        dic['director']=f'{list1[0]} {list1[1]}'
      dic['year']=dic['year'].strip()
      dic['number']=dic['number']+'人'
      dic['index']=index
      csv_writer.writerow(dic.values())

    resp.close()

if __name__=='__main__':
    i=0
    f = open('data.csv', mode='a', encoding='utf-8', newline='')
    index=1
    while(i<=225):
        url = f'https://movie.douban.com/top250?start={i}&filter='  #https://movie.douban.com/top250?start=25&filter=
        extract_data(url,index)
        i+=25
        index+=1
    f.close()
    print('over!')

    numbers=0
    f=open('data.csv', mode='r', encoding='utf-8')
    for i in f :
        numbers+=1

    print(numbers)
