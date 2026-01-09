"""
Module: app_backend
"""
import asyncio
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


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
    async def run_multiprocessing_manual_approach_with_queue(task_function, number_of_iterations: int, number_of_tasks: int) -> tuple:
        """
        Manual multiprocessing approach using multiprocessing.Process directly.
        :param task_function: the function to execute in each process
        :param number_of_iterations: the number of iterations for each task
        :param number_of_tasks: the number of parallel tasks to run
        :return: tuple containing results and performance metrics

        Demonstrates:
        1. Direct process creation with multiprocessing.Process
        2. Manual process lifecycle management (start/join)
        3. Inter-process communication with Queue
        4. Lower-level control compared to ProcessPoolExecutor
        """
        def sync_run():
            results = []

            processes = []
            results_queue = multiprocessing.Queue()

            # 1. Create and start processes
            for process_id in range(number_of_tasks):
                p = multiprocessing.Process(
                    # target=task_function, # cannot pass non-picklable functions, so we use a module-level wrapper
                    # it would work if we didnt use results = await asyncio.to_thread(sync_run), because of niceui!
                    target=AppBackend._multiprocessing_worker,
                    args=(task_function, number_of_iterations, process_id, results_queue)
                )
                p.start()
                processes.append(p)

            # 2. Wait for all processes to complete
            for p in processes:
                p.join()

            # 3. Collect results
            while not results_queue.empty():
                task_id, result = results_queue.get()
                results.append(result)

            return results

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Multiprocessing (manual) ', duration, results), ('Multiprocessing (manual)', duration, number_of_tasks)

    @staticmethod
    async def run_multiprocessing_executor_approach(task_function, number_of_iterations: int, number_of_tasks: int) -> tuple:
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
            """
            Wraps blocking multiprocessing operations
            Needed because multiprocessing is synchronous/blocking
            :return: list of results from all tasks
            """
            results = []
            ctx = multiprocessing.get_context('spawn')  # Safe for Windows (creates fresh Python processes)

            # 1. Create and start processes
            with ProcessPoolExecutor(max_workers=number_of_tasks, mp_context=ctx) as executor:
                """
                Creates number_tasks Future objects
                Each Future represents a task running in a separate process
                Tasks start executing immediately (when workers available)
                No explicit queue needed - Futures handle result collection internally
                """
                futures = [executor.submit(task_function, number_of_iterations) for _ in range(number_of_tasks)]

                # 2. Wait for all processes to complete / 3. Collect results
                for f in futures:
                    try:
                        results.append(f.result())  # Blocks until task completes
                    except Exception as e:
                        results.append(e)
            return results

        start = time.time()
        """
        asyncio.to_thread(sync_run): Offloads blocking sync_run() to thread pool
        Why?: Keeps NiceGUI event loop responsive
        Alternative without threads: Would block UI during execution"""
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Multiprocessing (auto)', duration, results), ('Multiprocessing (auto)', duration, number_of_tasks)

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
