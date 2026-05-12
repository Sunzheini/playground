class SingletonInterface:
    """A singleton interface to ensure only one instance of a class is created."""
    _INSTANCE = None
    _INITIALIZED = False

    # __new__ is responsible for creating a new instance of the class. It checks if an instance
    # already exists and returns it if it does, otherwise it creates a new one.
    def __new__(cls, *args, **kwargs):
        if cls._INSTANCE is None:
            cls._INSTANCE = super().__new__(cls)
        return cls._INSTANCE

    # __init__ is responsible for initializing the instance. It checks if the instance has already
    # been initialized to prevent reinitialization.
    def __init__(self, *args, **kwargs):
        if not self._INITIALIZED:
            self._INITIALIZED = True

            # Call the actual initialization logic in subclass
            self._initialize(*args, **kwargs)

    def _initialize(self, *args, **kwargs):
        """Override this method in subclasses for initialization logic."""
        pass


class DataBaseManager(SingletonInterface):
    """A database manager for user data using PostgreSQL and SQLAlchemy."""
    def _initialize(self):
        """Initialization logic that runs only once."""
        # Do something as if in the constructor
