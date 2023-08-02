


import random
import os

file_name='账户密码.txt'
len=0
def id():

    list=[]
    for i in range(1,9+1):
        s=random.randint(1,10)
        list.append(str(s))
    name=''.join(list)
    print(f'name:{name}')

    with open('账户密码.txt','a',encoding='utf-8') as f :
        content=f'id:  {name}'+'\n'
        f.write(content)


def code():
    list=[]
    for i in range(1, 5 + 1):
        s = random.choice('wadwqfqfqfqeefefqfqqdqw')
        list.append(s)

    for i in range(1,5+1):
        s=random.randint(1,15)
        list.append(str(s))

    for i in range(1,5+1):
        s=random.choice('wadwqfqfqfqeefefqfqqdqw')
        list.append(s)

    code=''.join(list)
    print(f'code:{code}')

    with open('账户密码.txt', 'a',encoding='utf-8') as f:
        content1=f'code:  {code}'+'\n'
        f.write(content1)
        content2='========================='+'\n'
        f.write(content2)





def name1(name):

    with open('账户密码.txt', 'a',encoding='utf-8') as f:

        content=f'用途:  {name}'+'\n'
        f.write(content)



def delete(i):
    if i=='delete':
        with open('账户密码.txt', 'r+') as f:
            f.truncate(len)
    elif i=='deletedelete':
        with open('账户密码.txt', 'r+') as f:
            f.truncate(0)


def main(name):
    name1(name)
    id()
    code()




if __name__ == '__main__':
    len=os.path.getsize(file_name)
    print(f'字节大小:{len}')
    name=input('用于记录的账户名称： ')
    main(name)
    i=input('若删除刚才输入内容，请输入 delete:  '
            '若想删除所有内容输入 deletedelete:')
    if i=='delete':
        delete(i)
    elif i=='deletedelete':
        delete(i)



#85 169 255 340
