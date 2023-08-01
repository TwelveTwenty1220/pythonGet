import aiohttp
import asyncio


urls=[
    'https://i1.huishahe.com/uploads/tu/201807/9999/02a26ad6f7.jpg',
    'https://i1.huishahe.com/uploads/tu/201807/9999/0907a5d433.jpg',
    'https://i1.huishahe.com/uploads/tu/201807/9999/2921a95bf9.jpg'
]


async def aio_download(url):
    name=url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            with open(name,'wb') as f :
                f.write(await resp.content.read())
    print(name,'下载完毕')
    pass

async def main():

    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(aio_download(url)))

    await asyncio.wait(tasks)



    pass

if __name__ == '__main__':
    asyncio.run(main())


