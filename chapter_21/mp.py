import multiprocessing
import os


def whoami(what):
    print(f"process {os.getpid()} says: {what}")


if __name__ == "__main__":
    whoami("i am the main program")
    for n in range(4):
        p = multiprocessing.Process(target=whoami, args=(f"i am function {n}",))
        p.start()
