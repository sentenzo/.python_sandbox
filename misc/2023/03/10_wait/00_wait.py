import random
import asyncio

N = 5

async def runner(delay):
    name = asyncio.current_task().get_name()
    for i in range(3):
        try:
            await asyncio.sleep(random.random()*delay)
        except asyncio.exceptions.CancelledError as e:
            print(f"{name}: I was cancelled!")
            # raise e
            return None
        print(f"{name}: {i+1}")
    return 42

async def main():
    tasks = set()
    results = []
    while len(results) < N*3:
        while len(tasks) < N:
            new_task = asyncio.create_task(runner(random.random()))
            tasks.add(new_task)
        done, panding = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_COMPLETED
        )
        for task in done:
            results.append(task.result())
        tasks = panding
    for task in panding:
        task.cancel()
        await task
    print(results, "len:", len(results))

asyncio.run(main())