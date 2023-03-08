import time
import asyncio

DURATION = 5

def long_sync_task():
    time.sleep(0.1)
    print("Sync task: Started")
    for i in range(DURATION):
        print("Sync task: " + ("Tick!","Tock!")[i%2])
        time.sleep(1)
    print("Sync task: Finnished")

async def long_async_task():
    print("Async task: Started")
    for i in range(DURATION):
        print("Async task: " + ("Tick!","Tock!")[i%2])
        await asyncio.sleep(1)
    print("Async task: Finnished")

async def main():
    # # Low-level API
    # async def wrapper():
    #     loop = asyncio.get_event_loop()
    #     await loop.run_in_executor(None, long_sync_task)

    # await asyncio.gather(long_async_task(), wrapper())

    # High-level API
    await asyncio.gather(
        long_async_task(), 
        asyncio.to_thread(long_sync_task),
    )

    # t1 = asyncio.create_task(long_async_task())
    # t2 = asyncio.create_task(asyncio.to_thread(long_sync_task))
    # await asyncio.gather(t1, t2)




if __name__ == "__main__":
    asyncio.run(main())