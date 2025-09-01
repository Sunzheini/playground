import time
import asyncio
from multiprocessing import Queue, Process
from random import random

import requests
from async_timeout import timeout
from bs4 import BeautifulSoup

from lab.exercise_beautiful_soup import CustomScraper
from projects.concurrent_and_parallel.core.cmd_menu import CommandMenu
from projects.concurrent_and_parallel.helpers.measure_and_print_time_decorator import measure_and_print_time_decorator
from projects.concurrent_and_parallel.workers.custom_thread_worker import CustomThreadWorker


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
    # async specifies that this is a coroutine
    async def counting1():
        for a in range(2):
            print(f"counting1: {a}")
            await asyncio.sleep(1)      # waits for the sleep without blocking the loop

    async def counting2():
        for b in range(2):
            print(f"counting2: {b}")
            await asyncio.sleep(1)

    async def start():                  # must be wrapped in a function no directly: run(gather(...))
        await asyncio.gather(counting1(), counting2())  # gather runs them concurrently

    asyncio.run(start())    # run starts and closes the loop


# Threading
@measure_and_print_time_decorator
def function_3():
    worker1 = CustomThreadWorker(target=function_1, args=())
    worker2 = CustomThreadWorker(target=sleeper_function, args=(5, ))

    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()


# Threading with web scraping
@measure_and_print_time_decorator
def function_4():
    link = 'https://en.wikipedia.org/wiki/Fortune_500'
    target_class = 'wikitable'
    scraper1 = CustomScraper(link)

    # scraper1.get_results()
    # sleeper_function(2)     # 2.32

    worker1 = CustomThreadWorker(target=scraper1.get_results, args=('', 'table', 'class', target_class))
    worker2 = CustomThreadWorker(target=sleeper_function, args=(2, ))

    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()  # 2.00, without the part below

    # phase 2 - multiple workers
    list_of_subworkers = []
    for i in range(scraper1.total_results):
        sub_worker = CustomThreadWorker(target=sleeper_function, args=(3, ))
        list_of_subworkers.append(sub_worker)
        sub_worker.start()

    [sub_worker.join() for sub_worker in list_of_subworkers]  # 5.00


# ------------------------------------------------------------------------------------------------
# function_5    # multiprocessing.Queue: 2 processes, each with multiple threads and a shared queue
"""
Producer runs in its own process → scrapes, spawns threads, collects results → puts results into the multiprocessing.Queue.
Consumer runs in its own process → continuously get()s items from the queue → stops when it sees the None sentinel.
Queue is shared between processes because multiprocessing.Queue is designed for inter-process communication.
"""
def producer(q):
    link = 'https://en.wikipedia.org/wiki/Fortune_500'
    target_class = 'wikitable'

    for i in range(3):
        scraper = CustomScraper(link)

        worker1 = CustomThreadWorker(target=scraper.get_results, args=('', 'table', 'class', target_class))
        worker2 = CustomThreadWorker(target=sleeper_function, args=(2,))

        worker1.start()
        worker2.start()

        worker1.join()
        worker2.join()

        result = random()
        q.put(result)       # you cannot put worker in the queue

    q.put(None)     # signal that production is done


def consumer(q):
    workers = []

    while True:
        try:
            item = q.get(timeout=10)  # blocks until the producer puts something in, it will start consuming as soon as the first item is produced
        except Exception as e:
            print(f"Consumer timed out waiting for item: {e}")
            break

        if item is None:
            break
        worker = CustomThreadWorker(target=sleeper_function, args=(2,))
        workers.append(worker)
        worker.start()

    [w.join() for w in workers]


@measure_and_print_time_decorator
def function_5():
    queue = Queue()

    process1 = Process(target=producer, args=(queue, ))
    process2 = Process(target=consumer, args=(queue, ))

    process1.start()
    process2.start()

    process1.join()
    process2.join()


# ------------------------------------------------------------------------------------------------
# Multiprocessing
@measure_and_print_time_decorator
def function_6():
    pass


if __name__ == "__main__":
    menu = CommandMenu(
        {
            '1': function_1,
            '2': function_2,
            '3': function_3,
            '4': function_4,
            '5': function_5,
            '6': function_6,
        }
    )
    menu.run()  # then run the function by their name
