"""
Create multiple tasks manually. This is not a recommended approach. 
"""

import random
import asyncio

async def runner():
    """prints "1\n2\n3\n" to stdout"""
    name = asyncio.current_task().get_name()
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
    succeeded = []
    failed = []
    cancelled = []

    def on_done_callback(task: asyncio.Task):
        todo.discard(task)
        if task.cancelled():
            cancelled.append(task)
        elif task.exception():
            failed.append(task)
        else:
            succeeded.append(task)

    for i in range(10):
        name = f"runner {i}"
        task = asyncio.create_task(runner(), name=name)
        todo.add(task)
        task.add_done_callback(on_done_callback)
    


    while todo:
        if random.random() < 0.1:
            any_task = next(iter(todo)) 
            was_cancel = any_task.cancel("Because I can!")
            if was_cancel:
                print(
                    "[MAIN]  :", 
                    any_task.get_name(), 
                    "was successfully cancelled",
                )
        # if we used `await task`, it could forward the Exception
        #  but if we run tasks implicitly in background (by sleeping in main 
        #  line), the Exception will not be forwarded, and will be stored 
        #  in `task.exception()`
        await asyncio.sleep(0.01)
    
    print()
    
    if succeeded:
        print("Succeeded:")
        for task in succeeded:
            # if we had an Exception in task.exception(), 
            #  then task.result() would rais it
            print("  ", task.get_name(), "=>", task.result())
    if cancelled:
        print("Cancelled:")
        for task in cancelled:
            print("  ", task.get_name())
    if failed:
        print("Failed:")
        for task in failed:
            print("  ", task.get_name(), "=>", task.exception())

asyncio.run(main())