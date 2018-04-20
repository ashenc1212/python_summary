import threading
import time

def foo(num):
    print("argument is %d"%num)
    time.sleep(1)

threads = [threading.Thread(target = foo, args = (i,)) for i in range(4)]

[print(thr.getName()) for thr in threads]
[thr.start() for thr in threads]
[thr.join() for thr in threads]
print("finished")