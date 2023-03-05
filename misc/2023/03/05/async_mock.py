import asyncio
import math
from unittest.mock import create_autospec

async def some_func(x):
    await asyncio.sleep(0.01)
    return math.sin(x)

mock_some_func = create_autospec(some_func, return_value=42)

print(asyncio.run(some_func(12)))
# print(mock_some_func(12))
print(asyncio.run(mock_some_func(12)))