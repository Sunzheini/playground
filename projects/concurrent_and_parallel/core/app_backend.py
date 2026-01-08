"""
Module: app_backend
"""
import asyncio
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from functools import partial


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
    @staticmethod
    async def run_multiprocessing_executor_approach(task_function, number_of_iterations: int, number_of_tasks: int):
        """
        Multiprocessing approach using ProcessPoolExecutor.
        :param task_function: the function to execute in parallel
        :param number_of_iterations: the number of iterations for each task
        :param number_of_tasks: the number of parallel tasks to run
        :return: tuple containing results and performance metrics

        Demonstrates:
        1. Using ProcessPoolExecutor for parallel execution
        2. Automatic process management
        """
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
    def _multiprocessing_worker(task_function, iterations, task_id, results_queue=None):
        """Module-level worker for manual multiprocessing."""
        try:
            result = task_function(iterations)
            if results_queue is not None:
                results_queue.put((task_id, result))
            return result
        except Exception as e:
            if results_queue is not None:
                results_queue.put((task_id, e))
            return e

    @staticmethod
    async def run_multiprocessing_manual_approach(task_function, number_of_processes: int, number_of_iterations: int, use_queue=False):
        """
        Manual multiprocessing approach using multiprocessing.Process directly.
        :param task_function: the function to execute in each process
        :param number_of_processes: the number of processes to create
        :param number_of_iterations: the number of iterations for each task
        :param use_queue: whether to use a multiprocessing.Queue for results
        :return: tuple containing results and performance metrics

        Demonstrates:
        1. Direct process creation with multiprocessing.Process
        2. Manual process lifecycle management (start/join)
        3. Inter-process communication with Queue
        4. Lower-level control compared to ProcessPoolExecutor
        """
        def sync_run():
            processes = []
            results_queue = multiprocessing.Queue() if use_queue else None
            results = []

            # 1. Create and start processes
            for process_id in range(number_of_processes):
                p = multiprocessing.Process(
                    target=AppBackend._multiprocessing_worker,  # Use module-level function
                    args=(task_function, number_of_iterations, process_id, results_queue)
                )
                p.start()
                processes.append(p)

            # 2. Wait for all processes to complete
            for p in processes:
                p.join()

            # 3. Collect results from queue if used
            if results_queue:
                while not results_queue.empty():
                    task_id, result = results_queue.get()
                    results.append(result)

            return results

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Multiprocessing', duration, results), ('Multiprocessing', duration, number_of_processes)

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
