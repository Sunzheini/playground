from nicegui import ui
import time
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing
import psutil
from datetime import datetime
import os

# --- Top-level worker functions ---
# Define worker functions at module level so they are picklable for ProcessPoolExecutor


def cpu_intensive(n):
    """CPU-intensive task: calculate pi using Leibniz formula (slow but demonstrative)."""
    pi = 0
    for i in range(n):
        pi += (-1) ** i / (2 * i + 1)
    return pi * 4


def io_intensive(n):
    """IO-intensive task: simulate file operations with sleep."""
    # time.sleep blocks the current thread; in our code we run this in a thread or process.
    time.sleep(0.001 * (n / 10000))
    return n * 2


def mixed_task_func(n):
    """Mixed CPU + IO task implemented at module level for pickling."""
    result = 0
    for i in range(n // 10):
        result += i ** 0.5
    time.sleep(0.0005 * (n / 10000))
    return result


class ConcurrencyDemo:
    # Limit history rows to avoid unbounded growth in the UI
    MAX_HISTORY = 200

    def __init__(self):
        self.running_tasks = set()
        self.results = []
        self.cpu_usage = []
        self.memory_usage = []
        self.start_time = None

        # Prime psutil so the first cpu_percent() call returns a valid value
        psutil.cpu_percent()

    def create_ui(self):
        """Create the main UI layout and schedule background metrics."""
        ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')

        # Header
        with ui.header().classes('bg-primary text-white'):
            ui.label('Python Concurrency Demo').classes('text-h4 font-bold')
            ui.space()
            ui.button('ℹ️', on_click=self.show_info).props('flat')

        # Main content
        with ui.row().classes('w-full'):
            # Left panel - Controls
            with ui.column().classes('w-1/3 p-4 space-y-4'):
                ui.label('Task Configuration').classes('text-h5')

                self.task_type = ui.select(
                    options=['CPU Intensive', 'IO Intensive', 'Mixed'],
                    value='CPU Intensive',
                    label='Task Type'
                ).classes('w-full')

                # Iterations slider: NiceGUI Slider doesn't accept a `label` kwarg, create a label widget instead
                ui.label('Iterations per task').classes('text-body2')
                self.iterations = ui.slider(
                    min=1000, max=10000000, value=1000000
                ).classes('w-full')

                # Number of tasks slider: create a label separately
                ui.label('Number of parallel tasks').classes('text-body2')
                self.num_tasks = ui.slider(
                    min=1, max=20, value=4
                ).classes('w-full')

                # Execution buttons - NiceGUI supports async callbacks, so we use async handlers
                with ui.row().classes('w-full space-x-2'):
                    ui.button('Sequential', on_click=self.run_sequential,
                              color='secondary').classes('flex-1')
                    ui.button('Threading', on_click=self.run_threading,
                              color='secondary').classes('flex-1')
                    ui.button('Multiprocessing', on_click=self.run_multiprocessing,
                              color='secondary').classes('flex-1')
                    ui.button('Asyncio', on_click=self.run_asyncio,
                              color='secondary').classes('flex-1')

                # Results display
                self.results_label = ui.label('Results will appear here').classes('text-body1')
                self.metrics_label = ui.label('').classes('text-body1')

                # Clear button
                ui.button('Clear Results', on_click=self.clear_results, color='negative')

            # Right panel - Visualizations
            with ui.column().classes('w-2/3 p-4 space-y-4'):
                ui.label('Performance Metrics').classes('text-h5')

                # Performance comparison chart (placeholder)
                self.chart_container = ui.column().classes('w-full h-64')

                # System resource monitoring
                with ui.card().classes('w-full'):
                    ui.label('System Resources').classes('text-h6')
                    self.cpu_label = ui.label('CPU: --%').classes('text-body1')
                    self.memory_label = ui.label('Memory: --%').classes('text-body1')
                    self.thread_count_label = ui.label('Threads: --').classes('text-body1')

                # Execution history
                with ui.card().classes('w-full'):
                    ui.label('Execution History').classes('text-h6')
                    self.history_table = ui.table(
                        columns=[
                            {'name': 'timestamp', 'label': 'Time', 'field': 'timestamp'},
                            {'name': 'method', 'label': 'Method', 'field': 'method'},
                            {'name': 'time', 'label': 'Time (s)', 'field': 'time'},
                            {'name': 'tasks', 'label': 'Tasks', 'field': 'tasks'}
                        ],
                        rows=[]
                    ).classes('w-full')

        # Schedule the metrics loop as a background task so it doesn't block UI creation
        # If there's already a running event loop (e.g. when NiceGUI is active), schedule the task immediately.
        # If not (e.g. create_ui called before ui.run), schedule creation of the task once the loop starts.
        try:
            asyncio.get_running_loop().create_task(self.update_system_metrics())
        except RuntimeError:
            # No running loop yet — arrange to create the task when the loop starts.
            try:
                # Prefer call_soon with a lambda that calls asyncio.create_task
                asyncio.get_event_loop().call_soon(lambda: asyncio.create_task(self.update_system_metrics()))
            except Exception:
                # Last-resort fallback: ignore — NiceGUI will create the loop and the metrics won't run
                pass

    def get_task_function(self):
        """Return a module-level function (picklable) for the selected task type."""
        task_type = self.task_type.value
        if task_type == 'CPU Intensive':
            return cpu_intensive
        elif task_type == 'IO Intensive':
            return io_intensive
        else:
            return mixed_task_func

    def start_execution(self, method):
        """Prepare for execution: reset results and mark start time."""
        self.results = []
        self.start_time = time.time()
        ui.notify(f'Starting {method} execution...')

    def show_results(self, method, duration, results):
        """Display execution results with a defensive guard for empty results."""
        avg = duration / len(results) if results else 0.0  # avoid division by zero
        self.results_label.set_text(
            f'{method} completed in {duration:.3f} seconds\n'
            f'Processed {len(results)} tasks\n'
            f'Average time per task: {avg:.3f}s'
        )

        # Update metrics (placeholder)
        self.update_performance_chart(method, duration)

    def add_to_history(self, method, duration, num_tasks):
        """Add execution to history table and cap size to MAX_HISTORY."""
        history = self.history_table.rows
        history.append({
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'method': method,
            'time': f'{duration:.3f}',
            'tasks': num_tasks
        })
        # Keep history bounded
        if len(history) > self.MAX_HISTORY:
            del history[0: len(history) - self.MAX_HISTORY]
        self.history_table.update()

    def update_performance_chart(self, method, duration):
        """Placeholder for updating a chart; left intentionally minimal."""
        # In a real app, you'd render a chart and embed it in the UI container
        pass

    async def update_system_metrics(self):
        """Periodically update CPU/memory/thread labels without blocking the event loop."""
        while True:
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            threads = threading.active_count()

            # Update UI labels from the event loop (safe after await)
            self.cpu_label.set_text(f'CPU: {cpu:.1f}%')
            self.memory_label.set_text(f'Memory: {memory:.1f}%')
            self.thread_count_label.set_text(f'Threads: {threads}')

            await asyncio.sleep(1)

    async def run_sequential(self):
        """Run tasks sequentially but offload the actual computation to a thread.

        This keeps the UI responsive while the CPU/IO work executes in a background
        thread via asyncio.to_thread.
        """
        self.start_execution('Sequential')
        task_func = self.get_task_function()
        n = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        # Execute the blocking loop in a background thread
        def sync_run():
            results = []
            for _ in range(num_tasks):
                try:
                    results.append(task_func(n))
                except Exception as e:
                    results.append(e)
            return results

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        self.show_results('Sequential', duration, results)
        self.add_to_history('Sequential', duration, num_tasks)

    async def run_threading(self):
        """Run tasks using ThreadPoolExecutor without blocking the event loop."""
        self.start_execution('Threading')
        task_func = self.get_task_function()
        n = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        # Wrap the synchronous ThreadPool work in a function and run it in a thread
        def sync_run():
            results = []
            with ThreadPoolExecutor(max_workers=num_tasks) as executor:
                futures = [executor.submit(task_func, n) for _ in range(num_tasks)]
                for f in futures:
                    try:
                        results.append(f.result())
                    except Exception as e:
                        results.append(e)
            return results

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        self.show_results('Threading', duration, results)
        self.add_to_history('Threading', duration, num_tasks)

    async def run_multiprocessing(self):
        """Run tasks using ProcessPoolExecutor safely on Windows and without blocking the event loop.

        Uses module-level functions (picklable) and spawn context to avoid Windows issues.
        """
        self.start_execution('Multiprocessing')
        task_func = self.get_task_function()
        n = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        def sync_run():
            results = []
            # Use 'spawn' context for safety on Windows
            ctx = multiprocessing.get_context('spawn')
            with ProcessPoolExecutor(max_workers=num_tasks, mp_context=ctx) as executor:
                futures = [executor.submit(task_func, n) for _ in range(num_tasks)]
                for f in futures:
                    try:
                        results.append(f.result())
                    except Exception as e:
                        results.append(e)
            return results

        start = time.time()
        results = await asyncio.to_thread(sync_run)
        duration = time.time() - start

        self.show_results('Multiprocessing', duration, results)
        self.add_to_history('Multiprocessing', duration, num_tasks)

    async def run_asyncio(self):
        """Run tasks using asyncio by offloading blocking calls to threads with asyncio.to_thread."""
        self.start_execution('Asyncio')
        task_func = self.get_task_function()
        n = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        # Build coroutines that call the sync function in a thread
        async def async_task():
            return await asyncio.to_thread(task_func, n)

        start = time.time()
        tasks = [async_task() for _ in range(num_tasks)]
        results = await asyncio.gather(*tasks)
        duration = time.time() - start

        self.show_results('Asyncio', duration, results)
        self.add_to_history('Asyncio', duration, num_tasks)

    def clear_results(self):
        """Clear UI results and history."""
        self.results_label.set_text('Results will appear here')
        self.metrics_label.set_text('')
        self.history_table.rows.clear()
        self.history_table.update()
        ui.notify('Results cleared')

    def show_info(self):
        """Show information dialog describing the demo."""
        with ui.dialog() as dialog, ui.card():
            ui.label('About This Demo').classes('text-h6')
            ui.markdown('''
            ### Python Concurrency Demo

            This application demonstrates different concurrency approaches in Python:

            1. **Sequential**: Runs tasks one after another
            2. **Threading**: Uses multiple threads (good for I/O-bound tasks)
            3. **Multiprocessing**: Uses multiple processes (good for CPU-bound tasks)
            4. **Asyncio**: Uses async/await for concurrent I/O operations

            **Task Types:**
            - CPU Intensive: Calculation of pi
            - IO Intensive: Simulated file operations
            - Mixed: Combination of both

            Adjust the sliders to see how different parameters affect performance!
            ''')
            ui.button('Close', on_click=dialog.close)
        dialog.open()


# Protect entry point for Windows so ProcessPool spawn doesn't re-import code unsafely
if __name__ == '__main__':
    demo = ConcurrencyDemo()
    demo.create_ui()

    # Run the NiceGUI server
    port = int(os.environ.get('PORT', '8081'))
    ui.run(title='Python Concurrency Demo', port=port, reload=False)
