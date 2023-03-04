import time
import asyncio
import random

tasks = [random.random()/50 for _ in range(100)]
# print(tasks)

def sync_worker():
    print("Sync worker: Started")
    while tasks:
        n = len(tasks)
        task = tasks[-1]
        # time.sleep(0.01)
        try:
            drop = tasks.pop()
            time.sleep(task)
        except IndexError:
            print(f"Sync worker: whoops 😕 - pop from empty list")
        if drop != task:
            print(f"Sync worker: whoops 😕 - dropped the wrong one")
        print(f"Sync worker: {n} - done")
    print("Sync worker: Finnished")

async def async_worker():
    print("Async worker: Started")
    while tasks:
        n = len(tasks)
        task = tasks[-1]
        # await asyncio.sleep(0.01)
        try:
            drop = tasks.pop()
            await asyncio.sleep(task)
        except IndexError:
            print(f"Async worker: whoops 😕 - pop from empty list")
        if drop != task:
            print(f"Async worker: whoops 😕 - dropped the wrong one")
        print(f"Async worker: {n} - done")
    print("Async worker: Finnished")

async def main():
    async_workers = [async_worker() for _ in range(3)]
    sync_workers = [asyncio.to_thread(sync_worker) for _ in range(2)]
    await asyncio.gather(
        *async_workers,
        *sync_workers,
    )

if __name__ == "__main__":
    started = time.time()

    # sync_worker()
    asyncio.run(main())

    ended = time.time()
    print(f"Took {ended - started} sec.")