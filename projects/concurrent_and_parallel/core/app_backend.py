"""
Module: app_backend. The backend of the concurrency and parallelism application.
"""
import os
import sys
import time
import asyncio
from random import random

import aiohttp
import multiprocessing
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from asyncio import new_event_loop

from lab.exercise_beautiful_soup import CustomScraper
from projects.concurrent_and_parallel.workers.custom_thread_worker import CustomThreadWorker


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
        No overlap, no parallelism


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


        **Threading**: Uses multiple threads (good for I/O-bound tasks, e.g. file I/O, network)
        I/O-bound tasks that use blocking libraries (not async-friendly)
        GUI responsiveness
        Tasks where you want real OS threads
⏳ 
        Multiple threads share same memory space
        Subject to GIL (Global Interpreter Lock) in CPython:
        Only one thread executes Python bytecode at a time
        Still useful for I/O waits, but not CPU-bound parallelism


        **Asyncio**: Uses async/await for concurrent I/O operations
        I/O-bound tasks
        Network requests (HTTP, sockets)
        File I/O (especially async libraries)
        Database queries (async drivers)
        Lots of concurrent tasks that mostly wait (not compute)

        Single-threaded, event-loop-based concurrency: We have 1 process and 1 thread!
        Uses coroutines (async def) and await to yield control while waiting
        Very lightweight: thousands of tasks can run concurrently
        
        --- When to use asyncio.run, create_task, to_thread ---
        Use asyncio.run(coro) to start the event loop and run a top-level coroutine.
          - Typical for scripts, main entry points, or testing async code.
          - Only call once per program (it creates and closes the event loop).
    
        Use asyncio.create_task(coro) to schedule a coroutine to run concurrently in the background.
          - Only use inside an already running event loop (i.e., inside async functions).
          - Lets you start multiple async tasks and await them later (e.g., with asyncio.gather).
        
        Use asyncio.to_thread(func, *args) to run blocking (sync) code in a separate thread from async code.
          - Useful for file I/O, CPU-bound, or legacy sync functions that would block the event loop.
          - Returns a coroutine you can await in async code.


        **Task Types:**
        - CPU Intensive: e.g. Calculations, Data processing
        - IO Intensive: e.g. File operations, Network requests
        - Mixed: Combination of both
        
        **Notes**:
        Creating processes/threads has cost:
        Process creation: ~0.1s overhead
        Thread creation: ~0.01s overhead
        If tasks are very short, overhead dominates

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

    # region 1. Sequential
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
            results_list = []
            for _ in range(number_of_tasks):
                try:
                    results_list.append(task_function(number_of_iterations))
                except Exception as e:
                    results_list.append(e)
            return results_list

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Sequential', duration, results), ('Sequential', duration, number_of_tasks)
    # endregion

    # region 2. Multiprocessing
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
            results_list = []

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
                    results_list.append(result)

                return results_list

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
            results_list = []
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
                        results_list.append(f.result())  # Blocks until task completes
                    except Exception as e:
                        results_list.append(e)
            return results_list

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
    #endregion

    #region 3. Multithreading
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
            results_list = []
            threads = []

            results_lock = threading.Lock()     # To protect shared results list

            try:
                # 1. Create and start threads
                for thread_id in range(number_of_tasks):
                    thread = threading.Thread(
                        target=AppBackend._multithreading_worker,
                        args=(task_function, number_of_iterations, thread_id, results_list, results_lock)
                    )

                    thread.start()
                    threads.append(thread)

                # 2. Wait for all threads to complete
                for thread in threads:
                    thread.join()

                # 3. Collect results
                results_list.sort(key=lambda x: x[0])    # Sort by worker_id and extract results
                return [r[1] for r in results_list]

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
            results_list = []

            # 1. Create and start processes
            with ThreadPoolExecutor(max_workers=number_of_tasks) as executor:
                futures = [executor.submit(task_function, number_of_iterations) for _ in range(number_of_tasks)]

                # 2. Wait for all processes to complete / 3. Collect results
                for f in futures:
                    try:
                        results_list.append(f.result())  # Blocks until task completes
                    except Exception as e:
                        results_list.append(e)
            return results_list

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Threading', duration, results), ('Threading', duration, number_of_tasks)

    @staticmethod
    async def demonstrate_thread_reuse() -> tuple:
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
    async def demonstrate_thread_states() -> tuple:
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
    async def demonstrate_thread_synchronization() -> tuple:
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
    async def demonstrate_gil_limitation() -> tuple:
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
    #endregion

    # region 4. Asyncio
    @staticmethod
    async def run_asyncio_manually(task_function, number_of_iterations: int, number_of_tasks: int) -> tuple:
        """
        Manual asyncio approach using asyncio.to_thread.
        Info:
        - async keyword specifies that this is a coroutine
        - asyncio.create_task() schedules coroutine on event loop
        - asyncio.gather(tasks) waits for multiple tasks concurrently
        """
        async def async_task_function_wrapper(iterations):
            """Wrap the sync task to run in thread pool."""
            return await asyncio.to_thread(task_function, iterations)

        def sync_run():
            """
            Runs asyncio code in a separate thread.
            This keeps the UI responsive while demonstrating asyncio concepts.
            """
            tasks = []

            # create a new event loop every time, instead of get_running_loop()
            loop = new_event_loop()
            asyncio.set_event_loop(loop)

            try:
                # 1. Create and start tasks
                for _ in range(number_of_tasks):
                    # Create a task from the coroutine
                    task = loop.create_task(async_task_function_wrapper(number_of_iterations))
                    tasks.append(task)

                # 2. Run the event loop until all tasks complete
                # asyncio.gather() returns a coroutine that needs to be awaited
                gather_coroutine = asyncio.gather(*tasks, return_exceptions=True)

                # 3. Run the event loop to completion and collect results
                results_from_run = list(loop.run_until_complete(gather_coroutine))

                return results_from_run

            finally:
                # Clean up the event loop
                if not loop.is_closed():
                    loop.close()

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Asyncio (manual) ', duration, results), ('Asyncio (manual)', duration, number_of_tasks)

    @staticmethod
    async def run_asyncio_auto(task_function, number_of_iterations: int, number_of_tasks: int) -> tuple:
        """
        Simplified manual asyncio approach using asyncio.run().

        Demonstrates:
        1. asyncio.run() - creates and runs event loop automatically
        2. asyncio.gather() - concurrent execution of tasks
        3. Clean, modern asyncio pattern
        """
        async def async_task_function_wrapper(iterations):
            """Wrap the sync task to run in thread pool."""
            return await asyncio.to_thread(task_function, iterations)

        def sync_run():
            """
            Run async code in a thread using asyncio.run().
            This keeps the UI responsive while demonstrating asyncio concepts.
            """
            # 1. Create list of coroutines
            async def main():
                tasks = [async_task_function_wrapper(number_of_iterations) for _ in range(number_of_tasks)]

                # 2. Run all tasks concurrently and 3. collect results
                return await asyncio.gather(*tasks, return_exceptions=True)

            # asyncio.run() handles event loop creation/cleanup automatically
            return asyncio.run(main())

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        return ('Asyncio (auto) ', duration, results), ('Asyncio (auto)', duration, number_of_tasks)

    @staticmethod
    async def demonstrate_event_loop_management() -> tuple:
        """
        Explicitly shows event loop management.

        Demonstrates:
        1. Getting current event loop
        2. Scheduling tasks on event loop
        3. Event loop states and methods
        4. Manual vs automatic loop management
        """
        results = []

        # Get the current running event loop
        loop = asyncio.get_running_loop()
        results.append("=== Current Event Loop ===")
        results.append(f"Loop type: {type(loop).__name__}")
        results.append(f"Is running: {loop.is_running()}")
        results.append(f"Is closed: {loop.is_closed()}")
        results.append(f"Loop time: {loop.time():.6f}")

        # Demonstrate scheduling
        results.append("")
        results.append("=== Scheduling Tasks ===")

        async def sample_task(task_id):
            await asyncio.sleep(0.1)
            return f"Task {task_id} completed"

        # Schedule tasks using different methods
        task1 = asyncio.create_task(sample_task(1))
        results.append(f"Created task 1: {task1}")

        # Using ensure_future (older method)
        coro = sample_task(2)
        task2 = asyncio.ensure_future(coro)
        results.append(f"Created task 2 (ensure_future): {task2}")

        # Wait for tasks
        await asyncio.gather(task1, task2)
        results.append("Both tasks completed")
        results.append(f"Task 1 result: {task1.result()}")
        results.append(f"Task 2 result: {task2.result()}")

        # Show loop methods
        results.append("")
        results.append("=== Event Loop Methods ===")
        results.append("loop.create_task() - Schedule coroutine as task")
        results.append("loop.run_until_complete() - Run until future completes")
        results.append("loop.run_forever() - Run loop indefinitely")
        results.append("loop.stop() - Stop running loop")
        results.append("loop.close() - Close loop")

        return results, 0.2

    @staticmethod
    async def demonstrate_coroutines_vs_generators() -> tuple:
        """
        Shows the difference between coroutines and generators.

        Required knowledge point from requirements.
        """
        results = ["=== Generators (yield) ===", "Synchronous, produce values on demand"]

        def number_generator(n):
            """Traditional generator using yield."""
            for i in range(n):
                yield i  # Produces value, pauses, resumes when next() called

        # Demonstrate generator
        gen = number_generator(3)
        results.append(f"Generator type: {type(gen)}")
        results.append(f"First value: {next(gen)}")
        results.append(f"Second value: {next(gen)}")
        results.append("Values are pulled with next()")
        results.append("Generator state: can send() values, throw() exceptions")

        results.append("")
        results.append("=== Coroutines (async/await) ===")
        results.append("Asynchronous, can await other async operations")

        async def number_coroutine(n):
            """Async coroutine."""
            for i in range(n):
                await asyncio.sleep(0.01)  # Can await!
                yield i  # Async generator (Python 3.6+)

        results.append(f"Coroutine type: async function")
        results.append("Uses 'async def' instead of 'def'")
        results.append("Can use 'await' to pause for async operations")
        results.append("Managed by event loop, not manually with next()")

        results.append("")
        results.append("=== Key Differences ===")
        results.append("1. Generators: yield VALUES (synchronous)")
        results.append("2. Coroutines: await OPERATIONS (asynchronous)")
        results.append("3. Generators: implement iterator protocol")
        results.append("4. Coroutines: implement async iterator protocol")
        results.append("5. Generators: controlled by caller (next())")
        results.append("6. Coroutines: controlled by event loop")
        results.append("7. Generators: good for lazy sequences")
        results.append("8. Coroutines: good for concurrent I/O")

        results.append("")
        results.append("=== Historical Context ===")
        results.append("Before async/await (Python 3.5):")
        results.append("- Used @asyncio.coroutine decorator")
        results.append("- Used 'yield from' for async operations")
        results.append("- Confusing mix of generators and coroutines")
        results.append("")
        results.append("After async/await (Python 3.5+):")
        results.append("- Clear separation: generators vs coroutines")
        results.append("- 'async def' for coroutines, 'def' for generators")
        results.append("- 'await' for async, 'yield' for values")

        return results, 0.0

    @staticmethod
    async def demonstrate_async_communication() -> tuple:
        """
        Simple demonstration of async communication patterns.

        Shows transports and protocols concept.
        """
        results = ["=== Async Communication Patterns ===", "", "1. Async Queue (producer/consumer):"]

        # 1. Async Queue (common pattern)

        queue = asyncio.Queue(maxsize=2)

        async def producer(name, items):
            for item in items:
                await queue.put(item)
                results.append(f"{name} produced: {item}")
                await asyncio.sleep(0.05)

        async def consumer(name):
            while True:
                item = await queue.get()
                results.append(f"{name} consumed: {item}")
                queue.task_done()
                if item == "DONE":
                    break

        # Run producer/consumer
        producer_task = asyncio.create_task(producer("P1", ["A", "B", "C", "DONE"]))
        consumer_task = asyncio.create_task(consumer("C1"))

        await asyncio.gather(producer_task, consumer_task)

        # 2. Event (signaling)
        results.append("")
        results.append("2. Async Event (signaling):")

        event = asyncio.Event()

        async def waiter(name):
            results.append(f"{name} waiting for event...")
            await event.wait()
            results.append(f"{name} received event!")

        async def setter():
            await asyncio.sleep(0.1)
            results.append("Setting event...")
            event.set()

        await asyncio.gather(waiter("Waiter1"), waiter("Waiter2"), setter())

        # 3. Transports/Protocols concept
        results.append("")
        results.append("3. Transports and Protocols (Concept):")
        results.append("Transports: Low-level connection abstraction")
        results.append("  - TCP, SSL, Unix sockets, etc.")
        results.append("Protocols: Application-level logic")
        results.append("  - HTTP, WebSocket, custom protocols")
        results.append("Example: asyncio.start_server() uses transports/protocols")

        return results, 0.3

    @staticmethod
    async def run_asyncio_with_aiohttp(number_of_tasks: int) -> tuple:
        """
        Asyncio approach using aiohttp for true async I/O
        operations for network-bound tasks, e.g. HTTP requests.

        We will not used the task_function parameter here
        """
        async def get_async_url_response(session, url):
            """
            Fetch a URL asynchronously using aiohttp.
            :param session: The aiohttp client session.
            :param url: The URL to fetch.
            :return: The response text.
            """
            try:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=3)) as response:
                    text = await response.text()
                    return f"{url}: {len(text)} chars"
            except Exception as e:
                return f"{url}: Error - {str(e)[:50]}"

        async def async_main(urls_list):
            async with aiohttp.ClientSession() as session:  # one shared session
                tasks = [get_async_url_response(session, url) for url in urls[:number_of_tasks]]
                return await asyncio.gather(*tasks)

        # Windows fix for "Event loop is closed" warning
        if sys.platform.startswith("win"):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        urls = [
            'https://httpbin.org/delay/1',  # Test with delay endpoint
            'https://httpbin.org/delay/2',
            'https://httpbin.org/status/404',  # Test error
            'https://httpbin.org/json',
        ]

        start = time.time()
        results = await async_main(urls)
        duration = time.time() - start

        return ('Asyncio (auto) ', duration, results), ('Asyncio (auto)', duration, number_of_tasks)
    #endregion

    #region 5. Custom examples
    @staticmethod
    async def custom_example_1() -> tuple:
        """
        multiprocessing.Queue: 2 processes, each with multiple threads and a shared queue

        Producer runs in its own process → scrapes, spawns threads, collects results → puts results into the multiprocessing.Queue.
        Consumer runs in its own process → continuously get()s items from the queue → stops when it sees the None sentinel.
        Queue is shared between processes because multiprocessing.Queue is designed for inter-process communication.
        """
        def sleeper_function(seconds):
            time.sleep(seconds)

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
                q.put(result)  # you cannot put worker in the queue

            q.put(None)  # signal that production is done

        def consumer(q):
            workers = []

            while True:
                try:
                    item = q.get(
                        timeout=10)  # blocks until the producer puts something in, it will start consuming as soon as the first item is produced
                except Exception as e:
                    print(f"Consumer timed out waiting for item: {e}")
                    break

                if item is None:
                    break
                worker = CustomThreadWorker(target=sleeper_function, args=(2,))
                workers.append(worker)
                worker.start()

            [w.join() for w in workers]

        def run():
            queue = multiprocessing.Queue()

            process1 = multiprocessing.Process(target=producer, args=(queue,))
            process2 = multiprocessing.Process(target=consumer, args=(queue,))

            process1.start()
            process2.start()

            process1.join()
            process2.join()

        start = time.time()
        await asyncio.to_thread(run)
        duration = time.time() - start

        return ('Custom Example 1', duration, []), ('Custom Example 1', duration, 1)
    #endregion
