import threading
import time

total = 0
# lock = threading.RLock()
cv = threading.Condition()
R = 10000

def increase(num):
    global total
    for _ in range(R):
        # print("increase", num, _)
        with cv:
            cv.wait_for(lambda: total < R/2)
            total = total + 1
            cv.notify_all()

def decrease(num):
    global total
    for _ in range(R):
        # print("decrease", num, _)        
        with cv:
            cv.wait_for(lambda: total > 0)
            total = total - 1
            cv.notify_all()

threads = [threading.Thread(target = increase, args = (i,)) for i in range(4)] + [threading.Thread(target = decrease, args = (i,)) for i in range(4)]
[thr.start() for thr in threads]
[thr.join() for thr in threads]
print(total)
print("finished")