import requests
import re




url='http://www.xinfadi.com.cn/getPriceData.html'
resp=requests.post(url)

print(resp.text)

obj=re.compile(r'{"id":.*?"prodName":"(?P<prodName>.*?)".*?"lowPrice":"(?P<lowPrice>.*?)"'
               r'.*?"pubDate":"(?P<date>.*?)"',re.S)

result=obj.finditer(resp.text)

for i in result:
    print(i.group('prodName'))
    print(i.group('lowPrice'))
    print(i.group('date'))


resp.close()