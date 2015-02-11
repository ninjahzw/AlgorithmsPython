from collections import deque as dq
import Queue
import time
current_milli_time = lambda: int(round(time.time() * 1000))

start = current_milli_time()
queue = []
a = 0
while a < 100000:
    queue.append(a)
    a += 1

while queue:
    queue.pop(0)
print current_milli_time()-start

start = current_milli_time()
queue = Queue.Queue()
a = 0
while a < 100000:
    queue.put(a)
    a += 1
while not queue.empty():
    queue.get()
print current_milli_time()-start


start = current_milli_time()
queue = dq()
a = 0
while a < 100000:
    queue.append(a)
    a += 1
while queue:
    queue.popleft()
print current_milli_time()-start


"""
Result:
1588
426
23
deque is much much faster because it is implemented using c
"""
