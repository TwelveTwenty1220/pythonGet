import requests
import re


url='https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=AOerA/kqNAOItSBlCCsPUGps6IodIiow9gC6uMO6gQBUPCfQ/C+rk5/dgBYosE2gGFqEw4gZG+EV6U2S19UtYd8WNe/09oC7IY7bjE6apsMHSrvLFlPe9ftJTEBSr3qq'
headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'}

resp=requests.get(url=url,headers=headers)
html_content=resp.text

with open('裁判文书.txt', 'w', encoding='utf-8') as f:
    f.write(html_content)

obj=re.compile(r'',re.S)

result=obj.finditer(html_content)


