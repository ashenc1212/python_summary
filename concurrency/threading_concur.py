import threading
import time

total = 0
lock = threading.RLock()

def foo(num):
    global total
    lock.acquire()
    for _ in range(1000000):
        total = total + 1
    lock.release()

threads = [threading.Thread(target = foo, args = (i,)) for i in range(4)]
[thr.start() for thr in threads]
[thr.join() for thr in threads]
print(total)
print("finished")