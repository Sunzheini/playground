"""
Module: app_backend
"""
import asyncio
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from projects.concurrent_and_parallel.helpers.helper_functions import counter


class AppBackend:
    """
    Backend logic for the concurrency and parallelism application.
    """
    #region Properties
    @property
    def info_text(self) -> str:
        """
        Get the multithreading information text.
        :return: A string representing multithreading info.
        """
        text = '''
        ## Python Concurrency Examples

        This application demonstrates different concurrency approaches in Python:

        1. **Sequential**: Runs tasks one after another


        2. **Multiprocessing**: Uses multiple processes (good for CPU-bound tasks)
        Tasks that require true parallel execution without GIL interference 
        (GUI frameworks run in a single main thread, and blocking operations freeze the event loop.)
        (Tkinter does not natively support async/await)!

        Runs in separate processes, separate memory.
        Each process has its own Python interpreter, so GIL is not a bottleneck.
        More memory and setup overhead than threads or asyncio.

        3. **Threading**: Uses multiple threads (good for I/O-bound tasks)


        4. **Asyncio**: Uses async/await for concurrent I/O operations

        **Task Types:**
        - CPU Intensive: e.g. Calculations, Data processing
        - IO Intensive: e.g. File operations, Network requests
        - Mixed: Combination of both

        Adjust the sliders to see how different parameters affect performance!
        '''
        return text

    @property
    def number_of_cores_text(self) -> str:
        """
        Get the number of CPU cores text.
        :return: A string representing the number of CPU cores.
        """
        num_cores = multiprocessing.cpu_count()
        return f"{num_cores}"
    #endregion

    #region Methods
    async def run_sequential(self, task_function, number_of_iterations: int, number_of_tasks: int):
        # Execute the blocking loop in a background thread
        def sync_run():
            results = []
            for _ in range(number_of_tasks):
                try:
                    results.append(task_function(number_of_iterations))
                except Exception as e:
                    results.append(e)
            return results

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Sequential', duration, results), ('Sequential', duration, number_of_tasks)

    async def run_multiprocessing(self, task_function, number_of_iterations: int, number_of_tasks: int):
        def sync_run():
            results = []
            # Use 'spawn' context for safety on Windows
            ctx = multiprocessing.get_context('spawn')
            with ProcessPoolExecutor(max_workers=number_of_tasks, mp_context=ctx) as executor:
                futures = [executor.submit(task_function, number_of_iterations) for _ in range(number_of_tasks)]
                for f in futures:
                    try:
                        results.append(f.result())
                    except Exception as e:
                        results.append(e)
            return results

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Multiprocessing', duration, results), ('Multiprocessing', duration, number_of_tasks)

    @staticmethod
    def parallel_processes(number_of_processes: int, number_to_count: int, queue=False) -> tuple[float, list]:
        """
        Run parallel processes.
        :param number_of_processes: The number of processes to run.
        :param number_to_count: The number each process should count to.
        :param queue: An optional Queue for inter-process communication.
        :return: Elapsed time in seconds.
        """
        processes = []
        queue = multiprocessing.Queue() if queue else None  # create a queue for inter-process communication

        start = time.perf_counter()

        # 1. Start processes -----------------------------------------------------------
        for process_number in range(number_of_processes):
            p = multiprocessing.Process(target=counter, args=(number_to_count, queue, process_number))

            p.start()   # 1. start the process
            processes.append(p)
        # ------------------------------------------------------------------------------

        # 2. Wait for processes to finish ----------------------------------------------
        for p in processes:
            p.join()
        # ------------------------------------------------------------------------------

        # 3. Collect results from queue (consumer) -------------------------------------
        results = []
        if queue is not None:
            while not queue.empty():
                results.append(queue.get())

            print(f"Results from processes: {results}")
        # ------------------------------------------------------------------------------

        end = time.perf_counter()
        elapsed_time_in_seconds = end - start

        return elapsed_time_in_seconds, results

    async def run_multithreading(self, task_function, number_of_iterations: int, number_of_tasks: int):
        # Wrap the synchronous ThreadPool work in a function and run it in a thread
        def sync_run():
            results = []
            with ThreadPoolExecutor(max_workers=number_of_tasks) as executor:
                futures = [executor.submit(task_function, number_of_iterations) for _ in range(number_of_tasks)]
                for f in futures:
                    try:
                        results.append(f.result())
                    except Exception as e:
                        results.append(e)
            return results

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Threading', duration, results), ('Threading', duration, number_of_tasks)

    async def run_asyncio(self, task_function, number_of_iterations: int, number_of_tasks: int):
        # Build coroutines that call the sync function in a thread
        async def async_task():
            return await asyncio.to_thread(task_function, number_of_iterations)

        start = time.time()
        tasks = [async_task() for _ in range(number_of_tasks)]
        results = await asyncio.gather(*tasks)
        duration = time.time() - start

        return ('Asyncio', duration, results), ('Asyncio', duration, number_of_tasks)
    #endregion
