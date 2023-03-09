import random
import asyncio

async def runner(name):
    """prints "1\n2\n3\n" to stdout"""
    for i in range(3):
        await asyncio.sleep(random.random()/10)
        print(f"{name}: {i+1}")
    return 42

async def main():
    runners = [runner(f"runner {i}") for i in range(10)]
    await asyncio.gather(*runners)

asyncio.run(main())