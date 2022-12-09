import asyncio
import time

BEAT = 1.0


async def snape(delay=0.5):
    await asyncio.sleep(delay)
    i = 0
    pause = 0.2
    while True:
        i %= 4
        if i == 2:
            print("Se", end="", flush=True)
            time.sleep(pause)
            print("ve", end="", flush=True)
            time.sleep(pause)
            print("rus", end="", flush=True)
            time.sleep(pause * 2)
            print()
            await asyncio.sleep(BEAT - 4 * pause)
        else:
            print("Snape")
            await asyncio.sleep(BEAT)
        i += 1


async def dumbledore(delay=0.1 + BEAT * 8):
    await asyncio.sleep(delay)
    pause = 0.2
    while True:
        print(" Dum", end="", flush=True)
        time.sleep(pause)
        print("ble", end="", flush=True)
        time.sleep(pause)
        print("dore!", end="", flush=True)
        print()
        await asyncio.sleep(BEAT * 8 - 2 * pause)


# async def main():
#     await snape()
#     await dumbledore()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    tasks = [
        loop.create_task(snape()),
        loop.create_task(dumbledore()),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
