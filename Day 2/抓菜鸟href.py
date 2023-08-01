import requests
from bs4 import BeautifulSoup




url='https://www.runoob.com/python/att-string-strip.html'

resp=requests.get(url=url)

page=BeautifulSoup(resp.text,'html.parser')

col_nav=page.find('div' ,attrs={'class':'col nav'})

pc_nav=col_nav.find('ul',attrs={'class':'pc-nav'})

links=pc_nav.find_all(href=True)

list= [link['href']for link in links]

print(list)




