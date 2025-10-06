import threading


def do_this(what):
    whoami(what)

def whoami(what):
    print(f"thread {threading.current_thread()} says {what}")


if __name__ == "__main__":
    whoami("i am the main program")
    for n in range(5):
        p = threading.Thread(target=do_this, args=(f"i am function {n}",))
        p.start()