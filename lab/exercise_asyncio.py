import asyncio
import time
from asyncio import get_event_loop, sleep, gather, wait, new_event_loop, set_event_loop, create_task, run


"""
✅ Best for:
    I/O-bound tasks:
        Network requests (HTTP, sockets)
        File I/O (especially async libraries)
        Database queries (async drivers)
    Lots of concurrent tasks that mostly wait (not compute)

⏳ Behavior:
    Single-threaded, event-loop-based concurrency
    Uses coroutines (async def) and await to yield control while waiting
    Very lightweight: thousands of tasks can run concurrently
"""


def function_1():
    for a in range(2):
        print(f"counting1: {a}")
        time.sleep(1)

    for b in range(2):
        print(f"counting2: {b}")
        time.sleep(1)


def function_2():
    async def counting1():
        for a in range(2):
            print(f"counting1: {a}")
            await sleep(1)

    async def counting2():
        for b in range(2):
            print(f"counting2: {b}")
            await sleep(1)

    # long version: create and close the loop manually -------------------------
    # loop = new_event_loop() # create a new event loop every time
    # set_event_loop(loop)
    #
    # coroutine1 = loop.create_task(counting1())  # create a coroutine object
    # coroutine2 = loop.create_task(counting2())
    #
    # loop.run_until_complete(wait([coroutine1, coroutine2]))
    # loop.close()  # close the loop
    # -------------------------------------------------------------------------

    # short version: use asyncio.run() ----------------------------------------
    async def start():                  # must be wrapped in a function no directly: run(gather(...))
        await asyncio.gather(counting1(), counting2())

    asyncio.run(start())
    # -----------------------------------------------------------------------------


if __name__ == "__main__":
    start_time = time.perf_counter()

    # function_1()  # 4sec
    function_2()    # 2sec

    end_time = time.perf_counter()
    print(f"Total time taken: {end_time - start_time} seconds")
