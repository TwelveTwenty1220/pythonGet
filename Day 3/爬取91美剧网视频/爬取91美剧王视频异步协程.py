#1.首先获取m3u8.index的第一层地址
#2.获取m3u8.index的第二层地址
#3.下载视频
#4.合并视频
#Start to do it !

import requests
import re
from bs4 import BeautifulSoup
import aiohttp
import aiofiles
import asyncio
import os



def get_first_m3u8(url):
    resp = requests.get(url)
    obj=re.compile(r'var vid="(?P<first_m3u8>.*?)"')
    return obj.search(resp.text).group('first_m3u8')

def get_second_m3u8(url):
    resp=requests.get(url)
    with open('1.m3u8','wb') as f:
        f.write(resp.content)
    with open('1.m3u8','r',encoding='utf-8') as f:
        for line in f:
            if(line.startswith('#')):
                continue
            else:
                line.strip()
                url1=url.split('index.m3u8')[0]
                url1=url1+line
                download_second_m3u8(url1)
                return url1.split('mixed.m3u8')[0]

def download_second_m3u8(url):
    resp=requests.get(url)
    with open('2.m3u8','wb') as f:
        f.write(resp.content)
    print('m3u8.index下载完毕')

async def download_ts(url,name,session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video4\\{name}",'wb') as f:
            await f.write(await resp.content.read())
    print(f'{name}下载完毕')


    pass
async def download_video(second_up):
    tasks=[]
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open('2.m3u8','r',encoding='utf-8') as f :
            async for line in f :
                if(line.startswith('#')):
                    continue
                else:
                    url=second_up+line.strip()
                    task=asyncio.create_task(download_ts(url,line.strip(),session))
                    tasks.append(task)

            await asyncio.wait(tasks)




    pass

def merge_ts():
    print('开始合并')
    with open('2.m3u8','r',encoding='utf-8') as f :
        list=[]
        target='风骚女子.mp4'
        for line in f:
            if(line.startswith('#')):
                continue
            else:
                line=line.strip()
                list.append(line)

        with open('video4\\3.txt','w',) as f:
            for i in list:
                content=f"file '{i}'"
                f.write(content+'\n')

        # print(os.getcwd())
        # os.chdir('video')
        # print(os.getcwd())
        # ok=os.system('ffmpeg -f concat -safe 0 -i 3.txt -c copy aoo.mp4')
        # print(ok)




if __name__ == '__main__':
    url='https://mjw21.com/dp/NDcxOC0xLTI=.html'
    first_m3u8=get_first_m3u8(url)
    second_up=get_second_m3u8(first_m3u8)
    asyncio.run(download_video(second_up))
    merge_ts()

