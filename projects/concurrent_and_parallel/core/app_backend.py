"""
Module: app_backend
"""
import asyncio
import multiprocessing
import os
import subprocess
import threading
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

        **Sequential**: Runs tasks one after another. Slowest for multiple tasks.
        Visual timeline:
        Task 1: [======]
        Task 2:        [======]
        Task 3:               [======]
        Task 4:                      [======]
        # No overlap, no parallelism

        **Multiprocessing**: Uses multiple processes (good for CPU-bound tasks)
        Tasks that require true parallel execution without GIL interference 
        (GUI frameworks run in a single main thread, and blocking operations freeze the event loop.)
        (Tkinter does not natively support async/await)!

        Runs in separate processes, separate memory.
        Each process has its own Python interpreter, so GIL is not a bottleneck.
        More memory and setup overhead than threads or asyncio.
        
        Process Pool Benefits:
        1. Process Reuse: Creating processes is expensive. Pools reuse them.
        2. Load Balancing: Tasks automatically distributed to available workers.
        3. Resource Management: Automatic cleanup with context manager.
        4. Queue Management: Internal result collection (no manual Queue needed).
        
        Running External Programs:
        1. Python can start external programs using the 'subprocess' module.
        2. This creates a completely separate process with its own memory space.

        **Threading**: Uses multiple threads (good for I/O-bound tasks)
        I/O-bound tasks that use blocking libraries (not async-friendly)
        GUI responsiveness
        Tasks where you want real OS threads
⏳ 
        Multiple threads share same memory space
        Subject to GIL (Global Interpreter Lock) in CPython:
        Only one thread executes Python bytecode at a time
        Still useful for I/O waits, but not CPU-bound parallelism

        **Asyncio**: Uses async/await for concurrent I/O operations

        **Task Types:**
        - CPU Intensive: e.g. Calculations, Data processing
        - IO Intensive: e.g. File operations, Network requests
        - Mixed: Combination of both
        
        **Notes**:
        # Creating processes/threads has cost:
        Process creation: ~0.1s overhead
        Thread creation: ~0.01s overhead
        # If tasks are very short, overhead dominates

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
    # -----------------------------------------------------------------------------------------
    # 1. Sequential
    # -----------------------------------------------------------------------------------------
    @staticmethod
    async def run_sequential(task_function, number_of_iterations: int, number_of_tasks: int) -> tuple:
        """
        Run tasks sequentially. Slowest for multiple tasks.
        :param task_function: The function to execute.
        :param number_of_iterations: The number of iterations for each task.
        :param number_of_tasks: The number of tasks to run.
        :return: tuple containing results and performance metrics
        """
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

    # -----------------------------------------------------------------------------------------
    # 2. Multiprocessing
    # -----------------------------------------------------------------------------------------
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

            try:
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
                    task_id, result = results_queue.get(timeout=30)
                    results.append(result)

                return results

            finally:
                # Ensure all processes are terminated
                for p in processes:
                    if p.is_alive():
                        p.terminate()
                results_queue.close()
                results_queue.join_thread()

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

    @staticmethod
    async def run_multiprocessing_external_program() -> tuple:
        """
        Demonstrate running code in a separate process using subprocess.
        This shows how to start another program from Python.
        """
        def sync_run():
            # Safe command that works on all systems
            if os.name == 'nt':  # Windows
                command = ['cmd', '/c', 'echo', 'Hello from external process']
            else:  # Unix/Linux/Mac
                command = ['echo', 'Hello from external process']

            try:
                # Run the external command
                result = subprocess.run(
                    command,
                    capture_output=True,  # Capture output
                    text=True,            # Return as text
                    timeout=5             # Timeout after 5 seconds
                )

                # Return info about the external process
                return {
                    'return_code': result.returncode,
                    'stdout': result.stdout.strip(),
                    'stderr': result.stderr.strip(),
                    'command': ' '.join(command)
                }

            except subprocess.TimeoutExpired:
                return {'error': 'Process timed out'}
            except Exception as e:
                return {'error': str(e)}

        start = time.time()
        process_info = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        # Format results for display
        if 'error' in process_info:
            results = [f"Error: {process_info['error']}"]
        else:
            results = [
                f"Command: {process_info['command']}",
                f"Return code: {process_info['return_code']}",
                f"Output: {process_info['stdout']}",
                f"Errors: {process_info['stderr'] or 'None'}"
            ]

        return ('External Process', duration, results), ('External Process', duration, 1)

    # -----------------------------------------------------------------------------------------
    # 3. Multithreading
    # -----------------------------------------------------------------------------------------
    @staticmethod
    def _multithreading_worker(task_function, iterations, task_id, results, results_lock):
        """Module-level worker for manual multithreading."""
        try:
            result = task_function(iterations)
            with results_lock:
                results.append((task_id, result))
        except Exception as e:
            with results_lock:
                results.append((task_id, e))

    @staticmethod
    async def run_multithreading_manual_approach(task_function, number_of_iterations: int, number_of_tasks: int) -> tuple:
        """
        Manual multithreading approach using threading.Thread directly.
        :param task_function: the function to execute
        :param number_of_iterations: the number of iterations for each task
        :param number_of_tasks: the number of parallel tasks to run
        :return: tuple containing results and performance metrics
        """
        def sync_run():
            """Wrap the synchronous Thread work in a function and run it in a thread"""
            results = []
            threads = []

            results_lock = threading.Lock()     # To protect shared results list

            try:
                # 1. Create and start threads
                for thread_id in range(number_of_tasks):
                    thread = threading.Thread(
                        target=AppBackend._multithreading_worker,
                        args=(task_function, number_of_iterations, thread_id, results, results_lock)
                    )

                    thread.start()
                    threads.append(thread)

                # 2. Wait for all threads to complete
                for thread in threads:
                    thread.join()

                # 3. Collect results
                results.sort(key=lambda x: x[0])    # Sort by worker_id and extract results
                return [r[1] for r in results]

            finally:
                # Ensure all threads are cleaned up
                for thread in threads:
                    if thread.is_alive():
                        thread.join()

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Threading (manual)', duration, results), ('Threading (manual)', duration, number_of_tasks)

    @staticmethod
    async def run_multithreading_executor_approach(task_function, number_of_iterations: int, number_of_tasks: int) -> tuple:
        """
        Multithreading approach using ThreadPoolExecutor.
        1. Uses ThreadPoolExecutor for managing threads
        2. Automatic thread lifecycle management
        3. Simplified concurrent execution
        4. Suitable for I/O-bound tasks
        5. Subject to GIL limitations for CPU-bound tasks

        :param task_function: The function to execute
        :param number_of_iterations: The number of iterations for each task
        :param number_of_tasks: The number of parallel tasks to run
        :return: tuple containing results and performance metrics
        """
        def sync_run():
            results = []

            # 1. Create and start processes
            with ThreadPoolExecutor(max_workers=number_of_tasks) as executor:
                futures = [executor.submit(task_function, number_of_iterations) for _ in range(number_of_tasks)]

                # 2. Wait for all processes to complete / 3. Collect results
                for f in futures:
                    try:
                        results.append(f.result())  # Blocks until task completes
                    except Exception as e:
                        results.append(e)
            return results

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Threading', duration, results), ('Threading', duration, number_of_tasks)

    @staticmethod
    async def demonstrate_thread_reuse():
        """Show that threads cannot be restarted."""
        def worker():
            print(f"Thread {threading.current_thread().name} running")
            time.sleep(0.1)

        # Create and start thread
        thread = threading.Thread(target=worker, name="TestThread")
        thread.start()
        thread.join()

        # Try to restart (will fail)
        try:
            thread.start()  # Raises RuntimeError
            return ["Thread CAN be restarted (WRONG!)"], 0.0
        except RuntimeError as e:
            return [f"Thread CANNOT be restarted: {e}"], 0.0

    @staticmethod
    async def demonstrate_thread_states():
        """Show thread states during lifecycle."""
        states_info = []

        def worker():
            time.sleep(0.5)

        thread = threading.Thread(target=worker, name="StateDemo")

        # Initial state
        states_info.append(f"Created: {thread.is_alive()} (alive={thread.is_alive()})")

        thread.start()
        await asyncio.sleep(0.1)
        states_info.append(f"Running: {thread.is_alive()} (alive={thread.is_alive()})")

        thread.join()
        states_info.append(f"Finished: {thread.is_alive()} (alive={thread.is_alive()})")

        return states_info, 0.0

    @staticmethod
    async def demonstrate_thread_synchronization():
        """Show race condition and lock solution."""

        def sync_run():
            results = []

            # Without lock (race condition)
            counter = 0

            def increment():
                nonlocal counter
                for _ in range(1000):
                    counter += 1

            threads = []
            for _ in range(10):
                t = threading.Thread(target=increment)
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

            results.append(f"Without lock: {counter} (expected 10000)")

            # With lock
            counter = 0
            lock = threading.Lock()

            def increment_safe():
                nonlocal counter
                for _ in range(1000):
                    with lock:
                        counter += 1

            threads = []
            for _ in range(10):
                t = threading.Thread(target=increment_safe)
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

            results.append(f"With lock: {counter} (expected 10000)")
            return results, 0.0

        return await asyncio.to_thread(sync_run)

    @staticmethod
    async def demonstrate_gil_limitation():
        """Show that threading doesn't help CPU-bound tasks."""

        def sync_run():
            def cpu_worker(n):
                result = 0
                for i in range(n):
                    result += i * i
                return result

            n = 10000000  # 10 million iterations

            # Sequential
            start = time.time()
            for _ in range(4):
                cpu_worker(n)
            seq_time = time.time() - start

            # Threaded
            start = time.time()
            threads = []
            for _ in range(4):
                t = threading.Thread(target=cpu_worker, args=(n,))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()
            thread_time = time.time() - start

            return [
                f"Sequential (1 thread): {seq_time:.2f}s",
                f"Threaded (4 threads): {thread_time:.2f}s",
                f"Speedup: {seq_time / thread_time:.2f}x (GIL limited!)"
            ], 0.0

        return await asyncio.to_thread(sync_run)

    # -----------------------------------------------------------------------------------------
    # 4. Asyncio
    # -----------------------------------------------------------------------------------------
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
