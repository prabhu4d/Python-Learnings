import time
import threading


def hello():
    print("Hello Thread")
    time.sleep(0.1)


threads = []

for _ in range(100):
    t = threading.Thread(target=hello)
    threads.append(t)

for thread in threads:
    thread.start()
    print(f"Active Threads {threading.activeCount()}")

for thread in threads:
    thread.join()

print("Completed...")
