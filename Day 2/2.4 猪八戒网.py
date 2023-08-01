import requests
from lxml import etree

url='https://huaban.com/discovery'
headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'}
resp=requests.get(url)
html=etree.HTML(resp.text)
divs=html.xpath('/html/body/div[1]/main/div[3]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div')

resp.close()


for div in divs:
    name=div.xpath('./div/div[2]/div[1]/a/div[2]/text()')
    src=div.xpath('./div/div[1]/a/img/@src')[0]
    resp=requests.get(src)
    i_name=src.split('/')[-1]
    with open('huaban/'+i_name,'wb') as f :
        f.write(resp.content)


print('Finish!')



