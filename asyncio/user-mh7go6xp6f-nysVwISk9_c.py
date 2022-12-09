"""
https://www.youtube.com/watch?v=nysVwISk9_c
Школа бэкенд-разработки 2021
12. Асинхронное программирование на практике – Дмитрий Орлов 

https://github.com/YaBackSchool2021/homework9/blob/71f78f56eac989396eb0e5e318604f75bbb5e31b/event-loop-yield-from.py

"""


import logging
import time
from typing import Any, Callable
import heapq
import functools
import queue
from typing import NamedTuple


class Future:
    def __init__(self) -> None:
        self.result = None
        self.done = False
        self.done_callbacks: set[Callable[["Future"], Any]] = set()
        self.exception = None

    def _handle_callbacks(self):
        for cb in self.done_callbacks:
            try:
                cb(self)
            except Exception:
                logging.exception("Unhandled exception in", cb)

    def set_result(self, result):
        self.done = True
        self.result = result
        self._handle_callbacks()

    def set_exception(self, exception):
        self.exception = exception

    def get_result(self):
        if self.exception:
            raise self.exception
        return self.result

    def __iter__(self):
        while not self.done:
            yield None
        return self.get_result()


"""
# Example:

def sleep(seconds) -> Future:
    future = Future()
    loop.call_later(
        seconds,
        future.set_result,
        True
    )
    return future

yield from sleep(10)

"""


@functools.total_ordering
class TimedContainer(NamedTuple):
    time: float
    value: Any

    def __lt__(self, other):
        return self.time < other.time

    def __eq__(self, other):
        return self.time == other.time


class CallbackHandler:
    def __init__(self) -> None:
        self.heap = []

    def call_later(self, delay, func, *args) -> Future:
        future = Future()
        heapq.heappush(
            self.heap,
            TimedContainer(
                delay + time.monotonic(),
                (
                    future,
                    functools.partial(func, *args),
                ),
            ),
        )
        return future

    def step(self) -> None:
        """
        If the time is ripe for the earliest scheduled callback, then run it
         and update the Future object.
        If there's no callbacks ready to run (the heap is empty or they are
         currently all delayed), do nothing.
        """
        while self.heap:
            if self.heap[0][0] > time.monotonic():
                return
            _future, func = heapq.heappop(self.heap).value
            future: Future = _future
            try:
                future.set_result(func())
            except Exception as e:
                future.set_exception(e)


class EventLoop:
    def __init__(self):
        self.events = queue.SimpleQueue()
        self.callbacks = CallbackHandler()

    def call_later(self, delay, callback, *args) -> Future:
        return self.callbacks.call_later(delay, callback, *args)

    def step(self, coro):
        try:
            next(coro)
        except StopIteration as e:
            return e.value
        self.events.put(coro)

    def run(self):
        while not self.events.empty():
            self.callbacks.step()
            self.step(self.events.get())

    def create_task(self, coro):
        future = Future()

        def wrapper():
            try:
                result = yield from coro
                future.set_result(result)
            except Exception as e:
                future.set_exception(e)

        gen = wrapper()
        self.events.put(gen)
        return future

    def run_until_complete(self, coro):
        future = self.create_task(coro)
        self.run()
        return future.get_result()


loop = EventLoop()


def sleep(secs) -> Future:
    return loop.call_later(secs, lambda: True)


def test(s):
    yield from sleep(2 + s)
    print(time.monotonic(), "test done")


print(time.monotonic(), "start")
loop.create_task(test(0.1))
loop.create_task(test(0.2))
loop.run_until_complete(test(0.3))

print(time.monotonic(), "finished")
