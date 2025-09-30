import asyncio
import sys

import aiohttp
import threading
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
    Single-threaded, event-loop-based concurrency: We have 1 process and 1 thread!
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
    # async specifies that this is a coroutine
    async def counting1():
        for a in range(2):
            print(f"counting1: {a}")
            await asyncio.sleep(1)  # waits for the sleep without blocking the loop

    async def counting2():
        for b in range(2):
            print(f"counting2: {b}")
            await asyncio.sleep(1)

    # long version: create and close the loop manually -------------------------
    #
    # loop = new_event_loop() # create a new event loop every time
    # set_event_loop(loop)
    #
    # coroutine1 = loop.create_task(counting1())  # create a coroutine object
    # coroutine2 = loop.create_task(counting2())
    #
    # loop.run_until_complete(wait([coroutine1, coroutine2]))
    # loop.close()  # close the loop
    #
    # -------------------------------------------------------------------------

    # short version: use asyncio.run() ----------------------------------------
    async def start():                  # must be wrapped in a function no directly: run(gather(...))
        await asyncio.gather(counting1(), counting2())  # gather runs them concurrently

    asyncio.run(start())    # run starts and closes the event loop

    # -----------------------------------------------------------------------------

    # run only counting2(). When it hits await asyncio.sleep(1), function_1 will not run
    async def start_only_1_function():
        await counting2()   # executes this first, because they are awaited sequentially
        await counting2()   # executes this second


    asyncio.run(start_only_1_function())
    # Creates a new event loop and runs the coroutine
    # Hits await asyncio.sleep(1) → the coroutine yields control to the event loop
    # Since there are no other coroutines running in this event loop, it just waits for the sleep to finish.
    function_1()

    # -----------------------------------------------------------------------------

    # run only counting2(). When it hits await asyncio.sleep(1), function_1 will run
    threading.Thread(target=function_1).start()     # start function_1 in a separate thread
    asyncio.run(start_only_1_function())            # runs in the main thread using its event loop

    # -----------------------------------------------------------------------------

    # with return values
    async def counting_with_return_1():
        await asyncio.sleep(1)
        return "Result from counting_with_return_1"

    async def counting_with_return_2():
        await asyncio.sleep(1)
        return "Result from counting_with_return_2"

    async def start_with_returns():
        result1, result2 = await asyncio.gather(
            counting_with_return_1(),
            counting_with_return_2()
        )
        print(result1)
        print(result2)

        # the same like result1 + result2 but with timeout
        try:
            result3, result4 = await asyncio.gather(
                asyncio.wait_for(counting_with_return_1(), 10),
                asyncio.wait_for(counting_with_return_2(), 10)
            )
            print(result3)
            print(result4)
        except asyncio.TimeoutError:
            print("A coroutine took too long and was cancelled")

    asyncio.run(start_with_returns())


# async for loops
def function_3():
    async def async_sleep(seconds):
        n = max(2, seconds)

        for i in range(n):
            yield i
            await asyncio.sleep(1)


    async def run_async_sleep(seconds):
        async for i in async_sleep(seconds):
            print(f"Async sleep {seconds}: {i+1}/{seconds}")


    asyncio.run(run_async_sleep(5))


# aiohttp for async HTTP requests
def function_4():
    # Windows fix for "Event loop is closed" warning
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    async def get_async_url_response(session, url):
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=3)) as response:
                return await response.text()
        except asyncio.TimeoutError:
            print(f"Timeout fetching {url}")
            return ""
        except Exception as e:
            print(f"⚠Error fetching {url}: {e}")
            return ""

    async def main():
        urls = [
            'https://python.org',
            'https://docs.python.org/3/library/asyncio.html',
            'https://10.255.255.1',  # fake dead IP to test timeout
            'https://en.wikipedia.org/wiki/Asynchronous_I/O',
        ]

        async with aiohttp.ClientSession() as session:  # one shared session
            tasks = []
            for url in urls:
                print(f"Fetching: {url}")
                task = asyncio.create_task(get_async_url_response(session, url))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)

            for i, response in enumerate(responses):
                if response:
                    print(f"Response {i + 1}: {len(response)} characters")
                else:
                    print(f"Response {i + 1}: <empty or error>")

    asyncio.run(main())


# --- When to use asyncio.run, create_task, to_thread ---
# Use asyncio.run(coro) to start the event loop and run a top-level coroutine.
#   - Typical for scripts, main entry points, or testing async code.
#   - Only call once per program (it creates and closes the event loop).
#
# Use asyncio.create_task(coro) to schedule a coroutine to run concurrently in the background.
#   - Only use inside an already running event loop (i.e., inside async functions).
#   - Lets you start multiple async tasks and await them later (e.g., with asyncio.gather).
#
# Use asyncio.to_thread(func, *args) to run blocking (sync) code in a separate thread from async code.
#   - Useful for file I/O, CPU-bound, or legacy sync functions that would block the event loop.
#   - Returns a coroutine you can await in async code.

# --- asyncio.create_task example ---
def example_create_task():
    async def _process_job(job_id):
        print(f"Start job {job_id}")
        await asyncio.sleep(1)
        print(f"End job {job_id}")
        return f"Job {job_id} done"

    async def main():
        # Schedule jobs concurrently
        tasks = [asyncio.create_task(_process_job(i)) for i in range(3)]
        # Await all jobs
        results = await asyncio.gather(*tasks)
        print("Results:", results)

    asyncio.run(main())

# --- asyncio.to_thread example ---
def example_to_thread():
    import os
    def blocking_file_write(filename, text):
        with open(filename, "w") as f:
            f.write(text)
        return f"Written to {filename}"

    async def main():
        filename = "asyncio_to_thread_example.txt"
        result = await asyncio.to_thread(blocking_file_write, filename, "Hello from to_thread!")
        print(result)
        # Clean up
        if os.path.exists(filename):
            os.remove(filename)

    asyncio.run(main())

# Uncomment to run examples:
# example_create_task()
# example_to_thread()


if __name__ == "__main__":
    start_time = time.perf_counter()

    # function_1()  # 4sec
    # function_2()    # 2sec

    # function_3()

    function_4()

    end_time = time.perf_counter()
    print(f"Total time taken: {end_time - start_time:.3f} seconds")
