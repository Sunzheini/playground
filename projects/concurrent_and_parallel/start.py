def run_program(*args, **kwargs):
    if args:
        print(f"args: {', '.join(str(arg) for arg in args)}")
    if kwargs:
        print(f"kwargs: {kwargs}")


"""
Continue with:
https://realpython.com/async-io-python/
Udemy course
Deepseek conversation
"""


if __name__ == "__main__":
    run_program(4, 5)
