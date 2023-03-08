"""
Create multiple tasks manually. This is not a recommended approach. 
"""

import random
import asyncio

async def runner(name):
    """prints "1\n2\n3\n" to stdout"""
    for i in range(3):
        try:
            await asyncio.sleep(random.random()/10)
        except asyncio.exceptions.CancelledError as e:
            # --- sometimes we kill them
            print(f"{name}: I was cancelled!")
            raise e
        if random.random() < 0.1:
            # --- sometimes they just die on their own
            raise Exception("Dummy Exception")
        print(f"{name}: {i+1}")
    # ----------- sometimes they work just fine
    return 42

async def main():
    todo = set()
    done = []
    for i in range(10):
        name = f"runner {i}"
        task = asyncio.create_task(runner(name), name=name)

        todo.add(task)
        task.add_done_callback(todo.discard) # todo.discard(task)
        task.add_done_callback(done.append) #  done.append(task)

    while todo:
        if random.random() < 0.1:
            any_task = next(iter(todo)) 
            any_task.cancel("Because I can!")
        await asyncio.sleep(0.05)
    
    print()
    
    for task in done:
        if task.cancelled():
            print(task.get_name(), "- cancelled")
        else:
            result = None
            try:
                result = task.result()
                print(task.get_name(), "- ok, result=", result)
            except Exception as e:
                print(task.get_name(), "- failed with", e)

asyncio.run(main())