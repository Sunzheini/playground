import threading
import time

"""
✅ Best for:
    I/O-bound tasks that use blocking libraries (not async-friendly)
    GUI responsiveness
    Tasks where you want real OS threads

⏳ Behavior:
    Multiple threads share same memory space
    Subject to GIL (Global Interpreter Lock) in CPython:
        Only one thread executes Python bytecode at a time
        Still useful for I/O waits, but not CPU-bound parallelism
"""


def eat_breakfast():
    time.sleep(3)
    print("Breakfast")


def drink_coffee():
    time.sleep(4)
    print("Coffee")


def study():
    time.sleep(5)
    print("Study")


x = threading.Thread(target=eat_breakfast, args=())    # daemon=True means it will not block the main thread from exiting
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()


x.join()                              # main thread waits for x to continue
y.join()
z.join()


print(threading.active_count())       # 1
print(threading.enumerate())          # [<_MainThread(MainThread, started 9372)>]
print(time.perf_counter())            # how long it needed from Run to finish


# Locking example
counter = 0
lock = threading.Lock()
"""
lock is a mutex — it ensures that only one thread at a time can execute the 
code inside the with lock: block.
"""

def increment():
    global counter
    for _ in range(100000):
        with lock:

            """
            thread tries to acquire the lock. If the lock is already held by the other
            thread, it waits. If the lock is free, it acquires it.

            Exiting with lock: automatically releases the lock.
            """
            counter += 1  # safe operation

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()

print(counter)  # Always 200000
