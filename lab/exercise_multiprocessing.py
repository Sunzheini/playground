from multiprocessing import Process, Queue, cpu_count
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
# producer
def counter(num, q=None):
    count = 0
    while count < num:
        count += 1

    if q:
        q.put(count)    # put method is used to add an item to a queue


def several_processes():
    start = time.perf_counter()

    print(cpu_count())      # how many I have - 12 (threads, 6 cores)

    # counter(50000000)
    # counter(50000000)   # 3.85

    a = Process(target=counter, args=(50000000,))
    b = Process(target=counter, args=(50000000,))

    a.start()
    b.start()

    a.join()
    b.join()    # 2.60

    end = time.perf_counter()
    print(f"Finished in {end - start} seconds")


def with_queue():
    start = time.perf_counter()

    q = Queue()     # create a queue for inter-process communication

    a = Process(target=counter, args=(50000000, q))
    b = Process(target=counter, args=(50000000, q))

    a.start()
    b.start()

    a.join()
    b.join()

    # collect results from queue (consumer)
    results = []
    while not q.empty():
        value = q.get()     # this is a blocking call, waits until an item is available!
        results.append(value)

    print(f"Results: {results}")

    end = time.perf_counter()
    print(f"Finished in {end - start} seconds")



def main():
    several_processes()

    with_queue()


if __name__ == '__main__':          # if we create a child process it will copy our
    main()                          # module but not execute it




