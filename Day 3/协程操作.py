import asyncio
import time





async def downLoad(i):
    await asyncio.sleep(2)
    print(f'这是什么{i}')
    pass


async def main():
    task=[]

    for i in range(1,5):
        t=downLoad(i)
        task.append(asyncio.create_task(t))

    await asyncio.wait(task)

    pass

def normal_downLoad(i):
    time.sleep(2)
    print(f'这是什么{i}')
    pass


if __name__ == '__main__':
    t1=time.time()
    asyncio.run(main())
    t2=time.time()
    print(t2-t1)

    t3=time.time()
    for i in range(1,5):
        normal_downLoad(i)
    t4=time.time()

    print(t4-t3)

