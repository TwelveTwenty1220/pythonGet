import requests
import re
import csv
import tqdm

#record dommain
domain='https://dytt89.com/'



def main(url):
    resp=requests.get(url=url)
    resp.encoding='gb2312'
    obj1=re.compile(r'2023必看热片.*?<ul>.*?</ul>',re.S)
    result1=obj1.finditer(resp.text)
    num=0
    list1=[]
    list2=[]
    for i in result1:
        list1=i.group()
    obj2=re.compile(r"<li><a href='(?P<href>.*?)'",re.S)
    result2=obj2.finditer(list1)


    for j in result2:
        num+=1
        print('正在获取href'+f'{num}')
        list2.append(domain+j.group('href').strip('/'))
    resp.close()
    return list2

def extract_data(url):
    resp=requests.get(url=url)
    resp.encoding='gb2312'
    # print(resp.text)


    obj=re.compile(r'<div class=player_list>.*?<li><a href="(?P<ftp>.*?)"'
                   r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<http>.*?)"',re.S)
    result=obj.finditer(resp.text)

    f=open('data.csv','a',encoding='gb2312',newline='')
    csv_writer=csv.writer(f)

    for i in result:
       dic=i.groupdict()

    dic['ftp']='ftp的下载地址为:'+dic['ftp']
    dic['http']='http的下载地址为:'+dic['http']

    csv_writer.writerow(dic.values())
    resp.close()




if __name__=='__main__':
    list=main(domain)
    num=0
    for url in list:
        num+=1
        print('正在提取下载地址'+f'{num}')
        extract_data(url)

    print('over!')