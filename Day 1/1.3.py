import requests

s=input("请输入你要翻译的英文")

data={'kw':s}

url="https://fanyi.baidu.com/sug"


#发送Post请求
resp=requests.post(url=url,data=data)

print(resp)
print(resp.json())
