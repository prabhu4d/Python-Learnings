from multiprocessing import Process
import os
import math
import time

N = 200000000

start = time.perf_counter()
def calc():
  for i in range(0, N):
    math.sqrt(i)
    
processes = []

for i in range(10):
  print('registered process %d' % i)
  processes.append(Process(target=calc))
  
  
for proc in processes:
  proc.start()
  
for proc in processes:
  proc.join()
  
finish = time.perf_counter()
print("Process task completed with in %ds" % (finish - start))