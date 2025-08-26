import asyncio
import time
from asyncio import get_event_loop, sleep, gather, wait, new_event_loop, set_event_loop, create_task, run

from projects.concurrent_and_parallel.core.cmd_menu import CommandMenu
from projects.concurrent_and_parallel.core.measure_and_print_time_decorator import measure_and_print_time_decorator

"""
Continue with:
https://realpython.com/async-io-python/
Udemy course
Deepseek conversation
"""

"""
coroutine: an async def function
"""


@measure_and_print_time_decorator
def function_1():
    for a in range(2):
        print(f"counting1: {a}")
        time.sleep(1)

    for b in range(2):
        print(f"counting2: {b}")
        time.sleep(1)


@measure_and_print_time_decorator
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
    menu = CommandMenu(
        {
            '1': function_1,
            '2': function_2,
        }
    )
    menu.run()  # then run the function by their name
