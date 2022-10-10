# Multithreading


import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("Breakfast")


def drink_coffee():
    time.sleep(4)
    print("Coffee")


def study():
    time.sleep(5)
    print("Study")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()


x.join()                              # main thread waits for x to continue


print(threading.active_count())       # 1
print(threading.enumerate())          # [<_MainThread(MainThread, started 9372)>]
print(time.perf_counter())            # how long it needed from Run to finish









