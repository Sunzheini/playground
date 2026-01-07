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
            self._create_label(self.backend.multithreading_info_text)
            self._create_label(self.backend.number_of_cores_text)

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
