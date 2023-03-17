from .helpers import get_rand_name, task
from threading import Thread


class MyThread(Thread):
    def run(self):
        self.answer = task()

def main():
    threads = []
    for _ in range(10):
        threads.append(MyThread())
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(", ".join([str(thread.answer) for thread in threads]))


if __name__ == "__main__":
    main()