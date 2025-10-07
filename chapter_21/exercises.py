import multiprocessing
import random
import time


def wait_time():
    time.sleep(random.random())
    print(time.asctime(time.localtime()))


if __name__ == "__main__":
    for i in range(3):
        proc = multiprocessing.Process(target=wait_time)
        proc.start()
