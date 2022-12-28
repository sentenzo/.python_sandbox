import config
import os
from threading import Thread

config.Config.path = os.path.join(os.path.dirname(__file__), "config.json")

def check_trivial():
    conf = config.Config()
    print(conf.random)

    one_more_conf = config.Config()
    print(id(conf) == id(one_more_conf))  # should be always true

def check_multithreading():
    def routine() -> None:
        conf = config.Config()
        print(id(conf))
    process1 = Thread(target=routine)
    process2 = Thread(target=routine)
    process1.start()
    process2.start()

def main():
    # check_trivial()
    check_multithreading()  # should always print the same id twice

if __name__ == "__main__":
    main()