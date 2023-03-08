# from collections import deque
import time
import asyncio
import random

tasks = list(range(10))
# print(tasks)
def count123(name):
    while tasks:
        task = tasks.pop()
        print(name, ":", task)
        yield


workers = [
    count123("aaa"), 
    count123("bbb"), 
    count123("ccc"),
    count123("ddd"),
]

while workers:
    counter = workers.pop(0)
    try:
        next(counter)
        workers.append(counter)
    except StopIteration:
        ...
