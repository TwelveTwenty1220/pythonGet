
import requests

query=input("输入你要搜索的内容: ")
url1=f'这是一首简单的歌{query}'
url='https://cn.bing.com/search?mkt=zh-cn&pc=LVBT&form=CNTP59&ensearch=0&q=%E5%91%A8%E6%9D%B0%E4%BC%A6'
headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'}
#地址栏里面是Get
#headers来模拟浏览器发送请求，防止被误认为程序发送。
resp=requests.get(url,headers=headers)
print(url1)
print(resp)
print(resp.text)

