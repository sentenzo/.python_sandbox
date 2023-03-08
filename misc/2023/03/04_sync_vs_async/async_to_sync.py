import asyncio
import random

LINES = """
    My name is Yon Yonson,
    I live in Wisconsin.
    I work in a lumber yard there.
    The people I meet as
    I walk down the street,
    They say "Hello!"
    I say "Hello!"
    They say "What's your name?"
    I say:""".split("\n")

N = 3

async def im_a_fancy_async_func():
    for line in LINES:
        await asyncio.sleep(random.random()/10)
        print(line)
    await asyncio.sleep(random.random()/10)

async def a_main():
    await asyncio.gather(
        *[im_a_fancy_async_func() for _ in range(N)]
    )

def convert_to_sync(f):
    def wrapper(*args, **kwargs):
        asyncio.run(f(*args, **kwargs))
    return wrapper


def main():
    im_a_dull_sync_func = convert_to_sync(im_a_fancy_async_func)
    [im_a_dull_sync_func() for _ in range(N)]



if __name__ == "__main__":
    asyncio.run(a_main())
    # main()