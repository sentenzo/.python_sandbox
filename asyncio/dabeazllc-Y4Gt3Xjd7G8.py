"""
https://www.youtube.com/watch?v=Y4Gt3Xjd7G8

Build Your Own Async
"""

import time
import random

SCALE = 100


def get_random_time():
    return random.random() * 8


def get_random_id():
    return hex(random.randint(0x10000000, 0xFFFFFFFF))[2:]


def go_do_something_good(id):
    time_to_go = get_random_time()
    time_to_do = get_random_time()
    print(
        f"{id}: 👍 Taks received to go and do something good. On my way! "
        f"(it'll take {time_to_go} secs)"
    )
    time.sleep(time_to_go)
    print(
        f"{id}: ✊ Now I'm going to do something good. "
        f"(it'll take {time_to_do} secs)"
    )
    time.sleep(time_to_do)
    print(f"{id}: 🏁 The task is finished!")


def main_sync():
    for _ in range(SCALE):
        id = get_random_id()
        go_do_something_good(id)


def main_threading():
    import threading

    for _ in range(SCALE):
        id = get_random_id()
        thread = threading.Thread(target=go_do_something_good, args=(id,))
        thread.start()


def main_multiproc():
    import multiprocessing

    for _ in range(SCALE):
        id = get_random_id()
        process = multiprocessing.Process(target=go_do_something_good, args=(id,))
        process.start()


def main_pool():
    import multiprocessing

    with multiprocessing.Pool(processes=20) as pool:
        for _ in range(SCALE):
            id = get_random_id()
            pool.apply_async(go_do_something_good, (id,))
        pool.close()
        pool.join()


if __name__ == "__main__":
    # main_sync()
    # main_threading()
    # main_multiproc()
    main_pool()
    # asyncio.run(main_async())
