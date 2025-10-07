from invoke import task
import time


@task
def mytime(ctx):
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print(f"local time: {time_str}")
