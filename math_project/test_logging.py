# 输出到指定目录
# import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler('output_test.log')
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
import time
import asyncio
import aiohttp
# import pandas as pd
import aiofiles
import csv
import requests
# async def hello():  # 异步代码
#     asyncio.sleep(1)
#     print('hello world %s' % time.time())
#
#
# def run():
#     for i in range(5):
#         loop.run_until_complete(hello())
#
#
# loop = asyncio.get_event_loop()


# async def crawl_pic(urls):
#     tasks = []
#     async with aiohttp.ClientSession() as session:
#         for i, url in enumerate(urls):
#             if i == 0:
#                 continue
#             # elif i / 3000 == 0:
#             #     await asyncio.sleep(10)
#             uid = url[0]  # 用csv才用这两行
#             url = url[1]
#             name = uid + "_" + url.split(".jpg")[0][-43:] + ".jpg"
#             print("i %s, name,%s" % (i, name))
#             tasks.append(write_one(url=url, file=name, session=session))
#         await asyncio.gather(*tasks)



async def func(urls):
    uid = urls[0]  # 用csv才用这两行
    url = urls[1]
    # async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=60)) as session:
    async with aiohttp.ClientSession() as session:
        file = uid + "_" + url.split(".jpg")[0][-43:] + ".jpg"
        async with session.get(url) as response:
            try:
                res = await response.read()
            except:
                return
            # with open("./images/" + file, 'wb') as f:
            #     f.write(res)
            async with aiofiles.open(r"D:\\image_3\\" + file, "wb") as f:
                await f.write(res)


def shuffle():
    # 以前使用的算法是使用另一个对象，并删除掉选出来的数据
    list_a = [1, 2, 3, 4]
    import random
    for m in range(len(list_a)):  # 取四次数据
        x = random.randint(0, len(list_a)-m)  # 独特的闭区间
        list_a[x], list_a[-m-1] = list_a[-m-1], list_a[x]
        print(list_a, x, m)


def funct(urls):
    url = urls[2]
    try:
        r = requests.get(url)
    except:
        return
    # file = uid + "_" + url.split(".jpg")[0][-43:] + ".jpg"
    file = url.split(".jpg")[0][-43:] + ".jpg"
    with open("D:\\image_pass\\" + file, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    # run()
    # import requests
    #
    # # r = requests.get("https://akulaku.s3.amazonaws.com/face/SsufLJJGHbs98d21Bq5eZC5qsfXeyhq3o_f3Lecm4AQ.jpg?AWSAccessKeyId=AKIAJ4ZF337PHI6MV6OA&Signature=lAk63POgzQ80sJ3s%2BsfEeKkX%2BGo%3D&Expires=1555728465")
    # r = requests.get("https://akulaku.s3.amazonaws.com/authentication/vhLQXYoesfn9gDghn1sxtfg3cHkHbCIcLD1pW1w8tPM.jpg?AWSAccessKeyId=AKIAJ4ZF337PHI6MV6OA&Signature=FnMs8eRw1%2BsOkzcypMdX18BeIhI%3D&Expires=1556357407")
    # with open('D:\\image_2\\img11.png', 'wb') as f:
    #     f.write(r.content)
    # start_time = time.time()
    # with open("urls.txt") as infile:
    #     urls = set(map(str.strip, infile))

    # data = pd.read_csv('foo.csv')
    # urls = set(data['pic_url'])

    # csvFile = open("pic_urls_01.csv", "r")
    # urls = csv.reader(csvFile)
    # # loop = asyncio.get_event_loop()
    # loop = asyncio.ProactorEventLoop()
    # asyncio.set_event_loop(loop)
    # tasks = []
    # for i, url in enumerate(urls):
    #     if i == 0:
    #         continue
    #     # elif i == 5000:
    #     #     break
    #     tasks.append(asyncio.ensure_future(func(url)))
    # loop.run_until_complete(asyncio.wait(tasks))
    # total_time = time.time() - start_time
    # print(total_time)
    # loop.close()

    # import threadpool
    # csvFile = open("foo_02.csv", "r", encoding='utf-8')
    # urls = csv.reader(csvFile)
    # tasks = []
    # for i, url in enumerate(urls):
    #     if i == 0:
    #         continue
    #     # elif i == 5000:
    #     #     break
    #     # uid = url[0]  # 用csv才用这两行
    #     # url = url[1]
    #     tasks.append(url)
    # pool = threadpool.ThreadPool(600)
    # req = threadpool.makeRequests(funct, tasks)
    # [pool.putRequest(rq) for rq in req]
    # pool.wait()
    # total_time = time.time() - start_time
    # print(total_time)
    shuffle()
