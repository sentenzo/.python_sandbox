import time
import random
import asyncio

tasks = [random.random()/50 for _ in range(100)]
# print(tasks)

def sync_worker():
    print("Sync  worker:    Started")
    while tasks:
        n = len(tasks)
        task = tasks[-1]
        # time.sleep(0.01)
        try:
            drop = tasks.pop()
            time.sleep(task)
        except IndexError:
            print(f"Sync  worker: ⚠️  Whoops - pop from empty list")
        if drop != task:
            print(f"Sync  worker: ⚠️  Whoops - dropped the wrong one")
        print(f"Sync  worker:    {n} - done")
    print("Sync  worker: ✅ Finnished ")


async def do_task(task):
    # time.sleep(task)
    await asyncio.sleep(task)

async def async_worker():
    print("Async worker:    Started")
    while tasks:
        n = len(tasks)
        task = tasks[-1]
        # await asyncio.sleep(0.001)
        try:
            drop = tasks.pop()
            await do_task(task)
        
        except IndexError:
            print(f"Async worker: ⚠️  Whoops - pop from empty list")
        if drop != task:
            print(f"Async worker: ⚠️  Whoops - dropped the wrong one")
        print(f"Async worker:    {n} - done")
    print("Async worker: ✅ Finnished")


async def main():
    # await asyncio.wait([
    #     async_worker(), 
    #     async_worker(), 
    #     async_worker(),
    #     async_worker(), 
    #     async_worker(), 
    #     async_worker(),
    # ])
    sync_workers = [
        asyncio.to_thread(sync_worker) for _ in range(4)
    ]
    await asyncio.gather(
        *sync_workers,
    )

if __name__ == "__main__":
    started = time.time()

    asyncio.run(main())

    ended = time.time()
    print(f"Took {ended - started} sec.")

