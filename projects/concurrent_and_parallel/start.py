import asyncio
import time
import requests
from bs4 import BeautifulSoup

from lab.exercise_beautiful_soup import CustomScraper
from projects.concurrent_and_parallel.core.cmd_menu import CommandMenu
from projects.concurrent_and_parallel.helpers.measure_and_print_time_decorator import measure_and_print_time_decorator
from projects.concurrent_and_parallel.workers.custom_thread_worker import CustomThreadWorker

"""
Continue with:
Udemy course + openai chat
https://realpython.com/async-io-python/
Deepseek conversation
"""

"""
coroutine: an async def function
"""


def sleeper_function(seconds):
    time.sleep(seconds)


# Synchronous
@measure_and_print_time_decorator
def function_1():
    for a in range(2):
        print(f"counting1: {a}")
        time.sleep(1)

    for b in range(2):
        print(f"counting2: {b}")
        time.sleep(1)


# Asynchronous
@measure_and_print_time_decorator
def function_2():
    async def counting1():
        for a in range(2):
            print(f"counting1: {a}")
            await asyncio.sleep(1)

    async def counting2():
        for b in range(2):
            print(f"counting2: {b}")
            await asyncio.sleep(1)

    async def start():                  # must be wrapped in a function no directly: run(gather(...))
        await asyncio.gather(counting1(), counting2())

    asyncio.run(start())


# Threading
def function_3():
    start = time.perf_counter()

    worker1 = CustomThreadWorker(target=function_1, args=())
    worker2 = CustomThreadWorker(target=sleeper_function, args=(5, ))

    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()

    end = time.perf_counter()
    print(f"Total time taken in threads: {end - start} seconds")


# Threading with web scraping
def function_4():
    start = time.perf_counter()

    link = 'https://en.wikipedia.org/wiki/Fortune_500'
    target_class = 'wikitable'
    scraper1 = CustomScraper(link, target_class)

    # scraper1.get_results()
    # sleeper_function(2)     # 2.32

    worker1 = CustomThreadWorker(target=scraper1.get_results, args=())
    worker2 = CustomThreadWorker(target=sleeper_function, args=(2, ))

    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()  # 2.00

    end = time.perf_counter()
    print(f"Total time taken in threads: {end - start} seconds")


if __name__ == "__main__":
    menu = CommandMenu(
        {
            '1': function_1,
            '2': function_2,
            '3': function_3,
            '4': function_4,
        }
    )
    menu.run()  # then run the function by their name
