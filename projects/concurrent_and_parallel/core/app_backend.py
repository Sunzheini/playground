"""
Module: app_backend
"""
import multiprocessing


class AppBackend:
    """
    Backend logic for the concurrency and parallelism application.
    """
    def __init__(self):
        pass

    #region properties
    @property
    def current_backend(self):
        return self

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
    def number_of_cores_text(self) -> str:
        """
        Get the number of CPU cores text.
        :return: A string representing the number of CPU cores.
        """
        num_cores = multiprocessing.cpu_count()
        return f"Number of CPU cores: {num_cores}"
    #endregion
