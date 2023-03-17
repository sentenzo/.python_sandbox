import time
import random

def get_rand_name(prefix=None):
    name = hex(random.randint(0x100, 0xfff))[2:]
    if prefix:
        name = f"{prefix}_{name}"
    return name

def task(name=None):
    if not name:
        name = get_rand_name()
    for i in range(5):
        time.sleep(random.random())
        print(f"{name}: {i+1}\n", end="")
    return 42