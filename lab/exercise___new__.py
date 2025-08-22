class SingletonExample:
    _INSTANCE = None
    _INITIALIZED = False

    def __new__(cls, *args, **kwargs):
        if cls._INSTANCE is None:
            cls._INSTANCE = super().__new__(cls)
        return cls._INSTANCE

    def __init__(self, name: str):
        if not self._INITIALIZED:
            self.name = name
            self._INITIALIZED = True

    def __str__(self):
        return self.name

def execute():
    obj1 = SingletonExample('name1')
    obj2 = SingletonExample('name2')
    print(obj1)
    print(obj2)


if __name__ == "__main__":
    execute()
