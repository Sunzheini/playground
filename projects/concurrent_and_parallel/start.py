import os

from nicegui import ui

from projects.concurrent_and_parallel.core.app_backend import AppBackend
from projects.concurrent_and_parallel.core.concurrency_frontend import ConcurrencyFrontend


# Protect entry point for Windows so ProcessPool spawn doesn't re-import code unsafely
if __name__ == '__main__':
    backend = AppBackend()
    frontend = ConcurrencyFrontend(backend)
    frontend.create_ui()

    # Run the NiceGUI server
    port = int(os.environ.get('PORT', '8080'))
    ui.run(title='Python Concurrency Demo', port=port, reload=False)
