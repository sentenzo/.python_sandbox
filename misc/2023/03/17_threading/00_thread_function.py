from .helpers import get_rand_name, task
from threading import Thread

def main():
    threads = []
    for _ in range(50):
        name = get_rand_name("thread")
        thread = Thread(target=task, args=(name,))
        threads.append(thread)
        thread.start()
    [thread.join() for thread in threads]


if __name__ == "__main__":
    main()