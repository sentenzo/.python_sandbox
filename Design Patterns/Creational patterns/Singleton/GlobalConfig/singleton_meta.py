from typing import Any
from threading import Lock
from time import sleep

class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwds)
                sleep(0.005)
                cls._instances[cls] = instance
        return cls._instances[cls]