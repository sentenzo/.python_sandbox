from threading import (
    Thread,
    current_thread, 
    main_thread,
    active_count,
    get_ident,
    get_native_id,
    enumerate,
)
from time import sleep

thread = current_thread()
assert thread == main_thread()

print("main_thread:")
print(f'\tname={thread.name}, daemon={thread.daemon}, id={thread.ident}')


threads = [Thread(target=lambda:sleep(0.1)) for _ in range(3)]
[thread.start() for thread in threads]
print(f"active_count:\n\t{active_count()}")
print("enumerate():")
for active_thread in enumerate():
    print("\t", active_thread)
[thread.join() for thread in threads]
print(f"\t{active_count()}")

def task():
    print("Task:")
    print("\tcurrent_thread():\t", current_thread())
    print("\tget_ident():      \t", get_ident())
    print("\tget_native_id():\t", get_native_id())

thread = Thread(target=task)
thread.start()
thread.join()