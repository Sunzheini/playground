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
    def __init__(self):
        pass

    @property
    def current_backend(self):
        return self

    #region Multiprocessing
    @property
    def multithreading_info_text(self) -> str:
        """
        Get the multithreading information text.
        :return: A string representing multithreading info.
        """
        text = """
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
        return text

    @property
    def multithreading_queue_text(self) -> str:
        """
        Get the multithreading queue information text.
        :return: A string representing multithreading queue info.
        """
        text = """
        Benefits of adding a queue:
        1. Inter-Process Communication (IPC): Processes can't share memory directly. A queue allows them to communicate and exchange data.
        2. Collect Results: Without a queue, you can't get results back from processes. With a queue, each process can put its result in the queue.
        3. Progress Monitoring: Processes can send progress updates back to the main process.
        4. Load Balancing: You can use a queue as a task queue for worker processes.
        """
        return text

    @property
    def number_of_cores_text(self) -> str:
        """
        Get the number of CPU cores text.
        :return: A string representing the number of CPU cores.
        """
        num_cores = multiprocessing.cpu_count()
        return f"Number of CPU cores: {num_cores}"

    def parallel_processes(self, number_of_processes: int, number_to_count: int, queue=False) -> float:
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

        for _ in range(number_of_processes):
            if queue:
                p = multiprocessing.Process(target=counter, args=(number_to_count, queue))
            else:
                p = multiprocessing.Process(target=counter, args=(number_to_count,))

            p.start()   # 1. start the process
            processes.append(p)

        for p in processes:
            p.join()    # 2. wait for the process to finish

        end = time.perf_counter()
        elapsed_time_in_seconds = end - start

        return elapsed_time_in_seconds
    #endregion

    #region Multithreading
    # Multithreading related methods can be added here
    #endregion

    #region Asyncio
    # Asyncio related methods can be added here
    #endregion
