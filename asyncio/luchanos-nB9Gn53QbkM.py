"""
https://www.youtube.com/watch?v=nB9Gn53QbkM
"""

import time
import random

N = 100

# ----------------------------------------


def do_havy_io_operation_sync(number: int):
    time.sleep(random.random() * 3)
    t = random.random() * 3
    print(f"🚀 - #{number} (time: {t} sec)")
    time.sleep(t)
    print(f"🏁 - #{number}")


def main_sync():
    for num in range(N):
        do_havy_io_operation_sync(num)


# ----------------------------------------


import asyncio


async def do_havy_io_operation_async(number: int):
    await asyncio.sleep(random.random() * 3)
    t = random.random() * 3
    print(f"🚀 - #{number} (time: {t} sec)")
    await asyncio.sleep(t)
    print(f"🏁 - #{number}")


async def main_async():
    await asyncio.gather(*[do_havy_io_operation_async(num) for num in range(N)])


# ----------------------------------------

import threading


def main_threading():
    for num in range(N):
        # do_havy_io_operation_sync(num)
        th = threading.Thread(target=do_havy_io_operation_sync, args=(num,))
        th.start()


if __name__ == "__main__":
    main_sync()
    # asyncio.run(main_async())
    # main_threading()
