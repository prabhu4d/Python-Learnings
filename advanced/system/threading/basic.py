from threading import Thread
import os
import math
import time

N = 200000000

start = time.perf_counter()
def calc():
  for i in range(0, N):
    math.sqrt(i)
    
threads = []

for i in range(os.cpu_count()):
  print('registered thread %d' % i)
  threads.append(Thread(target=calc))
  
  
for thread in threads:
  thread.start()
  
for thread in threads:
  thread.join()
  
finish = time.perf_counter()
print("Thread task completed with in %ds" % (finish - start))