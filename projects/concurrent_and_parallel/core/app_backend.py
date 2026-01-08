"""
Module: app_backend
"""
import multiprocessing
import time

from projects.concurrent_and_parallel.helpers.helper_functions import counter


class AppBackend:
    """
    Backend logic for the concurrency and parallelism application.
    """
    @property
    def info_text(self) -> str:
        """
        Get the multithreading information text.
        :return: A string representing multithreading info.
        """
        text = '''
        ### Python Concurrency Demo

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
