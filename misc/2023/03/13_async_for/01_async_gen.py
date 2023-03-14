import asyncio

async def comb(arr):
    if len(arr) < 1:
        yield arr
    else:
        for i, x in enumerate(arr):
            await asyncio.sleep(0.00)
            async for c in comb(arr[:i] + arr[i+1:]):
                yield [x] + c

async def print_combs(seq):
    async for c in comb(seq):
        print(c)

async def do_some_other_stuff():
    for _ in range(10):
        await asyncio.sleep(0.00)
        print("... doing other stuff")

async def main():
    await asyncio.gather(
        print_combs([1,2,3]),
        do_some_other_stuff(),
    )

asyncio.run(main())

    