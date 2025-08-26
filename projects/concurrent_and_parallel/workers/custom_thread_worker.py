import threading


class CustomThreadWorker(threading.Thread):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
