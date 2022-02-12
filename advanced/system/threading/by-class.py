from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for _ in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for _ in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.5)
t2.start()

t1.join()
t2.join()

print("Main Thread Completed")