"""
The UI of the application to showcase concurrent and parallel processing using NiceGUI.
"""
from nicegui import ui


class NiceGuiUI:
    """
    The UI of the application to showcase concurrent and parallel processing using NiceGUI.
    """
    def __init__(self, backend):
        self.ui = ui
        self.ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
        self.backend = backend

        # --------------------------------------------------------------------------------------
        # Multiprocessing section
        # --------------------------------------------------------------------------------------
        with self.ui.row().classes('items-center justify-center mt-4 mb-8'):
            with self.ui.row().classes('items-center justify-center mt-8 border-2 border-gray-300'):
                # self._create_label(self.backend.multithreading_info_text)
                self._create_label(self.backend.number_of_cores_text)

            with self.ui.row().classes('items-center justify-center mt-8 border-2 border-gray-300'):
                self.input_number_processes = self.ui.input(label='Number of processes', value='2').classes('w-48')
                self.input_number_count = self.ui.input(label='Number to count to', value='50000').classes('w-48')
                self.test_button = self.ui.button('Run Multiprocessing Test', on_click=self.run_parallel_processes)
                self.multiprocessing_result = self.ui.label('Click the button to run test')

            with self.ui.row().classes('items-center justify-center mt-8 border-2 border-gray-300'):
                self._create_label(self.backend.multithreading_queue_text)
                self.test_button = self.ui.button('Run Multiprocessing Test', on_click=self.run_parallel_processes_with_queue)
                self.multiprocessing_queue_result = self.ui.label('Click the button to run test with queue')

        # --------------------------------------------------------------------------------------
        # Multithreading section
        # --------------------------------------------------------------------------------------
        with self.ui.row().classes('items-center justify-center mt-4 mb-8'):
            self._create_label("Multithreading demo will be here.")

        # --------------------------------------------------------------------------------------
        # Asyncio section
        # --------------------------------------------------------------------------------------
        with self.ui.row().classes('items-center justify-center mt-4 mb-8'):
            self._create_label("Asyncio demo will be here.")

    # --------------------------------------------------------------------------------------
    # Multiprocessing methods
    # --------------------------------------------------------------------------------------
    def run_parallel_processes(self):
        """
        Run the parallel processes and update the UI with the result.
        """
        num_processes = int(self.input_number_processes.value)
        num_to_count = int(self.input_number_count.value)

        elapsed_time, _ = self.backend.parallel_processes(num_processes, num_to_count)
        self.multiprocessing_result.set_text(f'Finished in {elapsed_time:.2f} seconds using {num_processes} processes counting to {num_to_count}.')

    def run_parallel_processes_with_queue(self):
        """
        Run the parallel processes with a queue and update the UI with the result.
        """
        num_processes = int(self.input_number_processes.value)
        num_to_count = int(self.input_number_count.value)

        elapsed_time, results = self.backend.parallel_processes(num_processes, num_to_count, queue=True)
        self.multiprocessing_queue_result.set_text(f'Finished in {elapsed_time:.2f} seconds using {num_processes} processes counting to {num_to_count} with a queue. '
                                                   f'Results collected from queue: {results}')

    #region properties
    @property
    def current_ui(self):
        return self.ui
    #endregion

    #region private methods
    def _create_label(self, text: str):
        """
        Create a label in the UI.
        :param text: The text of the label.
        :return: The created label element.
        """
        return self.ui.label(text).classes('p-4 bg-blue-50 rounded-lg whitespace-pre-wrap')
    #endregion
