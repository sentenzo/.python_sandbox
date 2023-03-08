import asyncio
import math
from unittest.mock import create_autospec

async def some_func(x):
    await asyncio.sleep(0.01)
    return math.sin(x)

mock_some_func = create_autospec(some_func, return_value=42)

coro = some_func(12)
print(f"{type(some_func)}, {type(coro)}:", asyncio.run(coro))

coro = mock_some_func(12)
print(f"{type(mock_some_func)}, {type(coro)}:", asyncio.run(coro))

