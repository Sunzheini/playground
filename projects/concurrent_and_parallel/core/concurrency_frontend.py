"""
Frontend for demonstrating Python concurrency methods using NiceGUI.
"""
import os
import time
from datetime import datetime
import multiprocessing
import threading
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import psutil
from nicegui import ui

from projects.concurrent_and_parallel.helpers.simulated_tasks import cpu_intensive_task, io_intensive_task, mixed_task


class ConcurrencyFrontend:
    """
    Manages concurrency demonstrations using different methods.
    """
    MAX_EXECUTION_HISTORY_RECORDS = 200

    def __init__(self, backend):
        self.backend = backend

        #region ui elements
        self.task_type = None
        self.iterations = None
        self.num_tasks = None
        self.results_label = None
        self.cpu_label = None
        self.memory_label = None
        self.thread_count_label = None
        self.history_table = None
        self.chart_container = None
        #endregion

        #region collections
        self.task_choices = ['CPU Intensive', 'IO Intensive', 'Mixed']
        #endregion

        #region state
        self.running_tasks = set()
        self.results = []
        self.cpu_usage = []
        self.memory_usage = []
        self.start_time = None
        #endregion

    #region UI Creation
    def create_ui(self):
        """Create the main UI layout and schedule background metrics."""
        ui.colors(primary='#496CAB', secondary='#53B689', accent='#111B1E', positive='#53B689')

        # Header
        with ui.header().classes('bg-primary text-white'):
            ui.label('Python Concurrency Examples').classes('text-h4 font-bold')
            ui.space()
            ui.button('ℹ️', on_click=self._show_info).props('flat')

        # Main content
        with ((ui.row().classes('w-full'))):
            # Left panel - Controls
            with ui.column().classes('33vw p-4 space-y-4'):
                ui.label('Task Configuration').classes('text-h5')

                ui.label(f'{self._show_number_of_cores()}').classes('text-body2 text-blue-600')

                self.task_type = ui.select(
                    options=self.task_choices,
                    value='CPU Intensive',
                    label='Task Type'
                ).classes('w-full')

                # Two cards side by side in a row
                with ui.row().classes('w-full gap-4 items-stretch'):

                    # region Iterations
                    with ui.column().classes('flex-1'):
                        with ui.card().classes('p-4 border-2 border-blue-200 rounded-lg h-full'):
                            ui.markdown(
                                '**Iterations per task** (how many times the selected task is executed within each parallel task)') \
                                .classes('text-body2 q-mb-xs')

                            with ui.row().classes('items-center w-full gap-4'):
                                # Min value display
                                ui.label('1').classes('text-caption text-grey w-12')

                                # Slider
                                self.iterations = ui.slider(
                                    min=1, max=100, value=20
                                ).classes('flex-grow').on('update:model-value',
                                                          lambda e: number_input.set_value(e.args))

                                # Max value display
                                ui.label('100').classes('text-caption text-grey w-12')

                                number_input = ui.number(
                                    min=1, max=100, value=20
                                ).classes('w-40 ml-36').on('update:model-value',
                                                           lambda e: self.iterations.set_value(e.args))
                    # endregion

                    # region Number of tasks
                    with ui.column().classes('flex-1'):
                        with ui.card().classes(
                                'p-4 border-2 border-blue-200 rounded-lg h-full'):
                            ui.markdown(
                                '**Number of parallel tasks** (sequential run / separate processes / worker threads / coroutines)') \
                                .classes('text-body2 q-mb-xs')

                            with ui.row().classes('items-center w-full gap-4'):
                                # Min value display
                                ui.label('1').classes('text-caption text-grey w-12')

                                # Slider
                                self.num_tasks = ui.slider(
                                    min=1, max=20, value=5
                                ).classes('flex-grow').on('update:model-value',
                                                          lambda e: num_tasks_input.set_value(e.args))

                                # Max value display
                                ui.label('20').classes('text-caption text-grey w-12')

                                # Number input for precise control
                                num_tasks_input = ui.number(
                                    min=1, max=20, value=5
                                ).classes('w-40 ml-36').on('update:model-value',
                                                           lambda e: self.num_tasks.set_value(e.args))
                    # endregion

                #region Execution buttons (NiceGUI supports async callbacks)
                with ui.row().classes('w-full space-x-2'):
                    ui.button('Sequential', on_click=self.run_sequential,
                              color='secondary').classes('flex-1')
                    ui.button('Multiprocessing (manual)', on_click=self.run_multiprocessing_manual,
                              color='secondary').classes('flex-1')
                    ui.button('Threading', on_click=self.run_multithreading,
                              color='secondary').classes('flex-1')
                    ui.button('Asyncio', on_click=self.run_asyncio,
                              color='secondary').classes('flex-1')

                with ui.row().classes('w-full space-x-2'):
                    ui.button('',
                              color='secondary').classes('flex-1')
                    ui.button('Multiprocessing (auto)', on_click=self.run_multiprocessing_auto,
                              color='secondary').classes('flex-1')
                    ui.button('',
                              color='secondary').classes('flex-1')
                    ui.button('',
                              color='secondary').classes('flex-1')
                #endregion

                #region  Results display
                with ui.card().classes('p-4 border border-gray-300 rounded-lg bg-gray-50 w-full'):
                    ui.label('Results').classes('text-h6 font-bold mb-2')
                    self.results_label = ui.label('Results will appear here').classes('text-body1')
                #endregion

                #region  Clear button
                ui.button('Clear Execution History', on_click=self.clear_results, color='negative')
                #endregion

                #region Execution history
                with ui.card().classes('w-full'):
                    ui.label('Execution History').classes('text-h6')
                    self.history_table = ui.table(
                        columns=[
                            {'name': 'timestamp', 'label': 'Time', 'field': 'timestamp', 'align': 'left'},
                            {'name': 'method', 'label': 'Method', 'field': 'method', 'align': 'left'},
                            {'name': 'time', 'label': 'Time (s)', 'field': 'time', 'align': 'left'},
                            {'name': 'tasks', 'label': 'Tasks', 'field': 'tasks', 'align': 'left'},
                        ],
                        rows=[]
                    ).classes('w-full')
                #endregion
    #endregion
    
    #region General methods
    def _show_info(self) -> None:
        """Show information dialog describing the demo."""
        with ui.dialog() as dialog, ui.card():
            ui.markdown(self.backend.info_text)
            ui.button('Close', on_click=dialog.close)
        dialog.open()

    def _show_number_of_cores(self) -> str:
        """Show a dialog with the number of CPU cores."""
        text = f'({self.backend.number_of_cores_text} CPU cores detected)'
        return text

    def get_task_function(self):
        """Return a module-level function (pickle-able) for the selected task type."""
        task_type = self.task_type.value
        if task_type == 'CPU Intensive':
            return cpu_intensive_task
        elif task_type == 'IO Intensive':
            return io_intensive_task
        else:
            return mixed_task

    def start_execution(self, method) -> None:
        """Prepare for execution: reset results and mark start time."""
        self.results = []
        self.start_time = time.time()
        ui.notify(f'Starting {method} execution...')

    def show_results(self, method, duration, results) -> None:
        """Display execution results with a defensive guard for empty results."""
        avg = duration / len(results) if results else 0.0  # avoid division by zero
        self.results_label.set_text(
            f'{method} completed in {duration:.3f} seconds.\n'
            f'Processed {len(results)} tasks.\n'
            f'Average time per task: {avg:.3f}s.\n'
            f'Results: {results}.'
        )

    def add_to_history(self, method, duration, num_tasks) -> None:
        """Add execution to history table and cap size to MAX_EXECUTION_HISTORY_RECORDS."""
        history = self.history_table.rows
        history.append({
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'method': method,
            'time': f'{duration:.3f}',
            'tasks': num_tasks
        })
        # Keep history bounded
        if len(history) > self.MAX_EXECUTION_HISTORY_RECORDS:
            del history[0: len(history) - self.MAX_EXECUTION_HISTORY_RECORDS]
        self.history_table.update()

    def clear_results(self) -> None:
        """Clear UI results and history."""
        self.results_label.set_text('Results will appear here')
        self.history_table.rows.clear()
        self.history_table.update()
        ui.notify('Results cleared')
    #endregion

    #region Concurrency Methods
    async def run_multiprocessing_manual(self):
        """Run tasks manually using multiprocessing.Process and Queue safely on Windows.
        Uses module-level functions (picklable) and spawn context to avoid Windows issues.
        """
        self.start_execution('Multiprocessing')
        task_func = self.get_task_function()
        num_iterations = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        results, history = await self.backend.run_multiprocessing_manual_approach_with_queue(task_func, num_iterations, num_tasks)

        self.show_results(*results)
        self.add_to_history(*history)

    async def run_multiprocessing_auto(self):
        """Run tasks using ProcessPoolExecutor safely on Windows and without blocking the event loop.
        Uses module-level functions (picklable) and spawn context to avoid Windows issues.
        """
        self.start_execution('Multiprocessing')
        task_func = self.get_task_function()
        num_iterations = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        results, history = await self.backend.run_multiprocessing_executor_approach(task_func, num_iterations, num_tasks)

        self.show_results(*results)
        self.add_to_history(*history)

    async def run_sequential(self):
        """Run tasks sequentially but offload the actual computation to a thread.

        This keeps the UI responsive while the CPU/IO work executes in a background
        thread via asyncio.to_thread.
        """
        self.start_execution('Sequential')
        task_func = self.get_task_function()
        num_iterations = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        results, history = await self.backend.run_sequential(task_func, num_iterations, num_tasks)

        self.show_results(*results)
        self.add_to_history(*history)

    async def run_multithreading(self):
        """Run tasks using ThreadPoolExecutor without blocking the event loop."""
        self.start_execution('Threading')
        task_func = self.get_task_function()
        num_iterations = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        results, history = await self.backend.run_multithreading(task_func, num_iterations, num_tasks)

        self.show_results(*results)
        self.add_to_history(*history)

    async def run_asyncio(self):
        """Run tasks using asyncio by offloading blocking calls to threads with asyncio.to_thread."""
        self.start_execution('Asyncio')
        task_func = self.get_task_function()
        num_iterations = int(self.iterations.value)
        num_tasks = int(self.num_tasks.value)

        results, history = await self.backend.run_asyncio(task_func, num_iterations, num_tasks)

        self.show_results(*results)
        self.add_to_history(*history)
    #endregion
