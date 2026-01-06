from nicegui import ui
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing
import psutil
import matplotlib
import os
# Use non-interactive backend for server environments (no display)
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import sys
from datetime import datetime
import numpy as np

# --- Module-level worker functions ---
# Define these at module level so they are picklable and safe to use with ProcessPoolExecutor.
def cpu_intensive_worker(n):
    """CPU-intensive worker: matrix multiplication (demonstrative)."""
    size = int(n ** 0.5)
    if size < 10:
        size = 10
    a = np.random.rand(size, size)
    b = np.random.rand(size, size)
    return np.dot(a, b).sum()


def io_intensive_worker(n):
    """IO-intensive worker: simulated latency-bound work."""
    time.sleep(0.01 * (n / 10000))
    return sum([i for i in range(n) if i % 2 == 0])


def mixed_worker(n):
    """Mixed CPU+IO worker."""
    result = sum([i ** 0.5 for i in range(n // 100)])
    time.sleep(0.005 * (n / 10000))
    return result


class EnhancedConcurrencyDemo:
    def __init__(self):
        self.performance_data = {'Sequential': [], 'Threading': [],
                                 'Multiprocessing': [], 'Asyncio': []}
        self.execution_history = []
        self.fig, self.ax = plt.subplots(2, 2, figsize=(10, 8))
        plt.subplots_adjust(hspace=0.3, wspace=0.3)

        # Prime psutil so the first cpu_percent() call returns a meaningful value
        psutil.cpu_percent()

    def create_ui(self):
        """Create enhanced UI with visualizations"""
        ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E')

        # Header
        with ui.header().classes('bg-primary text-white shadow-lg'):
            with ui.row().classes('items-center w-full justify-between'):
                ui.label('🐍 Advanced Python Concurrency Demo').classes('text-h4 font-bold')
                ui.button('📊 Performance Dashboard', on_click=self.show_dashboard,
                          color='accent')

        # Main layout
        with ui.tabs().classes('w-full') as tabs:
            ui.tab('Demo', icon='play_circle')
            ui.tab('Explanation', icon='info')
            ui.tab('System Monitor', icon='monitor_heart')

        with ui.tab_panels(tabs, value='Demo').classes('w-full'):
            # Demo Tab
            with ui.tab_panel('Demo'):
                self.create_demo_tab()

            # Explanation Tab
            with ui.tab_panel('Explanation'):
                self.create_explanation_tab()

            # System Monitor Tab
            with ui.tab_panel('System Monitor'):
                self.create_monitor_tab()

        # Schedule the async monitor loop as a background task so it runs without blocking
        # Use create_task to ensure it's scheduled on the running event loop.
        try:
            asyncio.get_running_loop().create_task(self.update_monitor())
        except RuntimeError:
            # If there's no running loop yet (calling create_ui before ui.run), schedule when loop starts
            from functools import partial
            asyncio.get_event_loop().call_soon(partial(asyncio.create_task, self.update_monitor()))

    def create_demo_tab(self):
        """Create the main demonstration tab"""
        with ui.row().classes('w-full h-full'):
            # Control Panel
            with ui.column().classes('w-1/3 p-6 space-y-6 bg-gray-50 rounded-lg m-2'):
                ui.label('🧪 Experiment Setup').classes('text-h5 text-primary')

                # Task Configuration
                with ui.card().classes('w-full'):
                    ui.label('Task Configuration').classes('text-h6')
                    self.task_type = ui.select(
                        options=['CPU Intensive', 'IO Intensive', 'Mixed'],
                        value='CPU Intensive',
                        label='Task Type'
                    ).props('outlined').classes('w-full')

                    # Iterations slider and a label to show its value
                    self.iterations = ui.slider(
                        min=1000, max=5000000, value=100000,
                    ).classes('w-full')
                    # Keep a label to display the numeric value (updated via onchange)
                    self.iterations_label = ui.label(f'Iterations: {100_000:,}')
                    # Update iterations label when slider value changes
                    self.iterations.on('update:model-value', lambda e: self.iterations_label.set_text(f'Iterations: {int(e.args) if hasattr(e, "args") else int(e)}'))

                    self.num_tasks = ui.slider(
                        min=1, max=16, value=4,
                    ).classes('w-full')
                    self.tasks_label = ui.label('Parallel Tasks: 4')
                    self.num_tasks.on('update:model-value', lambda e: self.tasks_label.set_text(f'Parallel Tasks: {int(e.args) if hasattr(e, "args") else int(e)}'))

                # Execution Buttons
                with ui.card().classes('w-full'):
                    ui.label('Execution Methods').classes('text-h6')
                    with ui.grid(columns=2).classes('gap-2 w-full'):
                        ui.button('🔢 Sequential', on_click=self.run_sequential,
                                  color='blue').classes('h-12')
                        ui.button('🧵 Threading', on_click=self.run_threading,
                                  color='green').classes('h-12')
                        ui.button('⚙️ Multiprocessing', on_click=self.run_multiprocessing,
                                  color='orange').classes('h-12')
                        ui.button('🔄 Asyncio', on_click=self.run_asyncio,
                                  color='purple').classes('h-12')

                # Results Display
                with ui.card().classes('w-full'):
                    ui.label('Results').classes('text-h6')
                    self.results_display = ui.column().classes('space-y-2')

            # Visualization Panel
            with ui.column().classes('w-2/3 p-6 space-y-6'):
                ui.label('📈 Performance Visualization').classes('text-h5 text-primary')

                # Performance Comparison
                with ui.card().classes('w-full h-96'):
                    self.chart_image = ui.image('').classes('w-full h-full')
                    self.update_comparison_chart()

                # Live Progress
                with ui.card().classes('w-full'):
                    ui.label('Live Progress').classes('text-h6')
                    self.progress_bars = {}
                    methods = ['Sequential', 'Threading', 'Multiprocessing', 'Asyncio']
                    for method in methods:
                        with ui.row().classes('items-center w-full'):
                            ui.label(method).classes('w-32')
                            # We keep progress updates coarse-grained to avoid thread-safety issues
                            self.progress_bars[method] = ui.linear_progress(0, show_value=False).classes('flex-1')

    def create_explanation_tab(self):
        """Create explanation tab with educational content"""
        with ui.column().classes('p-6 space-y-6'):
            ui.label('📚 Understanding Concurrency in Python').classes('text-h4')

            with ui.expansion('🧵 Threading', value=True).classes('w-full'):
                ui.markdown('''
                **Threading** uses multiple threads within a single process.

                **Best for:** I/O-bound tasks (network requests, file operations)

                **Limitations:** 
                - Global Interpreter Lock (GIL) prevents true parallel execution
                - Threads share memory space
                - Good for I/O but not CPU-bound tasks

                **Use when:** You have many I/O operations that spend time waiting
                ''')

            with ui.expansion('⚙️ Multiprocessing').classes('w-full'):
                ui.markdown('''
                **Multiprocessing** uses separate Python processes.

                **Best for:** CPU-bound tasks (calculations, data processing)

                **Advantages:**
                - Each process has its own Python interpreter and memory space
                - Bypasses the GIL for true parallelism
                - Better CPU core utilization

                **Drawbacks:**
                - Higher memory usage
                - Inter-process communication overhead
                ''')

            with ui.expansion('🔄 Asyncio').classes('w-full'):
                ui.markdown('''
                **Asyncio** uses cooperative multitasking with async/await.

                **Best for:** High concurrency I/O operations

                **How it works:**
                - Single thread with an event loop
                - Tasks yield control when waiting for I/O
                - Extremely lightweight compared to threads

                **Ideal for:** Web servers, network clients, high concurrency apps
                ''')

    def create_monitor_tab(self):
        """Create system monitoring tab"""
        with ui.column().classes('p-6 space-y-6'):
            ui.label('📊 System Resource Monitor').classes('text-h4')

            # CPU Usage
            with ui.card().classes('w-full'):
                ui.label('CPU Usage').classes('text-h6')
                # Create line_plot without passing positional data; use keyword arg for limit
                self.cpu_chart = ui.line_plot(limit=20).classes('h-48')

            # Memory Usage
            with ui.card().classes('w-full'):
                ui.label('Memory Usage').classes('text-h6')
                self.memory_chart = ui.line_plot(limit=20).classes('h-48')

            # System Info
            with ui.row().classes('w-full space-x-4'):
                with ui.card().classes('flex-1'):
                    ui.label('System Info').classes('text-h6')
                    self.cpu_count_label = ui.label('')
                    self.memory_total_label = ui.label('')
                    self.python_version_label = ui.label('')

    # Keep instance methods for local/threaded execution, but multiprocessing will use module-level workers
    def cpu_intensive_task(self, n):
        """CPU-intensive task: matrix multiplication"""
        return cpu_intensive_worker(n)

    def io_intensive_task(self, n):
        """IO-intensive task: simulated network/disk IO"""
        return io_intensive_worker(n)

    def mixed_task(self, n):
        """Mixed CPU and IO task"""
        return mixed_worker(n)

    async def run_sequential(self):
        """Run tasks sequentially (offloaded to a thread to keep UI responsive)."""
        await self._run_with_method('Sequential')

    async def run_threading(self):
        """Run tasks using threading"""
        await self._run_with_method('Threading')

    async def run_multiprocessing(self):
        """Run tasks using multiprocessing"""
        await self._run_with_method('Multiprocessing')

    async def run_asyncio(self):
        """Run tasks using asyncio"""
        await self._run_with_method('Asyncio')

    async def _run_with_method(self, method):
        """Common execution logic for all methods.

        Important: Heavy/blocking operations are executed inside asyncio.to_thread to avoid
        blocking the main event loop / UI thread. We keep progress updates coarse-grained
        because updating UI from background threads is not safe.
        """
        # Pick a picklable function for multiprocessing; module-level workers are used.
        task_type = self.task_type.value
        if task_type == 'CPU Intensive':
            task_func = cpu_intensive_worker
        elif task_type == 'IO Intensive':
            task_func = io_intensive_worker
        else:
            task_func = mixed_worker

        n = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        # Set coarse progress indicator
        self.progress_bars[method].value = 0.1
        start = time.time()

        # Define sync functions to run inside threads so we don't block the event loop
        if method == 'Sequential':
            def sync_run():
                results = []
                for _ in range(num_tasks):
                    try:
                        results.append(task_func(n))
                    except Exception as e:
                        results.append(e)
                return results

            results = await asyncio.to_thread(sync_run)

        elif method == 'Threading':
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

            results = await asyncio.to_thread(sync_run)

        elif method == 'Multiprocessing':
            def sync_run():
                results = []
                ctx = multiprocessing.get_context('spawn')
                with ProcessPoolExecutor(max_workers=min(num_tasks, multiprocessing.cpu_count()), mp_context=ctx) as executor:
                    futures = [executor.submit(task_func, n) for _ in range(num_tasks)]
                    for f in futures:
                        try:
                            results.append(f.result())
                        except Exception as e:
                            results.append(e)
                return results

            results = await asyncio.to_thread(sync_run)

        else:  # Asyncio
            async def async_task():
                return await asyncio.to_thread(task_func, n)

            # Create real asyncio.Task objects so we can await them individually
            tasks = [asyncio.create_task(async_task()) for _ in range(num_tasks)]

            # As tasks complete we update a coarse progress indicator and collect results.
            results = []
            completed = 0
            for fut in asyncio.as_completed(tasks):
                try:
                    r = await fut
                except Exception as e:
                    r = e
                results.append(r)
                completed += 1
                # Update UI progress from the main loop
                self.progress_bars[method].value = completed / num_tasks

            # All tasks are awaited via as_completed; no need to call gather()

        duration = time.time() - start

        # Display results
        self.show_results(method, duration, results, num_tasks)

        # Reset progress bar after a short pause so user sees completion
        await asyncio.sleep(0.3)
        self.progress_bars[method].value = 0

        # Update chart
        self.update_performance_chart(method, duration, num_tasks)

    def get_task_function(self):
        """Get the appropriate task function (kept for backward compatibility)."""
        task_type = self.task_type.value
        if task_type == 'CPU Intensive':
            return cpu_intensive_worker
        elif task_type == 'IO Intensive':
            return io_intensive_worker
        else:
            return mixed_worker

    def show_results(self, method, duration, results, num_tasks):
        """Display execution results"""
        self.results_display.clear()
        with self.results_display:
            ui.label(f'✅ {method} Complete!').classes('text-h6 text-positive')
            ui.separator()
            ui.label(f'⏱️ Total Time: {duration:.3f} seconds')
            ui.label(f'📊 Tasks Completed: {num_tasks}')
            avg = duration / num_tasks if num_tasks else 0.0
            ui.label(f'📈 Average per task: {avg:.3f}s')
            ui.label(f'⚡ Speedup vs Sequential: Calculate by running both')

            # Color code based on performance
            color = 'positive' if duration < 2 else 'warning' if duration < 5 else 'negative'
            ui.label(f'🏆 Performance Rating: {self.get_performance_rating(duration, num_tasks)}').classes(
                f'text-{color}')

    def get_performance_rating(self, duration, num_tasks):
        """Get a performance rating"""
        efficiency = num_tasks / max(duration, 0.1)
        if efficiency > 10:
            return 'Excellent ⭐⭐⭐⭐⭐'
        elif efficiency > 5:
            return 'Good ⭐⭐⭐⭐'
        elif efficiency > 2:
            return 'Average ⭐⭐⭐'
        else:
            return 'Slow ⭐⭐'

    def update_performance_chart(self, method, duration, num_tasks):
        """Update performance comparison chart"""
        if method not in self.performance_data:
            self.performance_data[method] = []

        self.performance_data[method].append({
            'time': datetime.now(),
            'duration': duration,
            'tasks': num_tasks
        })

        # Keep only last 5 entries
        if len(self.performance_data[method]) > 5:
            self.performance_data[method].pop(0)

        self.update_comparison_chart()

    def update_comparison_chart(self):
        """Update the comparison chart image"""
        # Clear previous figure
        self.ax[0, 0].clear()
        self.ax[0, 1].clear()
        self.ax[1, 0].clear()
        self.ax[1, 1].clear()

        # Plot 1: Performance comparison
        methods = list(self.performance_data.keys())
        avg_durations = []

        for method in methods:
            if self.performance_data[method]:
                avg = np.mean([d['duration'] for d in self.performance_data[method]])
                avg_durations.append(avg)
            else:
                avg_durations.append(0)

        colors = ['blue', 'green', 'orange', 'purple']
        bars = self.ax[0, 0].bar(methods, avg_durations, color=colors)
        self.ax[0, 0].set_title('Average Execution Time')
        self.ax[0, 0].set_ylabel('Time (seconds)')
        try:
            self.ax[0, 0].bar_label(bars, fmt='%.2f')
        except Exception:
            pass

        # Plot 2: Speed comparison
        if avg_durations[0] > 0:
            speedup = [avg_durations[0] / max(d, 0.01) for d in avg_durations]
            self.ax[0, 1].bar(methods, speedup, color=colors)
            self.ax[0, 1].set_title('Speedup vs Sequential')
            self.ax[0, 1].set_ylabel('Speedup Factor')

        # Plot 3: Task throughput
        throughput = []
        for method in methods:
            if self.performance_data[method]:
                total_tasks = sum(d['tasks'] for d in self.performance_data[method])
                total_time = sum(d['duration'] for d in self.performance_data[method])
                throughput.append(float(total_tasks) / max(total_time, 0.01))
            else:
                throughput.append(0)

        self.ax[1, 0].bar(methods, throughput, color=colors)
        self.ax[1, 0].set_title('Task Throughput')
        self.ax[1, 0].set_ylabel('Tasks per second')

        # Plot 4: Method usage
        usage_counts = [len(self.performance_data[m]) for m in methods]
        total_usage = sum(usage_counts)
        if total_usage > 0:
            # Only draw pie chart when there is data; otherwise matplotlib computes NaNs and fails
            self.ax[1, 1].pie(usage_counts, labels=methods, colors=colors, autopct='%1.1f%%')
            self.ax[1, 1].set_title('Method Usage Distribution')
        else:
            # No usage data yet — draw a placeholder message instead of a pie chart
            self.ax[1, 1].text(0.5, 0.5, 'No data', horizontalalignment='center',
                               verticalalignment='center', transform=self.ax[1, 1].transAxes,
                               fontsize=12, color='gray')
            self.ax[1, 1].set_title('Method Usage Distribution')

        # Convert to image
        buf = io.BytesIO()
        plt.tight_layout()
        self.fig.savefig(buf, format='png', dpi=100)
        buf.seek(0)

        # Update image in UI
        img_base64 = base64.b64encode(buf.read()).decode()
        self.chart_image.source = f'data:image/png;base64,{img_base64}'
        buf.close()

    async def update_monitor(self):
        """Update system monitoring charts"""
        cpu_history = []
        memory_history = []

        # Initialize system info
        self.cpu_count_label.set_text(f'CPU Cores: {multiprocessing.cpu_count()}')
        memory_gb = psutil.virtual_memory().total / (1024 ** 3)
        self.memory_total_label.set_text(f'Total Memory: {memory_gb:.1f} GB')
        self.python_version_label.set_text(f'Python: {sys.version.split()[0]}')

        count = 0
        while True:
            # Update CPU and memory
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent

            cpu_history.append(cpu)
            memory_history.append(memory)

            # Keep only last 20 points
            if len(cpu_history) > 20:
                cpu_history.pop(0)
                memory_history.pop(0)

            # Update charts
            try:
                # NiceGUI line_plot.push accepts lists of x and y values
                self.cpu_chart.push([count], [cpu])
                self.memory_chart.push([count], [memory])
            except Exception:
                # If push isn't supported, skip updating plots gracefully
                pass

            count += 1
            await asyncio.sleep(1)

    def show_dashboard(self):
        """Show performance dashboard"""
        with ui.dialog() as dialog, ui.card().classes('w-full max-w-4xl'):
            ui.label('📊 Performance Dashboard').classes('text-h4')

            # Add more detailed charts here
            ui.label('Detailed performance analysis would go here...')

            ui.button('Close', on_click=dialog.close)
        dialog.open()


# Create and run the app under the usual guard so ProcessPoolExecutor spawn is safe on Windows
if __name__ == '__main__':
    app = EnhancedConcurrencyDemo()
    app.create_ui()

    port = int(os.environ.get('PORT', '8080'))
    ui.run(title='Advanced Concurrency Demo', port=port, reload=False)
