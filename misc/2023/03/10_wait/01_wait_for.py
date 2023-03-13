import random
import asyncio

async def runner(delay):
    name = asyncio.current_task().get_name()
    for i in range(3):
        await asyncio.sleep(random.random()*delay)
        print(f"{name}: {i+1}")
    return 42

async def main():
    wait_runner = asyncio.wait_for(runner(random.random()), timeout=0.1)
    try:
        result = await wait_runner
        print(result)
    except asyncio.exceptions.TimeoutError as e:
        print(repr(e))
        print("The task timed out")

asyncio.run(main())