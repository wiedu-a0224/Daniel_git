from threading import Thread
from time import sleep, time
from random import randint

def test(i, j):
    global r
    a =randint(1, 5)
    sleep(a)
    r[i] = a  #return

r=[None]*10
ths = [None]*10
for i in range(10):
    ths[i] = Thread(target=test, args=(i, i+1), daemon=True)
    ths[i].start()

timeout = 3
start = time()
for i in range(10):
    t= time()-start
    if t >= timeout:
        break
    ths[i].join(timeout=timeout-t)

for i in range(10):
    print(r[i])
