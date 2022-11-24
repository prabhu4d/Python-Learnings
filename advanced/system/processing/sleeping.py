from multiprocessing import Process
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for {seconds}s")
    time.sleep(seconds)
    print("Done Sleeping")


processes = []

for i in range(10):
    # t = threading.Thread(target=do_something, args=[(i+1)/10])
    p = Process(target=do_something, args=[10])
    p.start()
    processes.append(p)

"""
other instructions run after the thread is completed

"""
for proc in processes:
    proc.join()

finish = time.perf_counter()

print(f"Finished in {finish - start}s")
