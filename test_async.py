from time import time
import asyncio

event_loop = asyncio.get_event_loop()
start = time()


async def spider(site_name):
    for page in range(1, 4):
        await asyncio.sleep(1)
        print(site_name, page)


async def main():
    tasks = [
        asyncio.create_task(spider("blog")),
        asyncio.create_task(spider("tim")),
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    print("{:.2f}".format(time() - start))
