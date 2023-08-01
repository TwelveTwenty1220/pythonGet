import re

#findeall:找到所有符合正则的内容
lst=re.findall(r'\d+','我的电话是：12331，我女朋友的电话是:1231312')

print(lst)

#findeiter:返回迭代器,拿到内容使用Group
it=re.finditer(r'\d+','我的电话是：12331，我女朋友的电话是:1231312')
for i in it:
    print(i.group())

#re.search 找到结果就返回,全局匹配

#match是从头开始匹配

#预加载正则表达式

obj=re.compile(r'\d+')

resp=obj.finditer('12312312321')

for it in resp:
    print(it.group())



#从正则里面拿出东西
s=""""
<div clss='jay'><span id='1'>郭麒麟</span></div>
<div clss='qwe'><span id='2'>123麟</span></div>
<div clss='jf'><span id='3'>郭3麟</span></div>
<div clss='jfy'><span id='4'>4麒麟</span></div>
<div clss='gg'><span id='5'>郭5麟</span></div>
"""

obj=re.compile(r"<div clss='.*?'><span id='(?P<id>\d)'>(?P<I>.*?)</span></div>",re.S)

result=obj.finditer(s)

for i in result:
    print(i.group("I"))
    print(i.group('id'))



