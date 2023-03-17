from threading import Thread
from time import sleep

threads = [Thread(target=lambda:sleep(0.1)) for _ in range(3)]

threads[0].name = "Snow White    ... "
threads[0].daemon = False

threads.append(Thread(name="Daemon     .... ", daemon=True))

def stats(threads):
    [print(
        thread.name,
        thread.daemon, # is thread a daemon
        thread.ident, # the thread id in Python (only exists when thread is launched)
        thread.native_id, # the thread id in OS (only exists when thread is launched)
        thread.is_alive(), # is currently running
        sep="\t",
    ) for thread in threads]
    print("---")

stats(threads)
[thread.start() for thread in threads]
stats(threads)
[thread.join() for thread in threads]
stats(threads)