"""
Creating a single task.
"""

import asyncio

async def action():
    print("1:   action - starts")
    # switching to example1():
    await asyncio.sleep(0.2) # "2"
    print("3:   action - ends")

async def main():
    """create and await - the order of actions"""
    print("0: example1 - starts")
    coro = action()
    task = asyncio.create_task(coro)
    # switching to action():
    await asyncio.sleep(0.1) # "1: action - starts"
    # ^^ the task can be finnished at this point if sleep() is long enough, 
    print("2: example1 - task created")
    await task # "3: action - ends"
    # ^^ finnish up the task
    print("4: example1 - task awaited")

asyncio.run(main())