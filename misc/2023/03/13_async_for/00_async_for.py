import asyncio

class ACounter:
    def __init__(self):
        self.count = 10

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = self.count
        await asyncio.sleep(0.1)
        if val < 1:
            print("  ACounter: 0 (done!)")
            raise StopAsyncIteration
        print("  ACounter:", val)
        self.count -= 1
        return val

async def main():
    aiter = ACounter()
    async for i in aiter:
        print("main(): i =", i)

asyncio.run(main())