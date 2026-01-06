from nicegui import ui
import time
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing
import psutil
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime


class ConcurrencyDemo:
    def __init__(self):
        self.running_tasks = set()
        self.results = []
        self.cpu_usage = []
        self.memory_usage = []
        self.start_time = None

    def create_ui(self):
        """Create the main UI layout"""
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

                self.iterations = ui.slider(
                    min=1000, max=10000000, value=1000000,
                    label='Iterations per task'
                ).classes('w-full')

                self.num_tasks = ui.slider(
                    min=1, max=20, value=4,
                    label='Number of parallel tasks'
                ).classes('w-full')

                # Execution buttons
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

                # Performance comparison chart
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
                    self.history_table = ui.table({
                        'columns': [
                            {'name': 'timestamp', 'label': 'Time', 'field': 'timestamp'},
                            {'name': 'method', 'label': 'Method', 'field': 'method'},
                            {'name': 'time', 'label': 'Time (s)', 'field': 'time'},
                            {'name': 'tasks', 'label': 'Tasks', 'field': 'tasks'}
                        ],
                        'rows': []
                    }).classes('w-full')

        # Start system monitoring
        self.update_system_metrics()

    def cpu_intensive_task(self, n):
        """CPU-intensive task: calculate pi using Leibniz formula"""
        pi = 0
        for i in range(n):
            pi += (-1) ** i / (2 * i + 1)
        return pi * 4

    def io_intensive_task(self, n):
        """IO-intensive task: simulate file operations"""
        time.sleep(0.001 * (n / 10000))  # Simulate IO delay
        return n * 2

    def mixed_task(self, n):
        """Mixed CPU and IO task"""
        # CPU part
        result = 0
        for i in range(n // 10):
            result += i ** 0.5

        # IO part
        time.sleep(0.0005 * (n / 10000))

        return result

    def run_sequential(self):
        """Run tasks sequentially"""
        self.start_execution('Sequential')

        task_func = self.get_task_function()
        n = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        results = []
        start = time.time()

        for i in range(num_tasks):
            result = task_func(n)
            results.append(result)

        duration = time.time() - start
        self.show_results('Sequential', duration, results)
        self.add_to_history('Sequential', duration, num_tasks)

    def run_threading(self):
        """Run tasks using threading"""
        self.start_execution('Threading')

        task_func = self.get_task_function()
        n = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        start = time.time()

        with ThreadPoolExecutor(max_workers=num_tasks) as executor:
            futures = [executor.submit(task_func, n) for _ in range(num_tasks)]
            results = [future.result() for future in futures]

        duration = time.time() - start
        self.show_results('Threading', duration, results)
        self.add_to_history('Threading', duration, num_tasks)

    def run_multiprocessing(self):
        """Run tasks using multiprocessing"""
        self.start_execution('Multiprocessing')

        task_func = self.get_task_function()
        n = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        start = time.time()

        with ProcessPoolExecutor(max_workers=num_tasks) as executor:
            futures = [executor.submit(task_func, n) for _ in range(num_tasks)]
            results = [future.result() for future in futures]

        duration = time.time() - start
        self.show_results('Multiprocessing', duration, results)
        self.add_to_history('Multiprocessing', duration, num_tasks)

    async def run_asyncio(self):
        """Run tasks using asyncio"""
        self.start_execution('Asyncio')

        task_func = self.get_task_function()
        n = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        # Convert sync function to async
        async def async_task():
            return await asyncio.to_thread(task_func, n)

        start = time.time()

        # Run tasks concurrently
        tasks = [async_task() for _ in range(num_tasks)]
        results = await asyncio.gather(*tasks)

        duration = time.time() - start
        self.show_results('Asyncio', duration, results)
        self.add_to_history('Asyncio', duration, num_tasks)

    def get_task_function(self):
        """Get the appropriate task function based on selection"""
        task_type = self.task_type.value
        if task_type == 'CPU Intensive':
            return self.cpu_intensive_task
        elif task_type == 'IO Intensive':
            return self.io_intensive_task
        else:
            return self.mixed_task

    def start_execution(self, method):
        """Prepare for execution"""
        self.results = []
        self.start_time = time.time()
        ui.notify(f'Starting {method} execution...')

    def show_results(self, method, duration, results):
        """Display execution results"""
        self.results_label.set_text(
            f'{method} completed in {duration:.3f} seconds\n'
            f'Processed {len(results)} tasks\n'
            f'Average time per task: {duration / len(results):.3f}s'
        )

        # Update metrics
        self.update_performance_chart(method, duration)

    def add_to_history(self, method, duration, num_tasks):
        """Add execution to history table"""
        history = self.history_table.rows
        history.append({
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'method': method,
            'time': f'{duration:.3f}',
            'tasks': num_tasks
        })
        self.history_table.update()

    def update_performance_chart(self, method, duration):
        """Update or create performance comparison chart"""
        # In a real app, you'd update a chart here
        # For simplicity, we'll just show a notification
        pass

    async def update_system_metrics(self):
        """Update system resource metrics"""
        while True:
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            threads = threading.active_count()

            self.cpu_label.set_text(f'CPU: {cpu:.1f}%')
            self.memory_label.set_text(f'Memory: {memory:.1f}%')
            self.thread_count_label.set_text(f'Threads: {threads}')

            await asyncio.sleep(1)

    def clear_results(self):
        """Clear all results and history"""
        self.results_label.set_text('Results will appear here')
        self.metrics_label.set_text('')
        self.history_table.rows.clear()
        self.history_table.update()
        ui.notify('Results cleared')

    def show_info(self):
        """Show information dialog"""
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


# Create and run the app
demo = ConcurrencyDemo()
demo.create_ui()

ui.run(title='Python Concurrency Demo', port=8080, reload=False)
