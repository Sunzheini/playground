import time


def time_measurement(some_function):
    def wrapper(*args, **kwargs):
        print("starting")
        start = time.time()
        result = some_function(*args, **kwargs)     # the function
        end = time.time()
        measurement = end - start
        print(f"ended: {measurement}")
        return result                               # the function
    return wrapper


def int_validator(some_function):
    def wrapper(*args, **kwargs):
        print("validating")
        try:
            result = some_function(*args, **kwargs)     # the function
            return result
        except TypeError:
            return "Not an int!"
    return wrapper


def decorator_factory(command):
    def decorator_depending_on_command(some_function):
        def wrapper(*args, **kwargs):
            print("dec2")
            result = some_function(*args, **kwargs)  # the function
            if command == 2:
                result += 2
            elif command == 3:
                result += 33
            print("dec2 ended")
            return result  # the function
        return wrapper
    return decorator_depending_on_command


command = int(input())


@time_measurement               # this decorates the result of `int_validator`
@int_validator                  # this decorates the result of `decorator_factory`
@decorator_factory(command)           # executes first
def calculate(a, b):
    result = a + b
    time.sleep(1)
    print(f"calculated: {result}")
    return result


# a = 'ddd'     # to test int_validator
a = 5
b = 4


print(calculate(a, b))

