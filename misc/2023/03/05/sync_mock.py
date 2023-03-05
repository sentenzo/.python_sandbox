import math
from unittest.mock import create_autospec

def some_func(x):
    return math.sin(x)

mock_some_func = create_autospec(some_func, return_value=42)

print(some_func(12))
print(mock_some_func(12))

