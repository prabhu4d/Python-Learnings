"""

CPU bound
IO bound

"""

import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for {seconds}s")
    time.sleep(seconds)
    print("Done Sleeping")


threads = []

for i in range(10):
    # t = threading.Thread(target=do_something, args=[(i+1)/10])
    t = threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)

"""
other instructions run after the thread is completed

"""
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {finish - start}s")
