from multiprocessing import Process, cpu_count
import time

"""
✅ Best for:
    CPU-bound tasks (compute-heavy)
    
    Tasks that require true parallel execution without GIL interference 
    (GUI frameworks run in a single main thread, and blocking operations freeze the event loop.)
    (Tkinter does not natively support async/await)!
    
    Independent processes, often large-scale computation

⏳ Behavior:
    Runs in separate processes, separate memory
    Each process has its own Python interpreter, so GIL is not a bottleneck
    More memory and setup overhead than threads or asyncio
"""

def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print(cpu_count())      # how many I have - 12

    a = Process(target=counter, args=(50000000,))
    b = Process(target=counter, args=(50000000,))
    c = Process(target=counter, args=(50000000,))
    d = Process(target=counter, args=(50000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print(f"finished in: {time.perf_counter()} sec")


if __name__ == '__main__':          # if we create a child process it will copy our
    main()                          # module but not execute it




