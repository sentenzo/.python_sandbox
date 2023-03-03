"""
https://www.youtube.com/watch?v=QG-KvTZwxfc
"""
import asyncio
import random
import sys

import PySimpleGUI as sg

sg.change_look_and_feel("SystemDefaultForReal")

layout = [
    [sg.Text("Password"), sg.InputText(password_char="☼", key="password")],
    [sg.Text("", key="status")],
    [sg.Button("Submit"), sg.Button("Cancel")],
]

window = sg.Window("Async GUI", layout)


async def background():
    while True:
        await asyncio.sleep(1)
        val = random.random()
        print(val)
        window["status"].update(val)

async def ui():
    while True:
        e, v = window.read(timeout=10)
        if e != "__TIMEOUT__":
            print(e, v)
        if e in (None, "Cancel"):
            # sys.exit(0)
            break
        await asyncio.sleep(0)

async def main():
    # await asyncio.gather(
    #     ui(),
    #     background(),
    # )
    tasks = [asyncio.create_task(f()) for f in [ui, background]]
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        
if __name__ == "__main__":
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
