# from multiprocessing import Process
import multiprocessing as mp
import time

def foo(q, num):
    q.put(num)
    print("put", num)
    return 0

def f(x):
    time.sleep(1)
    return x * x

if __name__ == "__main__":
    all_res = []
    with mp.Pool(processes = 5) as pool:
        for i in range(9):
            res = pool.apply_async(f, (i,))
            all_res.append(res)
            print('put', i)
        for res in all_res:
            print(res.get())
