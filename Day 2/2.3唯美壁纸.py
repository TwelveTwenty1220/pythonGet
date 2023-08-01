import time

import requests
from bs4 import BeautifulSoup


url='https://www.umei.cc/meinvtupian/'
domain='https://www.umei.cc'

resp=requests.get(url=url)
resp.encoding='utf-8'

page=BeautifulSoup(resp.text,'html.parser')
resp.close()

tao_tu=page.find_all('div',attrs={'class':'taotu-main'})

for i in tao_tu:
    alist=i.find_all('a')
    time.sleep(1)

    for a in alist:
        child_url=domain+a.get('href')
        child_resp=requests.get(child_url)
        child_resp.encoding='utf-8'
        child_page=BeautifulSoup(child_resp.text,'html.parser')
        child_resp.close()

        a=child_page.find('div',attrs={'class':'big-pic'}).find('img')
        src=a.get('src')


        image=requests.get(src)
        image_name=src.split('/')[-1]
        with open('pictures/'+image_name,mode='wb') as f:
            f.write(image.content)

    time.sleep(1)


print('Over')

