import requests
import asyncio
import aiohttp
import aiofiles
import json
import socket



async def download(title,bid,cid):
    data = {"book_id": "4356474023",
            "cid": f"4356474023|{cid}",
            "need_bookinfo": 1}
    data = json.dumps(data)
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}') as resp:
            dic=await resp.json()
            async with aiofiles.open(title,'w',encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])
            resp.close()

    pass


async def get_chapter(url,bid):
    resp = requests.get(url=url)
    dic=resp.json()
    tasks=[]
    for item in dic['data']['novel']['items']:
        title=item['title']
        cid=item['cid']
        if(item['price_status']=='0'):
            tasks.append(asyncio.create_task(download(title,bid,cid)))
    await asyncio.wait(tasks)



if __name__ == '__main__':
    socket.setdefaulttimeout(5)
    bid = '4356474023'
    c_url='https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224356474023%22}'
    asyncio.run(get_chapter(c_url,bid))


