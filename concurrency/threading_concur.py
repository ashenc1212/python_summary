import threading
import time

total = 0
# lock = threading.RLock()
cv = threading.Condition()
R = 10000
eve = threading.Event()


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

def wait_print():
    print("wait for event")
    eve.wait()
    print("ready now")

threads = [threading.Thread(target = increase, args = (i,)) for i in range(4)] + [threading.Thread(target = decrease, args = (i,)) for i in range(4)]
[thr.start() for thr in threads]
[thr.join() for thr in threads]
print(total)

eve.clear()
threads = [threading.Thread(target=wait_print) for _ in range(4)]
[thr.start() for thr in threads]
time.sleep(1)
eve.set()
[thr.join() for thr in threads]

print("finished")